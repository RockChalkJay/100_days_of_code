import smtplib

sender_email = "<user>@protonmail.com"
password = "8ClsyOF4n5FV02ENKN0brQ"

with smtplib.SMTP("127.0.0.1:1025") as conn:
    conn.starttls()
    conn.login(user=sender_email, password=password)
    conn.sendmail(
        from_addr=sender_email,
        to_addrs="<user>@gmail.com",
        msg="Subject:Hello...\n\nWorld!!"
    )