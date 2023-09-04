from textbase import bot,Message
from typing import List
import requests

class OpenWeather:
    # Initialize the open weather object with Api key
    def __init__(self,API_KEY: str = None):
        self.apiKey = API_KEY

    # generate function used to get the current weather at given location
    def generate(
        self,
        messageHistory: list[Message],
        ):
        try:
            assert self.apiKey is not None,"Open Weather Api Key is required"
            header = {"Content-Type": "application/json"}
            geocordingURI = f"http://api.openweathermap.org/geo/1.0/direct?q="
            openweatherURI = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}"

            location = messageHistory.pop(-1)["content"][0]["value"];
            geocordingURI += f"{location}&limit=5&appid={self.apiKey}"
            response = requests.request('GET',geocordingURI,header)
            print("response:  ",response)
            openweatherURI += f"&appid={self.apiKey}"
            
        except Exception:
            return print(f"An exception occured while using this model, please try using another model.\n")


# Load your OpenWeather API key https://home.openweathermap.org/api_keys
openWeather = OpenWeather("9fd394cabeeb8557de6f5fe17eeaaa18")

@bot()
def on_message(message_history: List[Message], state: dict = None):
    openWeather.generate(messageHistory=message_history)