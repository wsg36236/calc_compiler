#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
# This script is used to define token class
# Version : 1.0.0.1
# usage :
#
#
###############################################################

from common_info import TYPE_EXPRESSION, TYPE_NUM, TYPE_OPERATOR, TYPE_SCOPE


def tokens_to_str(tokens):
    values = [token.value for token in tokens]
    return "".join(values)


class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        if self.type == TYPE_EXPRESSION:
            return tokens_to_str(self.value)
        else:
            return self.value

    def is_number(self):
        return self.type == TYPE_NUM

    def is_scope(self):
        return self.type == TYPE_SCOPE

    def is_operator(self):
        return self.type == TYPE_OPERATOR

    def is_expression(self):
        return self.type == TYPE_EXPRESSION
