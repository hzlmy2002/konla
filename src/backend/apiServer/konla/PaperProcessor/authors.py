
class AuthorParser():
    def __init__(self,doc):
        self.doc=doc
        self.names=[]


    def getConsecutiveNames(self):
        counter=0
        for i in self.doc.ents:
            if i.label_=="PERSON":
                self.names.append(i.text)
            else:
                if counter >5:
                    break
                counter+=1

    def run(self):
        self.getConsecutiveNames()
        return self.names

"""
def test():
    nlp=spacy.load("en_core_web_trf")
    with open("/tmp/typestudy.txt") as file:
        text=file.read()
    doc=nlp(text)
    ap=AuthorParser(doc)
    aaa=ap.run()
    pass

#test()
"""