#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
# This script is used to define data which use by other py
# Version : 1.0.0.1
# usage :
#
#
###############################################################

TYPE_NUM = "number"
TYPE_OPERATOR = "operator"
TYPE_SCOPE = "scope"
TYPE_EXPRESSION = "expression"

keyword_type_info = {
    '+': TYPE_OPERATOR,
    '-': TYPE_OPERATOR,
    '*': TYPE_OPERATOR,
    '/': TYPE_OPERATOR,
    '(': TYPE_SCOPE,
    ')': TYPE_SCOPE
}

keywords = keyword_type_info.keys()

MAX_PRIORITY = 9
BASE_PRIORITY = 0
operator_priority_info = {
    '+': BASE_PRIORITY + 1,
    '-': BASE_PRIORITY + 1,
    '*': BASE_PRIORITY + 2,
    '/': BASE_PRIORITY + 2
}


# exceptions
class NodeIsNotToken(Exception):
    def __init__(self, arg):
        self.args = arg


class StackIsNotBalance(Exception):
    def __init__(self, arg):
        self.args = arg
