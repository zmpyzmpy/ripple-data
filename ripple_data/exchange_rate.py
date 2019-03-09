# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:05:24 2018

@author: hjanssen
"""
import sys

from ripple_data import RippleAPI

class RippleExchangeRate(RippleAPI):
    """
    """

    EXCHANGES_URL = '/v2/exchange_rates/{base}/{counter}'

    def __init__(self, base, counter):
        self.base = base
        self.counter = counter

    def __str__(self):
        return self.EXCHANGES_URL.format(**self.__dict__)

    def exchange_rates(self):
        """
        Retrieve current Exchange rate for a given currency pair.
        """

        method = sys._getframe().f_code.co_name
        result = RippleAPI.get_ripple_data(str(self), locals())

        return result['rate']
