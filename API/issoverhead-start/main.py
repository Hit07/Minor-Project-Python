import smtplib
import requests
from datetime import datetime
import time

MY_LAT = -40.7289  # Your latitude
MY_LONG = -40.7289  # Your longitude
my_email = ''
password = "ruiqfmdbmldgqynb"


def nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # print(iss_longitude, iss_longitude)
    if MY_LONG - 10 <= iss_longitude <= MY_LONG + 10 and MY_LAT - 10 <= iss_latitude <= MY_LAT + 10:
        # print("run")
        return 1


# Your position is within +5 or -5 degrees of the ISS position.

def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    # print(sunrise, sunset, time_now)
    if sunset <= time_now <= sunrise:
        # print("run")
        return 1


while True:
    time.sleep(60)
    if nearby() == night():
        print("yes")
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs="",
                                    msg=f"Subject:LOOK UP👆🏻 \n\n ISS is above you in the sky🌌!!")
            print("successful")
        except Exception as e:
            print(e)
