import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculatePriceBidEqualOne(self):
    quotes = [
      {'top_ask': {'price': 112.39, 'size': 91}, 'timestamp': '2019-03-06 06:40:35.041441', 'top_bid': {'price': 112.27, 'size': 91}, 'id': '0.749348412931592', 'stock': 'ABC'},
      {'top_ask': {'price': 111.68, 'size': 33}, 'timestamp': '2019-03-06 06:40:35.041441','top_bid': {'price': 112.39, 'size': 54}, 'id': '0.749348412931592', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(((quote['top_ask']['price'] + quote['top_bid']['price']) / 2)/((quote['top_ask']['price'] + quote['top_bid']['price']) / 2), 1)

  def test_getRatio_calculatePriceBidNotEqualOne(self):
    quotes = [
      {'top_ask': {'price': 111.65, 'size': 74}, 'timestamp': '2019-03-08 23:35:56.746472', 'top_bid': {'price': 112.27, 'size': 91}, 'id': '0.23883877413463706', 'stock': 'ABC'},
      {'top_ask': {'price': 111.68, 'size': 33}, 'timestamp': '2019-03-08 23:35:56.746472','top_bid': {'price': 112.39, 'size': 54}, 'id': '0.23883877413463706', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertNotEqual(((quote['top_ask']['price'] + quote['top_bid']['price']) / 2)/((quote['top_ask']['price'] + quote['top_bid']['price']) / 2), 1.00001)


if __name__ == '__main__':
    unittest.main()