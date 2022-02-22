import spacy
import pickle

class Ref():
    def __init__(self,doc):
        self.doc=doc
        self.refs=[]
        self.nlp=spacy.load("en_core_web_trf")
        self.tightRules=[
            {"IS_SPACE":True,"OP":"*"},
            {"IS_PUNCT":True,"OP":"?"},
            {"IS_DIGIT":True,"LENGTH":1},
            {"IS_PUNCT":True,"OP":"?"},
            {"ENT_TYPE":"PERSON","OP":"+"},
            {"IS_PUNCT":True,"OP":"?"},
            {"OP":"*"},
            {"ENT_TYPE":"DATE"},
            {"IS_PUNCT":True,"OP":"?"}
        ]
        self.looseRules=[
            {"IS_SPACE":True,"OP":"*"},
            {"IS_PUNCT":True,"OP":"?"},
            {"IS_DIGIT":True},
            {"IS_PUNCT":True,"OP":"?"},
            {"ENT_TYPE":"PERSON","OP":"+"},
            {"IS_PUNCT":True,"OP":"?"},
            {"OP":"*"},
            {"ENT_TYPE":"DATE"},
            {"IS_PUNCT":True,"OP":"?"}
        ]
        self.refRegion=""

    def getRefRegion(self):
        matcher=spacy.matcher.Matcher(self.nlp.vocab)
        matcher.add("ref",[self.tightRules],greedy="LONGEST")
        matches=matcher(self.doc)
        self.refRegion=str(self.doc[matches[0][1]:matches[0][2]])

    def parseRef(self):
        matcher=spacy.matcher.Matcher(self.nlp.vocab)
        matcher.add("ref",[self.looseRules],greedy="LONGEST")
        lines=self.refRegion.split("\n")
        tmp=""
        for i in lines:
            tmp+=i+" "
            doc=self.nlp(tmp)
            matches=matcher(doc)
            if len(matches)>0:
                self.refs.append(str(doc[matches[0][1]:matches[0][2]]))
                tmp=str(doc[:matches[0][1]])+" "+str(doc[matches[0][2]:])
        self.refs.append(tmp)

    def run(self):
        self.getRefRegion()
        self.parseRef()
        return self.refs
            
            




def test():
    doc=pickle.load(open("doc3.pkl","rb"))
    r=Ref(doc)
    r.run()
    print(r.refRegion)
    print(r.refs)
    pass

#test()
    