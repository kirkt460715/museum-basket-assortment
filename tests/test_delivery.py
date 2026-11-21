"""核对交接文件中的来源依据。"""
import unittest
from inspect_delivery import read_table


class DeliveryTest(unittest.TestCase):
    def test_linked_records(self):
        visits = {r["basket"] for r in read_table("baskets.json")}
        orders = read_table("lines.json")
        self.assertLess({r["basket"] for r in orders}, visits)
        self.assertTrue(any(r["reason"] == "赠品" for r in orders))
        self.assertTrue(any(r["offer_type"] == "alt" for r in read_table("exposure.json")))
        self.assertTrue(set(r["need"] for r in read_table("dependencies.json"))
                        <= {r["sku"] for r in read_table("catalog.json")})
