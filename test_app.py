import unittest
from app import table_html

class TestApp(unittest.TestCase):
	def test_table_html(self):
		self.assertEqual(table_html(20))

if __name__ == "__main__":
	unittest.main()
