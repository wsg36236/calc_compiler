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
from calc_token import tokens_to_str


class TestLexicalParser(unittest.TestCase):
    def test_basic_lexical_parse(self):
        expression_token_map = {
            "3 * 21 - 1 + 4 / 2": "3*21-1+4/2",
            " ( 2 + 3)* 20   ": "(2+3)*20"
        }

        for expression, token_str in expression_token_map.items():
            tokens = parse_expression(expression)
            self.assertEquals(token_str, tokens_to_str(tokens))

    def test_error_expression(self):
        expressions = [
            "2^3",
            "0x1A + 3",
        ]

        for expression in expressions:
            self.assertRaises(SyntaxError, parse_expression, expression)


############################# main ##################################
if __name__ == '__main__':
    unittest.main()
