import spacy
import re
# COMP0016-Team6-Minyi Lei
class Ref():
    def __init__(self,doc,nlp):
        self.doc=doc
        self.refs=[]
        self.nlp=nlp
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
        self.refRegion=""

    def getRefRegion(self):
        matcher=spacy.matcher.Matcher(self.nlp.vocab)
        matcher.add("ref",[self.tightRules],greedy="LONGEST")
        matches=matcher(self.doc)
        self.refRegion=str(self.doc[matches[0][1]:matches[0][2]])

    def parseRef(self):
        lines=self.refRegion.split("\n")
        sequenceNumberPattern=r"^\[\d+\]"
        tmp=""
        for i in lines:
            isHitted= len(re.findall(sequenceNumberPattern,i.strip())) > 0
            if isHitted:
                if len(tmp.strip()) > 0:
                    self.refs.append(tmp)
                    tmp=""
            tmp= tmp+" "+i.strip()
        self.refs.append(tmp)

    def run(self):
        self.getRefRegion()
        self.parseRef()
        self.refs=list(map(lambda x:x.strip(),self.refs))
        return self.refs
