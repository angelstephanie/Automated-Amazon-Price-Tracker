import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "sender's email"
password = "my_email's password"
url = "https://www.amazon.com/Sony-Noise-Cancelling-Headphones-WH1000XM3/dp/B07G4YL6BM/ref=sr_1_11?crid=D49680FECA96&dchild=1&keywords=sony+headphones&qid=1629474786&sprefix=sony+head%2Caps%2C473&sr=8-11"

response = requests.get(url=url, headers={'Accept-Language': "en-US,en;q=0.9", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'})
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")

item_name = soup.find(id="productTitle").getText().replace("\n", "")
item_price = float(soup.find(name="span", id="priceblock_ourprice").getText().split("$")[1])
print(item_name)
if item_price < 220.0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="receiver's email",
                            msg=f"Subject:Low Price Alert!\n\n{item_name} is now only ${item_price}!\n{url}".encode("utf-8")
                            )
        print("email sent")


