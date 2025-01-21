from email import message
from unittest import result
from bs4 import BeautifulSoup
import requests
import smtplib

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url = practice_url)

soup = BeautifulSoup(response.content, "html.parser")
price = soup.find(class_ = "a-offscreen").getText()

price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)


title = soup.find(id = "productTitle").getText().strip()

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port = 587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(from_addr=YOUR_EMAIL, to_addrs=YOUR_EMAIL, msg = f"Subject: Amazon Price Alert\n\n{message}\n{live_url}".encode("utf-8"))