# =========================================SMTP module=============================================
# import smtplib
#
# my_email = ""
# password = "kgxwxlnvuhbcujoi"
#
# try:
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="",
#                             msg="Subject:hello\n\nThis message was sent using smtplib module")
#
#     print("Email sent successfully!")
#
# except Exception as e:
#     print(f"Error: {e}")
# ============================Date Time module=========================================
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(type(now))
# DOB = dt.datetime(year=2001,month=11,day=7)
# print(DOB)
import smtplib

# ---------------------------EMAIL MOTIVATIONAL QUOTE--------------------------------------------
# import datetime as dt
# import smtplib
# from random import choice
#
# with open("quotes.txt") as file:
#     quotes = file.readlines()
# # print(choice(quotes))
#
# now = dt.datetime.now()
# today = now.weekday()
# if today == 0:
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user="hiteshnarayana007@gmail.com", password="kgxwxlnvuhbcujoi")
#         connection.sendmail(from_addr="hiteshnarayana007@gmail.com",
#                             to_addrs="unknown.hitman.463@gmail.com",
#                             msg=f"Subject:Motivational Monday\n\n{choice(quotes)}")


# ------------------------------------AUTOMATED BIRTHDAY WISHER----------------------------------------------------
import pandas as pd
import datetime as dt
import smtplib
import random

data = pd.read_csv("birthdays.csv")
date = dt.datetime.now()
day = date.day
month = date.month
username = ""
password = "kgxwxlnvuhbcujoi"
# print(date.day)
for (index, row) in data.iterrows():
    if row.month == month and row.day == day:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            content = file.read()
            content = content.replace(f"[NAME]", f"{row['name']}")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=username, password=password)
            connection.sendmail(from_addr=username,
                                to_addrs=row["email"],
                                msg=f"Subject: Happy Birthday!\n\n{content}")
