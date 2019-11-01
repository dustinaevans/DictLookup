CT = "LOFYSDJ LZDPX' MDPPOVZOAI LSXR OA YSJJGNDDA OX SFMESJJZ FSWMSOA ROPR ROAU GV MYD LSXR OX LGUDJDU SVMDP' NOJJOSL XYSMADP'X VSFD HEM WSOAMDU NYOMD"

class DictLookup:

    def __init__(self):
        pass

    def update(self, ct):
        self.ct = ct

    def findPattern(self,pattern):
        pass

    def initDict(self,dictionary):
        fd = open(dictionary,'r')
        self.dictionary = fd.read()

    def populateCTWords(self):
        self.words = []
        wordcount = 0
        self.words.append('')
        for i in self.ct:
            if i==' ':
                wordcount += 1
                self.words.append('')
            elif i=='\n':
                pass
            else:
                self.words[wordcount] += i

    def printCTWords(self):
        for i in self.words:
            print(i)

dl = DictLookup()

dl.update(CT)
dl.initDict('./words_dictionary.json')
dl.populateCTWords()
dl.printCTWords()
