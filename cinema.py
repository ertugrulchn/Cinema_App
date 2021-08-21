# Sinema Örnek Uygulaması
# 04.08.2021
# ********************* #

import smtpserver as server

person_select_input = int(
    input("ÖĞRENCİYSENİZ 1, SİVİLSENİZ 2 NUMARASINI GİRİNİZ: "))
student_ticket_price = 7.5
full_ticket_price = 15

def cinema(select_process):
    if select_process == 1:
        film_name = str(input("FİLM ADI GİRİNİZ: "))
        print(film_name)
    elif select_process == 2:
        seat_number = int(input("KOLTUK NUMARASI GİRİNİZ(MAX=50): "))
        print(seat_number)
    elif select_process == 3:
        person_number = int(input("KİŞİ SAYISI GİRİNİZ: "))
        if person_select_input == 1:
            person_number *= student_ticket_price
        elif person_select_input == 2:
            person_number *= full_ticket_price          

def person_select():
    if person_select_input == 1:
        cinema(1)
        cinema(2)
        cinema(3)
    elif person_select_input == 2:
        cinema(1)
        cinema(2)
        cinema(3)
    else:
        print("HATALI BİR NUAMRA GİRDİNİZ.")

def factor():
    server.send_mail()

person_select()
factor()