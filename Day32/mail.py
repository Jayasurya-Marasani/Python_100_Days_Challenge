import smtplib

my_email = "appbreweryinfo@gmail.com"
password = "abcd1234()"
with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user = my_email, passowrd = password)
    connection.sendmail(from_addr=my_email, 
                    to_addrs="appbrewerytesting@yahoo.com", msg = "Subject: Hello\n\nBody of the Mail")
# connection.close()