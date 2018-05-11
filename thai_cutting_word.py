import deepcut

class ThaiCuttingWord(object):

#High Accuracy
#Add dictionary
    def cutWordOf(self,user_utterance):
        words = deepcut.tokenize(
            user_utterance, 
            custom_dict='./custom_dict.txt'
        )
        return words