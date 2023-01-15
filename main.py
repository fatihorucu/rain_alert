import requests as rq
from twilio.rest import Client
parameters = {
    "lat": 41.024620,
    "lon": 40.522920,
    "exclude": "current,minutely,daily,alerts",
    "appid": "# U can get it from api.openweathermap",
}
account_sid = "#  U can get it from api.openweathermap"
auth_token = "# U can get it from api.openweathermap"

response = rq.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
data = response.json()
is_rainy = False
for item in data["hourly"][0:12]:
    weather = [item["weather"][0]]
    for x in weather:
        if x["id"] < 700:
            is_rainy = True
if is_rainy:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is rainy today, take umbrella",
        from_="+13854328617",
        to="+905060264009"
    )
    print(message.status)