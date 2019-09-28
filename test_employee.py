import unittest
import simops.employee as ep

class TestEmplyee(unittest.TestCase):
    """Unit test for Employee module"""

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = ep.Employee('Korakot', 'Pariwatthanasak', 50000)
        self.emp_2 = ep.Employee('Phachinee', 'Sara', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('Test Email')
        self.assertEqual(self.emp_1.email, 'korakot.pariwatthanasak@email.com')
        self.assertEqual(self.emp_2.email, 'phachinee.sara@email.com')

        self.emp_1.first = 'Kittitat'
        self.emp_2.first = 'Panutat'

        self.assertEqual(self.emp_1.email, 'kittitat.pariwatthanasak@email.com')
        self.assertEqual(self.emp_2.email, 'panutat.sara@email.com')

    def test_fullname(self):
        print('Test Fullname')
        self.assertEqual(self.emp_1.fullname, 'Korakot Pariwatthanasak')
        self.assertEqual(self.emp_2.fullname, 'Phachinee Sara')

        self.emp_1.first = 'Kittitat'
        self.emp_2.first = 'Panutat'

        self.assertEqual(self.emp_1.fullname, 'Kittitat Pariwatthanasak')
        self.assertEqual(self.emp_2.fullname, 'Panutat Sara')

    def test_apply_raise(self):
        print('Test Apply Raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()