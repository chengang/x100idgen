import unittest
import re

import x100idgen


class TestSimple(unittest.TestCase):

    def setUp(self):
        self.x100idgen = x100idgen.IdGen()
        self.ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3"
        self.ip = "111.206.116.190"
        self.last_id = ""
        self.pattern = re.compile(r'^[0-9a-zA-Z]{18}$')

    def test_gen_id(self):
        _id = self.x100idgen.gen_id(self.ip + self.ua)
        self.last_id = _id
        self.assertEqual(len(_id), 18)
        self.assertRegex(_id, self.pattern)

    def test_gen_id_twice(self):
        _id = self.x100idgen.gen_id(self.ip + self.ua)
        self.assertEqual(len(_id), 18)
        self.assertRegex(_id, self.pattern)
        self.assertNotEqual(_id, self.last_id)

    def test_validate_id_true(self):
        self.assertTrue(self.x100idgen.validate_id("yt7NaHvuNOqSsc6PdM"))

    def test_validate_id_false(self):
        self.assertFalse(self.x100idgen.validate_id("yt7NaHvuNOqSsc6Pdm"))


if __name__ == '__main__':
    unittest.main()
