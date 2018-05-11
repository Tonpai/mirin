from greeting_dialog_manager import GreetingDialogManager
from ask_date_dialog_manager import AskDateDialogManager

class MainDialogManager():
    def action(self, frame_and_slot):
        print("OK")
        for slot in frame_and_slot:
            
            if slot[1] == "INTENT":
                if slot[0] == 'สวัสดี':
                    greeting_dm = GreetingDialogManager()
                    greeting_dm.action(frame_and_slot)
                if slot[0] == "วันอะไร":
                    ask_date_dm = AskDateDialogManager()
                    ask_date_dm.action(frame_and_slot)