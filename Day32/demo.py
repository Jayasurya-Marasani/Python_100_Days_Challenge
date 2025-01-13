import datetime as dt
from re import M
import smtplib
import random
import os
os.system("cls")
MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"
current_date = dt.datetime.now()
weekday = current_date.weekday()

if weekday==0:
    with open("quote.txt", encoding="UTF-8") as file:
        quote_lines = file.readlines()
        quote = random.choice(quote_lines)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg =f"Subject: Monday Motivation\n\n{quote}")

