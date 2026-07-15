import unittest

from finance_calculator import compound_amount, loan_emi, simple_interest


class FinanceCalculatorTests(unittest.TestCase):
    def test_simple_interest(self):
        self.assertAlmostEqual(simple_interest(1000, 10, 2), 200)

    def test_compound_amount(self):
        self.assertAlmostEqual(compound_amount(1000, 10, 1, 2), 1210)

    def test_loan_emi_with_interest(self):
        self.assertAlmostEqual(loan_emi(100000, 12, 12), 8884.88, places=2)

    def test_loan_emi_with_zero_interest(self):
        self.assertAlmostEqual(loan_emi(1200, 0, 12), 100)

    def test_invalid_negative_inputs(self):
        with self.assertRaises(ValueError):
            simple_interest(-1, 10, 2)


if __name__ == "__main__":
    unittest.main()
