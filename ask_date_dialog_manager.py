import datetime

class AskDateDialogManager():

    slot = {
        'TIME' : "วันไหนคะ วันนี้ พรุ่งนี้ เมื่อวาน"
    }

    def transformWordOfDay(self, day):
        day_number = {
            'วันนี้': datetime.datetime.today().weekday(),
            'พรุ่งนี้' : datetime.datetime.today().weekday()+1,
            'เมื่อวาน' : datetime.datetime.today().weekday()-1,
        }
        return day_number[day]

    def transformDayNumberToString(self,day_num):
        day_string = ('จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์')

        return day_string[day_num]

    def action(self, frame_and_slot):
        day = False
        for slot in frame_and_slot:
            if slot[1] == "DAY":
                day = True
                day_number = self.transformWordOfDay(slot[0])
                day_string = self.transformDayNumberToString(day_number)

        if day == False :
            print(self.slot['TIME'])
            return

        print('วัน',day_string,'ค่ะ')