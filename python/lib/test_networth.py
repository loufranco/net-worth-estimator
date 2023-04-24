from lib.networth import netWorthByAge
import unittest

class TestNetWorth(unittest.TestCase):
    
    def test_net_worth_simple(self):
        self.assertEqual(netWorthByAge([25]), [10000])

    def test_net_worth_two_ages(self):
        self.assertEqual(netWorthByAge([25, 26], 0, 10000, 0, 0), [10000, 10600])