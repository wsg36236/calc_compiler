#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
#
# This script is used to
# Version : 1.0.0.1
# usage :
#
#
###############################################################

import argparse
import sys
from logging import basicConfig, DEBUG

from calc_syntax_tree import calc_syntax_tree
from lexical_parser import parse_expression
from syntax_parser import parse_token


def calc_expression(expression):
    tokens = parse_expression(expression)
    syntax_tree = parse_token(tokens)
    ret = calc_syntax_tree(syntax_tree)
    return ret


def parse_args():
    """parse args"""

    cmd_parser = argparse.ArgumentParser()
    cmd_parser.add_argument("-e", "--expression", help="calc expression, example : (2 + 3) * 2", default=None)
    if len(sys.argv) == 1:
        cmd_parser.print_help()
        print("")
    return cmd_parser.parse_args()


def main():
    basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=DEBUG)
    args = parse_args()
    expression = args.expression
    if expression is None:
        expression = raw_input("please input calc expression : ")

    try:
        ret = calc_expression(expression)
        print("%s = %d" % (expression, ret))
    except Exception, e:
        print("calc error : " + str(e))


############################# main ##################################
if __name__ == '__main__':
    main()
