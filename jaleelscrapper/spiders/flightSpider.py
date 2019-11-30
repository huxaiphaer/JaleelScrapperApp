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

        flights = JaleelscrapperItem()

        for data in json_data['monitor']['departure']:
            note = ''
            destination = data['destinations'][0]['nameEN']
            time = data['scheduledatetime']
            """ Make request to the weather API"""
            r = requests.get(
                "http://api.weatherstack.com/forecast?access_key=54641e77096d3e2d3b4c4e51c212e8f0&query=" + destination)
            weather_data = r.json()
            temperature = weather_data["current"]["temperature"]

            if temperature > 25:
                note = "Let's go for a pint"
            elif temperature < 5:
                note = "!Que frio!"
            else:
                note = "Zmerno vreme"

            flights['destination'] = destination
            flights['time'] = time
            flights['temperature'] = temperature
            flights['note'] = note
            yield flights
