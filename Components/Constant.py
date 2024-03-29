#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:38:35 2020

@author: osvaldo
"""
from Components.BaseComponent import BaseComponent


class const(BaseComponent):
    """
        Description:
        This is the constant component class of the digital system.
        This class will take a given input and return the same value.
        ValueErrors: A Constant Object must be instantiated with a binary value.
    """
    def __init__(self, name, output):
        """
            Description
            :parameter (output) : value that will remain constant.
        """
        super().__init__(name)
        self.checked = False
        self.checkInputErrors(output)
        self.result = output
