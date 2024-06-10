import smtplib
import random
import datetime

sender_email = "<from-email>"
to_mail = "<to-email>"
password = "<password>"


def send_mail(msg, to_addr):
    with smtplib.SMTP("127.0.0.1:1026") as conn:
        conn.starttls()
        conn.login(user=sender_email, password=password)
        conn.sendmail(
            from_addr=sender_email,
            to_addrs=to_addr,
            msg="Subject:Quote of the Day\n\n" + msg
        )


def get_qoute():
    with open("quotes.txt", 'r') as quotes_file:
        quotes = quotes_file.readlines()
        return random.choice(quotes)


now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 0:  # Monday
    send_mail(get_qoute(), to_mail)

