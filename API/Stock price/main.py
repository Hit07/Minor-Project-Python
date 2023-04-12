import json
import random
import smtplib
import requests
from email.mime.text import MIMEText

stock_endpoint = "https://www.alphavantage.co/query"
stock_api_key = "6G9V8TF2NAZ6UHUN"
news_api_key = '63da9e3570084c61aa3d60c6b98f12d1'

parameter = {
    "function": 'TIME_SERIES_DAILY_ADJUSTED',
    "symbol": "IBM",
    # "interval": "Daily",
    "apikey": stock_api_key,
}
news_parameters = {
    "q": "IBM",
    "from": "2023-04-10",
    "apikey": news_api_key
}
get_news= False
my_email = ""
password = 'fkkegaqosileqouv'



r = requests.get(f"https://www.alphavantage.co/query?", params=parameter)
r.raise_for_status()
data = r.json()['Time Series (Daily)']
# print(data)
with open("ibm.json", mode="w") as file:
    json.dump(data, file, indent=6)
list_data = [value for key, value in data.items()]
eleven = float(list_data[0]["4. close"])
tenth = float(list_data[1]["4. close"])
diff = round(eleven - tenth, 4)
diff_percent = round((abs(diff) / eleven) * 100, 4)
print(diff_percent)
if diff_percent > 0.2:
    get_news = True

if get_news:
    response = requests.get("https://newsapi.org/v2/everything?", params=news_parameters)
    new_data = response.json()["articles"][4:6]
    with open("news.json",mode="w") as file:
        json.dump(new_data,file,indent=6)
    news = [f'{i["title"]}--->{i["description"]}' for i in new_data]
    # msg = MIMEText((random.choice(news)).encode('utf-8'), 'plain', 'utf-8')
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="",
                                msg=f"Subject:Did you Know?!🧐\n{random.choice(news)}".encode("UTF-8"))

    except Exception as e:
        print(f"Error: {e}")

    else:
        print("Email sent successfully!")
