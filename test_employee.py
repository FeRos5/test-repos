import unittest
import simops.employee as ep

class TestEmplyee(unittest.TestCase):
    """Unit test for Employee module"""

    def test_email(self):
        emp_1 = ep.Employee('Korakot', 'Pariwatthanasak', 50000)
        emp_2 = ep.Employee('Phachinee', 'Sara', 60000)

        self.assertEqual(emp_1.email, 'korakot.pariwatthanasak@email.com')
        self.assertEqual(emp_2.email, 'phachinee.sara@email.com')

        emp_1.first = 'Kittitat'
        emp_2.first = 'Panutat'

        self.assertEqual(emp_1.email, 'kittitat.pariwatthanasak@email.com')
        self.assertEqual(emp_2.email, 'panutat.sara@email.com')

    def test_fullname(self):
        emp_1 = ep.Employee('Korakot', 'Pariwatthanasak', 50000)
        emp_2 = ep.Employee('Phachinee', 'Sara', 60000)

        self.assertEqual(emp_1.fullname, 'Korakot Pariwatthanasak')
        self.assertEqual(emp_2.fullname, 'Phachinee Sara')

        emp_1.first = 'Kittitat'
        emp_2.first = 'Panutat'

        self.assertEqual(emp_1.fullname, 'Kittitat Pariwatthanasak')
        self.assertEqual(emp_2.fullname, 'Panutat Sara')

    def test_apply_raise(self):
        emp_1 = ep.Employee('Korakot', 'Pariwatthanasak', 50000)
        emp_2 = ep.Employee('Phachinee', 'Sara', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()