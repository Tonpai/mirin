import nltk
from thai_pattern import ThaiIntentPattern

class IntentParser:
    pattern = ThaiIntentPattern.pattern

    def parseString(self, utteranceArray):
        tagger = nltk.RegexpTagger(self.pattern)
        slot = tagger.tag(utteranceArray)
        return slot