import datetime as dt
import email
import random
import smtplib
import pandas as pd
import smtplib

MY_EMAIL = "appbrewaryinfo@gmail.com"
PASSWORD = "abcd1234()"

today = (dt.datetime.now().month, dt.datetime.now().day)
df = pd.read_csv("data/birthdays.csv")

birthdays_dict = {(data['month'], data['day']) : data for (index, data) in df.iterrows() }

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"data/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg = f"Subject: Happy Birthday\n\n{contents}")
        




