# File: test_lru_cache.py


import unittest
from app.SystemDesign.lru_cache_146 import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_example(self):
        cache = LRUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)

        cache.put(3, 3)  # evict 2
        self.assertEqual(cache.get(2), -1)

        cache.put(4, 4)  # evict 1
        self.assertEqual(cache.get(1), -1)

        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)


if __name__ == "__main__":
    unittest.main()

