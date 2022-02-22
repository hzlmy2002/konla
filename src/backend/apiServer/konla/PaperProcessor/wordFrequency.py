import collections
import spacy

class wordFrequency():
    def __init__(self,doc:"spacy.tokens.doc.Doc",max=10,ignoreCase=False,useLemma=False) -> None:
        self.doc = doc
        self.max = max
        self.ignoreCase = ignoreCase
        self.useLemma = useLemma

    def getWordFrequency(self) -> dict:
        wordList=[]
        for token in self.doc:
            if token.is_stop or token.is_punct or token.is_space or token.is_bracket or len(token.text)<4:
                continue
            if not self.useLemma:
                if self.ignoreCase:
                    wordList.append(token.text.lower())
                else:
                    wordList.append(token.text)
            else:
                wordList.append(token.lemma_)
    
        wordFreq = collections.Counter(wordList)
        wordDesc=wordFreq.keys()
        wordDesc=sorted(wordDesc,key=lambda x:wordFreq[x],reverse=True)
        result={}
        for word in wordDesc[:self.max]:
            result[word]=wordFreq[word]
        return result
            