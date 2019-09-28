import unittest
import simops.simops as so

class TestSimOps(unittest.TestCase):
    """Unit test for SimOps module"""

    def test_add(self):
        self.assertEqual(so.SimOps(10, 5).add(), 15)
        self.assertEqual(so.SimOps(-1, 1).add(), 0)
        self.assertEqual(so.SimOps(-1, -1).add(), -2)

    def test_subtract(self):
        self.assertEqual(so.SimOps(10, 5).subtract(), 5)
        self.assertEqual(so.SimOps(-1, 1).subtract(), -2)
        self.assertEqual(so.SimOps(-1, -1).subtract(), 0)

    def test_multiply(self):
        self.assertEqual(so.SimOps(10, 5).multiply(), 50)
        self.assertEqual(so.SimOps(-1, 1).multiply(), -1)
        self.assertEqual(so.SimOps(-1, -1).multiply(), 1)

    def test_divide(self):
        self.assertEqual(so.SimOps(10, 5).divide(), 2)
        self.assertEqual(so.SimOps(-1, 1).divide(), -1)
        self.assertEqual(so.SimOps(-1, -1).divide(), 1)
        
        with self.assertRaises(ValueError):
            so.SimOps(10, 0).divide()

if __name__ == '__main__':
    unittest.main()