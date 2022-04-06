# COMP0016-Team6-Minyi_Lei
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