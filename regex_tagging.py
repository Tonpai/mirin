import os
import nltk

from intent_parser import IntentParser
from thai_cutting_word import ThaiCuttingWord
from main_dialog_manager import MainDialogManager

os.system("clear")

#What day is date ?
if __name__ == "__main__":
    # User Input
    user_utterance = "สวัสดีครับวันนี้วันอะไรครับ"

    # Natural Language Understanding
    # Simple NLU
    cutter = ThaiCuttingWord()
    cutted_word_list = cutter.cutWordOf(user_utterance)

    intent_parser = IntentParser()
    slot = intent_parser.parseString(cutted_word_list)

    # Dialog Manager and NLG(Build-in Dialog system)
    dm = MainDialogManager()
    dm.action(slot)