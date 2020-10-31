# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:54:43 2020

@author: aespi
"""
from Components.BaseComponent import BaseComponent


class clock(BaseComponent):
    """
        Description:
        This is the clock class of the digital component.
        The class receives a binary value and flips it depending
        on the function call.
    """
    def __init__(self, name, input):
        """
            Description
            :parameter (input) : value that will be flipped.
        """
        super().__init__(name)
        # self.Output()
        self.result = input
        self.checked = False
        self.checkInputErrors(input)

    def Output(self,input):
        self.result = int(not (self.result))
        return self.result

