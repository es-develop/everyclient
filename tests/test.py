# -*- coding: utf-8 -*-

from context import EveryClient

import unittest


class NewTestSet(unittest.TestCase):

    def test_not_none(self):
        res = EveryClient().get_perfectures(None)
        self.assertIsNotNone(res['code'])


if __name__ == '__main__':
    unittest.main()
