from scrapytest import StatsSpec
from scrapytest.tests import Equal

from jaleelscrapper.spiders.flightSpider import FlightDestinationSpider


class TestStats(StatsSpec):
    spider_cls = FlightDestinationSpider
    validate = {
        **StatsSpec.validate,  # include defaults
        # should be as many results as there are urls scheduled
        'item_scraped_count': Equal(len(FlightDestinationSpider.test_urls)),
    }
