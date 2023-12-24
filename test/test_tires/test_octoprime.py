import unittest

from tires.model.octoprime import *


class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        tires = Octoprime([0.9, 0.9, 0.8, 0.8])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires = Octoprime([0.5, 0.5, 0.5, 0.5])
        self.assertFalse(tires.needs_service())
