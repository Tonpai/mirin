#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Thai:
    CONTEXT_FREE_GRAMMAR = """  S -> NP VP
                                VP -> V | V NP | V NP S | V NP PP ADV
                                PP -> PREP NP
                                V -> VERB | LAUX VERB | VERB RAUX | LAUX VERB RAUX
                                NP -> N | N DET | N CLAS DET | N CLAS VATT | N NUM CLAS DET | N VATT CLAS DET | NP PP | NP CONJ NP 
                                N -> 'คน' | 'แมว' | 'ลิง' | 'ถนน' | 'ข้าว' | 'ลาย' | 'เขา' | 'หนังสือ' | 'นก' | 'ของ' | 'เพื่อน' | 'ฉัน' | 'มหาวิทยาลัย' | 'หมา' | 'ทอม' | 'ของ' | 'เรา' | 'ประโยชน์' | 'เงิน'
                                VERB -> 'กิน' | 'นอน' | 'เดิน' | 'เล่น' | 'วิ่ง' | 'ทำ' | 'ซื้อ' | 'พบ' | 'ชอบ' | 'มี' | 'เป็น' | 'อยาก'
                                ADV -> 'ดี' | 'ชั่ว' | 'ใหญ่' | 'ขาว' | 'ร้อน' | 'เย็น' | 'หอม' | 'หวาน' | 'กลม' | 'แบน' | 'เอง' | 'นี้' | 'นั่น' | 'โน่น' | 'ทั้งนี้' | 'ทั้งนั้น' |  'แน่นอน' | 'เป็น'
                                PREP -> 'ของ' | 'และ' | 'ที่'
                                DET -> 'เกือบ' | 'นี้' | 'ทั้ง' | 'อีก' | 'ต่างๆ' | 'กว่า'
                                CLAS -> 'บาท' |  'ชั่วโมง' | 'สาย' | 'เล่ม'
                                NUM -> 'หนึ่ง' | 'สอง' | 'สาม' | 'สี่' | 'ห้า' | 'หก' | 'เจ็ด' | 'แปด' | 'เก้า'
                                LAUX -> 'กำลัง' | 'จะ' | 'ได้' | 'แล้ว' | 'ต้อง' | 'อย่า'  | 'จง' | 'โปรด' | 'ช่วย' | 'ควร' | 'คงจะ' | 'อาจจะ' | 'ค่อย'
                                RAUX -> 'เป็น' | 'เหมือน' | 'คล้าย' | 'เท่า' | 'คือ' | 'เสมือน' | 'ดุจ' | 'บน' | 'เล่น' | 'ได้'
                                CONJ -> 'ถึงกับ' | 'เมื่อก่อน' | 'ต่อมา' | 'ทั้งนี้ทั้งนั้น' | 'จึง' | 'หรือ' | 'และ'
                                VATT -> 'ดี' | 'ยิ่ง' | 'หลัก'     
    """