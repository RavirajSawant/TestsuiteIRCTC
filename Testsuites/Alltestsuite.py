import unittest
from package1.TC_login import loginTest
from package2.TC_flightsearch import Test_irctc

# get all the tests from logintest and flightsearch
tc1 = unittest.TestLoader().loadTestsFromTestCase(loginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Test_irctc)

#creating testsuite
ts = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(ts)