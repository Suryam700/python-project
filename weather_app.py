import requests
import os
import json

city = input("Enter your city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=c7a5f9a8a93d472490b70835251210&q={city}"
response = requests.get(url) 

weather_dic = json.loads(response.text)
temperature = weather_dic["current"]["temp_c"]
print(f"Temperature in {city} is {temperature}°C")

info_for_speak = f"temperature in {city} is {temperature} degree celcius"
command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{info_for_speak}\')"'
os.system(command)