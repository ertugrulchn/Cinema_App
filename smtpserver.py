import smtplib
import random 

def send_mail(): 
    sender_email = "mailadress@mailadress.com"
    rec_email = input(str("Email Adresinizi Giriniz: "))
    password = input(str("Lütfen Şifreni Gir: "))
    message = random.randint(1000, 9999)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("Giriş Başarılı")
    server.sendmail(sender_email, rec_email, str(message))
    print("Mesajınız ", rec_email, " Adresine Başarıyla Gönderildi.")

    factor_code = int(input("Lütfen Mail Adresinize Gelen Kodu Giriniz: "))

    if factor_code == message:
        print("Kod Doğrulanmıştır Keyfli Seyirler Dileriz.")
    else:
        print("Lütfen Doğru Bir Kod Girdiğinizden Emin Olun.")