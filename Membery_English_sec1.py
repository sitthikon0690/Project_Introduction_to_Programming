#นาย ชนาธิป ปรีชา 6530611020
#นาย สิทธิกร ชมภูพื้น 6530611030
#นาย ภานุพงค์ ชมภูพื้น 6530611031

def Membery_English():
    # a+	เปิดไฟล์เพื่อเขียนข้อมูลต่อท้ายและอ่านข้อมูลจากไฟล์ ถ้าหากไม่มีไฟล์อยู่จะสร้างไฟล์ใหม่
    vocabulary_a=open('./Python/0Python_Classroom/เพิ่มคำศัพท์_sec1/vocabulary.txt','a+')
    vocabulary_r=open('./Python/0Python_Classroom/เพิ่มคำศัพท์_sec1/vocabulary.txt','r')
    translate_a=open('./Python/0Python_Classroom/เพิ่มคำศัพท์_sec1/translate.txt','a+',encoding="utf-8")
    translate_r=open('./Python/0Python_Classroom/เพิ่มคำศัพท์_sec1/translate.txt','r',encoding="utf-8")
    key = input('ต้องการเก็บคำศัพท์พิมพ์ : W\nดูคำศัพท์พิมพ์ : P\nต้องการเล่นเกมพิมพ์ : G\n : ')
    key=key.upper()
    if key == 'W':
        new_vocabulary=input('กรอกคำศัพท์ : ').capitalize()
        check = None
        for v,t in zip(vocabulary_r,translate_r):
            if new_vocabulary == v[:-1]:
                print("คำศัพท์มีบันทึกอยู่แล้ว")
                print(v[:-1],'   แปลว่า   ',t)
                check = 0
        if check != 0:
            new_translate=input('คำแปลที่ต้องการเก็บ : ')
            vocabulary_a.writelines('%s\n'%(new_vocabulary))
            translate_a.writelines('%s\n'%(new_translate))
    elif key == 'P':
        for v,t in zip(vocabulary_r,translate_r):
                print(v[:-1],'   แปลว่า   ',t)
    elif key == 'G':
        import random
        readlines_vocabulary_r=vocabulary_r.readlines()
        readlines_translate_r=translate_r.readlines()
        frequency=int(input('ระบุจำนวนรอบ : '))
        for i in range(frequency):
            random_game=random.choice(readlines_vocabulary_r)
            print('\n : ',random_game)
            answer=input('กรอกคำตอบ(คำแปล) : ')
            random_game_index=readlines_vocabulary_r.index(random_game)
            correct_answer=readlines_translate_r[random_game_index]
            if correct_answer[:-1] == answer:
                print('คำตอบถูกต้อง')
            else:
                print('คำตอบไม่ถูก')
                print('คำตอบที่ถูกคือ : %s'%(correct_answer))
    else:
        print('กรอก Key ไม่ถูกต้อง')
    print('='*100) 
    vocabulary_a.close
    vocabulary_r.close
    translate_a.close
    translate_r.close
Membery_English()

