from unittest import TestCase

import fibo

class TestFibo(TestCase):
    def testFibo(self):
        rFib100 = fibo.fib2(100)
        self.assertEquals([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], rFib100)
