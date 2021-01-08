from bvc import BVC
from robust_testing import RobustTesting
from worst_test_case import WorstTestCase

if __name__ == '__main__':
    n = int(input("Enter number of parameter: "))
    bvc = BVC(n)
    bvc.get_csv()
    rbc = RobustTesting(n)
    rbc.get_csv()
    wrc = WorstTestCase(n)
    wrc.get_csv()