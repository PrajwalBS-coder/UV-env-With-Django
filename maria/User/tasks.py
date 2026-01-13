from celery import shared_task
from maria.celery import app
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone

time_literal="%I:%M %p"


@app.task(name="send_email_task", bind=True)
def send_email_task(self):
    print(f"CELERY TASK FUNCTION:{self.request!r}")

    API_KEY = settings.OPEN_WEATHER_API_KEY   # get from openweathermap.org
    CITY = "Bangalore"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    data = requests.get(URL).json()
    print(data)
    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    print(f"🌤️ Today in {CITY}: {temp}°C, {condition}")
    data={'coord': {'lon': 77.6033, 'lat': 12.9762}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 20.7, 'feels_like': 20.84, 'temp_min': 20.7, 'temp_max': 20.7, 'pressure': 1015, 'humidity': 77, 'sea_level': 1015, 'grnd_level': 917}, 'visibility': 10000, 'wind': {'speed': 4.16, 'deg': 107, 'gust': 7.14}, 'clouds': {'all': 97}, 'dt': 1768136928, 'sys': {'country': 'IN', 'sunrise': 1768094079, 'sunset': 1768135177}, 'timezone': 19800, 'id': 1277333, 'name': 'Bengaluru', 'cod': 200}
    timezone = ZoneInfo("Asia/Kolkata")

    sunrise_time = datetime.fromtimestamp(data['sys']['sunrise'], tz=timezone)
    sunset_time = datetime.fromtimestamp(data['sys']['sunset'], tz=timezone)

    print(data['main']['temp'])
    print(data['main']['feels_like'])
    print(data['weather'][0]['main'])
    print(data['main']['humidity'])
    print(data['wind']['speed'])
    print(sunrise_time.strftime(time_literal))
    print(sunset_time.strftime(time_literal))


    subject = "Weather Update"
    message_body = f"Today in {CITY}: {temp}°C, {condition}"
    html_body = render_to_string('weather.html', {'name':"Legend Amin",
                            'temperature': temp, 
                                'weather_condition': condition, 
                                'city': CITY, 
                                'sunrise_time': sunrise_time.strftime(time_literal), 
                                'sunset_time': sunset_time.strftime(time_literal),
                                'feels_like': data['main']['feels_like'],
                                'humidity': data['main']['humidity'],
                                'wind_speed': data['wind']['speed'],
                                'date_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                }
                                )


    senders_email=settings.EMAIL_HOST_USER
    recipients=[settings.RECIPETENT_EMAIL]



    send_mail(
            subject=subject,
            message=message_body,
            html_message=html_body,
            from_email=senders_email,
            recipient_list=recipients 
            )




