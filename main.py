import smtplib
from email.mime.text import MIMEText
from password import data
from emails import email

def send_func(message, itera, email):
    login = 'skuybedin.nik@gmail.com'
    password = data

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(login, password)
        msg = MIMEText(message)
        msg["Subject"] = "Тема письма"
        server.sendmail(login, email, msg.as_string())
        return f'Письмо {itera+1} успешно отправлено'
    except Exception as e:
        return f"{e}\nПароль введён неверно!"

def main():
    message = input("Введите желаемое письмо: ")
    for i in range(len(email)):
        print(send_func(message=message, itera=i, email=email[i]))

if __name__ == '__main__':
    main()