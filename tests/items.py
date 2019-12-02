from scrapytest import ItemSpec
from scrapytest.tests import Type, Match, MoreThan

from jaleelscrapper.items import JaleelscrapperItem


class TestFlights(ItemSpec):
    item_cls = JaleelscrapperItem

    # defining field tests
    destination_test = Type(str)
    time_test = Type(str)
    temperature_test = Type(int), MoreThan(0)
    note_test = Type(str)

    def url_test(self, value: str):
        if not value.startswith('http'):
            return f'Invalid url: {value}'
        return ''