import requests
from datetime import datetime
import smtplib
import time

# === USER CONFIGURATION ===
EMAIL = "example@example.com"
PASSWORD = "yourpassword"
MY_LAT = 51.507351     # e.g. London
MY_LONG = -0.127758
CHECK_INTERVAL = 60    # seconds between checks
# ===========================

def is_iss_overhead():
    """Returns True if the ISS is within ±5° latitude/longitude of the user."""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)

def is_night():
    """Returns True if it's currently nighttime at the user's location."""
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

    time_now = datetime.utcnow().hour  # UTC because API uses UTC
    return time_now >= sunset or time_now <= sunrise

def send_notification():
    """Sends an email alert that the ISS is overhead."""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look Up 👀\n\nThe ISS is above you in the sky!"
        )

# === MAIN LOOP ===
while True:
    time.sleep(CHECK_INTERVAL)
    try:
        if is_iss_overhead() and is_night():
            send_notification()
    except Exception as e:
        print(f"Error: {e}")
