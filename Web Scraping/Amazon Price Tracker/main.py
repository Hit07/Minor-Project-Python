import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

API_ENDPOINT = "https://www.amazon.com/SAMSUNG-Factory-Unlocked-Android-Smartphone/dp/B0BLP2Y34S/ref=sr_1_1_sspa?crid" \
               "=2X4QDLFDZF9Z3&keywords=s23+ultra&qid=1697461725&sprefix=s23%2Caps%2C323&sr=8-1-spons&sp_csd" \
               "=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
API_ENDPOINT_1 = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

MAIL = ""
PASSWORD = ''

HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;"

}

r = requests.get(API_ENDPOINT_1, headers=HEADER)
r.raise_for_status()
web_contents = r.text

tracker = BeautifulSoup(web_contents, "lxml")
name = tracker.find(name="span", id="productTitle")
price = tracker.find(name="span", class_="a-price-whole")
price_decimal = tracker.find(name="span", class_="a-price-fraction")

if price:
    price_text = price.get_text().rstrip()
    price_int = ''.join(filter(str.isdigit, price_text))
    # print(price_int)
    if int(price_int) < 100:
        print("......")
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MAIL, password=PASSWORD)
            connection.sendmail(from_addr=MAIL,
                                to_addrs="",
                                msg=f"Subject:hello\n\n{name.getText().strip()}\n"
                                    f"Price:{price_text}{price_decimal}")

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")
else:
    print("Price not found on the page.")


