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

from calc_compiler import calc_expression


class TestCalcCompiler(unittest.TestCase):
    def expression_test(self, expressions):
        for expression in expressions:
            compiler_ret = calc_expression(expression)
            python_ret = eval(expression)
            print("%s = %d" % (expression, compiler_ret))
            self.assertEqual(compiler_ret, python_ret)

    def test_basic_expression(self):
        expressions = [
            "2 + 3",
            "2 + 3 + 4",
            "3 - 2",
            "2 * 3",
            "4 / 2",
            "2 * 3 / 2"
        ]

        self.expression_test(expressions)

    def test_expression_with_priority(self):
        expressions = [
            "2 + 3 * 2",
            "2 + 4 / 2",
            "2 * 3 -2",
            "2- 4 / 2",
            "3 * 2 + 2",
            "4 / 2 + 2",
            "2 + 3 * 2 - 1 + 4 / 2"
        ]

        self.expression_test(expressions)

    def test_expression_with_parentheses(self):
        expressions = [
            "(2 + 3 * 2) / 2",
            "((2 + 3 * 2) - 3) / 5 + 2",
            "3 * (3 + 2) /5 + (2 + 3 * 2) /2",
            "1 + ((3 + 3) / 2 + 1) * (5 - 2)"
        ]

        self.expression_test(expressions)

    def test_expression_with_multiple_space_and_tab(self):
        expressions = [
            "2 +  3",
            "3  - 1",
            " 2 *3",
            "4/2  ",
            "   2 +     3",
            "               3+      2    ",
            "   ( 2 + 3 *2)/2",
            "(2 + 3 *2      )   /2",
        ]

        self.expression_test(expressions)

    def test_syntax_error_expression(self):
        expressions = [
            "(2 + 3 * 2 / 2",
            "*2 + 3",
            "2 * + 3",
            "2 2 + 3",
            "2  2+3",
            "2 + )3 + 2 ( + ",
            "(2 + 3 * 2) - 3) / 5 + 2",
            ""
        ]

        for expression in expressions:
            self.assertRaises(SyntaxError, calc_expression, expression)


############################# main ##################################
if __name__ == '__main__':
    unittest.main()
