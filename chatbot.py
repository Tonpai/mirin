from nl_parser import NLParser

class Chatbot:

    natural_lang_parser = NLParser()

    def __init__(self):
        print("Hello")

    def start(self):
        
        #READ UserInput
        #WHILE UserInput != Thank :
        #   TreeStructure = CFG_Parser(UserInput)
        #   ANALYSIS ()
        #   WRITE TreeStructure
        #   READ UserInput

        user_input = input("You >> ")
        while user_input != "thank":
            self.natural_lang_parser.convertToTree(sentence = user_input)
            
            user_input = input("You >> ")

            