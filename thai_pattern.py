class ThaiIntentPattern:
    pattern = [
        (r'(วันนี้|พรุ่งนี้|เมื่อวาน)','DAY'),
        (r'(วันอะไร|สวัสดี)$','INTENT')
    ]
    #     pattern = [
    #     (r'(สวัสดี)(ครับ|ค่ะ|$)','I_GREETING'),
    #     (r'วันที่|วันนี้|(วัน|^)(อาทิตย์|จันทร์|อังคาร|พุธ|พฤหัสบดี|ศุกร์|เสาร์)','DAY'),
    #     (r'(วันที่ |^)\d','DATE'),
    #     (r'(เดือน|^)((มกรา)(คม|$)|(เมษา)(ยน|$)|(กุมภา)(พันธ์|$))','MONTH'),
    #     (r'(อะไร|เท่าไหร่)','I_QUESTION'),
    #     (r'(วันที่เท่าไหร่)','INTENT')
    # ]