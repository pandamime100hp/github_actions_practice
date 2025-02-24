import unittest

from src.hello_world import hello_world


class TestMain(unittest.TestCase):
    def test_main(self):
        output = hello_world()
        self.assertEquals(output, "Hello World")