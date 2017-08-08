#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bs4
import  requests
import csv
import os


class ErrorSet:
    def __init__(self,error_set):
        self.error_set=error_set

    def __eq__(self, other):
        return self.error_set==other.error_set
    def __hash__(self):
        return hash(tuple(self.error_set))

if __name__=="__main__":
    a=ErrorSet(set([1,2,3,4,5,6]))
    b=ErrorSet(set([2,1,3,4,5,6]))
    c=ErrorSet(set([3,2,1,5,6,4]))
    print a.__hash__()
    print b.__hash__()
    print c.__hash__()
    output={}
    output.setdefault(a,0)
    print b in output.keys()


