#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
# This script is used to
# Version : 1.0.0.1
# usage :
#
#
###############################################################

import unittest
from lexical_parser import parse_expression
from syntax_parser import parse_token


class TestSyntaxParser(unittest.TestCase):
    def test_basic_syntax(self):
        expression = "(2 + 3) * 2"
        tokens = parse_expression(expression)
        syntax_tree = parse_token(tokens)


############################# main ##################################
if __name__ == '__main__':
    unittest.main()
