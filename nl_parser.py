#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
from thai import Thai

class NLParser:

    CFG = nltk.CFG.fromstring(Thai.CONTEXT_FREE_GRAMMAR)

    def convertToTree(self, sentence):
        rd_parser = nltk.RecursiveDescentParser(self.CFG)
        sent = 'หนังสือ สาม เล่ม นี้ มี ประโยชน์'.split()
        for tree in rd_parser.parse(sent):
            print(tree)
        