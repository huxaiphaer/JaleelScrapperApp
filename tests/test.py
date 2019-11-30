import subprocess
import sys
import unittest

from scrapy import Spider
from scrapy.http import Request

from jaleelscrapper.jaleelscrapper.items import JaleelscrapperItem
from jaleelscrapper.jaleelscrapper.spiders.flightSpider import FlightDestinationSpider


class TestParsers(unittest.TestCase):

    def setUp(self):
        self.item = JaleelscrapperItem()

    def test_destination(self):
        """Test destination filed """
        expected = "New York"
        result = self.item['destination'] = "New York"
        self.assertEqual(result, expected)

    def test_time(self):
        """Test time filed """
        expected = "12:00:00"
        result = self.item['time'] = "12:00:00"
        self.assertEqual(result, expected)

    def test_temperature(self):
        """Test temperature filed """
        expected = 23
        result = self.item['temperature'] = 23
        self.assertEqual(result, expected)

    def test_note(self):
        """Test note filed """
        expected = "!Que frio!"
        result = self.item['note'] = "!Que frio!"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
