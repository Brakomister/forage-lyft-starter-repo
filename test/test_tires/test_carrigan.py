import unittest

from tires.model.carrigan import *


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        tires = Carrigan([0.9, 0.9, 0.8, 0.8])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires = Carrigan([0.8, 0.7, 0.8, 0.7])
        self.assertFalse(tires.needs_service())
