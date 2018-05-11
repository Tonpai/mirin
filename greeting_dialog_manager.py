import random

class GreetingDialogManager():
    
    slot = {
        'HELLO' : [
            'สวัสดีค่ะ',
            'ค่ะ สวัสดีค่ะ',
            'ยินดีที่ได้คุยกันอีกค่ะ',
        ]
    }

    def action(self, frame_and_slot):
        print(self.slot['HELLO'][random.randint(0,2)])