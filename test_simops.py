import unittest
import simops.simops as so

class TestSimOps(unittest.TestCase):
    """Unit test for SimOps module"""

    def test_add(self):
        num_1 = so.SimOps(10, 5)
        num_2 = so.SimOps(-1, 1)
        num_3 = so.SimOps(-1, -1)

        self.assertEqual(num_1.add, 15)
        self.assertEqual(num_2.add, 0)
        self.assertEqual(num_3.add, -2)

    def test_subtract(self):
        num_1 = so.SimOps(10, 5)
        num_2 = so.SimOps(-1, 1)
        num_3 = so.SimOps(-1, -1)

        self.assertEqual(num_1.subtract, 5)
        self.assertEqual(num_2.subtract, -2)
        self.assertEqual(num_3.subtract, 0)

    def test_multiply(self):
        num_1 = so.SimOps(10, 5)
        num_2 = so.SimOps(-1, 1)
        num_3 = so.SimOps(-1, -1)

        self.assertEqual(num_1.multiply, 50)
        self.assertEqual(num_2.multiply, -1)
        self.assertEqual(num_3.multiply, 1)

    def test_divide(self):
        num_1 = so.SimOps(10, 5)
        num_2 = so.SimOps(-1, 1)
        num_3 = so.SimOps(-1, -1)
        num_4 = so.SimOps(5, 0)

        self.assertEqual(num_1.divide, 2)
        self.assertEqual(num_2.divide, -1)
        self.assertEqual(num_3.divide, 1)
        
        with self.assertRaises(ValueError):
            num_4.divide()

if __name__ == '__main__':
    unittest.main()