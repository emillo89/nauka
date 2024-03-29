import requests
import datetime as dt
import smtplib
import time

MY_LAT = 51.507351
MY_LONG = -0.127758
my_email = "appbrewery5@gmail.com"
password = "testowe1234"


def is_iss_overhead():
    """
    Check the latitude and longitude locations is in the given condition
    return:
    boolean: True or False
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    """
    See if it's nighttime now
    return:
    boolean: True or False
    """

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data =response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="emilszczesniak@yahoo.com",
                                msg="Subject: Look Up\n\n The ISS is above you in the sky.")

