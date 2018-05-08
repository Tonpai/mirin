import nltk
from thai import Thai

class NLParser:

    CFG = Thai.context_free_grammar

    def convertToTree(self, sentence):
        rd_parser = nltk.RecursiveDescentParser(self.CFG)
        sent = 'หนังสือ สาม เล่ม นี้ มี ประโยชน์'.split()
        for tree in rd_parser.parse(sent):
            print(tree)
        