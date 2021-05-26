import requests
from bs4 import BeautifulSoup
import smtplib

headers = {
    "Accept-Language": "tr,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
}

url = "https://www.amazon.com.tr/Apple-12-9-Tablet-Space-Grey/dp/B086XYT9TL/ref=sr_1_2?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ipad+pro&qid=1619311447&s=computers&sr=1-2"

response = requests.get(url=url, headers=headers)
contents = response.text
# print(contents)
soup = BeautifulSoup(contents, "html.parser")
price = soup.find(name="span", id="priceblock_ourprice").get_text()
title = soup.find(name="span", id="productTitle").get_text()
# print(title.split())
title_tag = ""
for i in title.split():
    title_tag += i
    title_tag += " "
print(title_tag)
price_tag = float(price[1:-3])

price_iwant = 8.000
my_email = "Your_Email"
password = "Your_Password"
email_to_send = "Email_To_Send"

if price_tag > price_iwant:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_to_send,
                            msg=f"Subject:Price Alert\n\n"
                                f"Hey Big day!!! {title_tag.encode('utf-8').strip()} is finally now: {price.encode('utf-8').strip()}! \n\n {url}")






