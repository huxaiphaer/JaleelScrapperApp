from scrapy import Request

from jaleelscrapper.spiders.flightSpider import FlightDestinationSpider


class TestSpider(FlightDestinationSpider):
    name = 'test1'
    test_urls = [
        "https://www.viennaairport.com/jart/prj3/va/data/flights/out.json?dummy=Rc7a6248Xb56e1c9",
    ]

    def start_requests(self):
        for url in self.test_urls:
            yield Request(url, self.parse)
