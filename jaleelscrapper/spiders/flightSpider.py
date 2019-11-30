import datetime
import json
import requests
import scrapy
from ..items import JaleelscrapperItem


class FlightDestinationSpider(scrapy.Spider):
    name = 'flights_destinations'
    start_urls = [
        "https://www.viennaairport.com/jart/prj3/va/data/flights/out.json?dummy=Rc7a6248Xb56e1c9"
    ]

    def parse(self, response):
        json_data = json.loads(response.body)

        item = JaleelscrapperItem()

        for data in json_data['monitor']['departure']:
            note = ''
            destination = data['destinations'][0]['nameEN']

            time = data['scheduledatetime']

            formatted_time = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%fZ').time()

            # Make request to the weather API and return response.
            r = self.get_weather_response(destination)
            weather_data = r.json()

            try:

                temperature = weather_data["current"]["temperature"]
                if temperature > 25:
                    note = "Let's go for a pint"
                elif temperature < 5:
                    note = "!Que frio!"
                else:
                    note = "Zmerno vreme"

                item['destination'] = destination
                item['time'] = formatted_time
                item['temperature'] = temperature
                item['note'] = note
                yield item
            except KeyError:
                yield {"error": "error"}

    def get_weather_response(self, destination):
        return requests.get(
            "http://api.weatherstack.com/forecast?access_key=3ffdb844e799259dbbbb67768547d033&query=" + destination)
