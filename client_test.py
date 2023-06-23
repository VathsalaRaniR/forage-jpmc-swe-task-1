import unittest
from client3 import getDataPoint,getRatio

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


  def test_getRatio_calculateRatioEqualRatioTwoPrices(self):
    quotes = [
      {'top_ask': {'price': 111.65, 'size': 74}, 'timestamp': '2019-03-08 23:35:56.746472', 'top_bid': {'price': 112.27, 'size': 91}, 'id': '0.23883877413463706', 'stock': 'ABC'},
      {'top_ask': {'price': 111.68, 'size': 33}, 'timestamp': '2019-03-08 23:35:56.746472','top_bid': {'price': 112.39, 'size': 54}, 'id': '0.23883877413463706', 'stock': 'DEF'}
    ]
    for quote in quotes:
      price_a = quote['top_ask']['price']+quote['top_bid']['price']/2
      price_b = quote['top_ask']['price']+quote['top_bid']['price']/2
      print(getRatio(price_a,price_b),price_a/price_b)
      self.assertEqual(getRatio(price_a,price_b),price_a/price_b)



if __name__ == '__main__':
    unittest.main()