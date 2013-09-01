import unittest
import app

class AppTest(unittest.TestCase):
  def test_say_hello(self):
    self.assertEqual("Hello World", app.App().say_hello())