#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
# This script is used to
# Version : 1.0.0.1
# usage :
#
#
###############################################################


import common_info
from calc_token import Token


def _parse_keyword(char):
    """
    if char is a keyword, return a dict with it type and value
    :param char:
    :return: {type : xx, value : %char%}
    """
    keywords = common_info.keywords
    keyword_type_info = common_info.keyword_type_info

    if char in keywords:
        keyword_type = keyword_type_info[char]
        return Token(keyword_type, char)


def parse_expression(expression):
    """
    extract token from expression : numbers, operators, ();
    if there is unknown token in expression, thrown an exception UnknownToken
    :param expression:
    :return: list, token info list, from left to right in expression, example : [{"type": "operator", "value": "+"}]
    """
    char_list = list(expression)
    # append a space at the end of %char_list%, to fetch the last number in expression
    char_list.append(" ")
    tokens = []
    number_list = []

    while True:
        if not char_list:
            break

        char = char_list.pop(0)

        # check number
        if char.isdigit():
            number_list.append(char)
            continue

        # if char is not a number, fetch last number
        if number_list:
            token = "".join(number_list)
            tokens.append(Token(common_info.TYPE_NUM, token))
            number_list = []

        # check space and tab
        if char == ' ' or char == ' ':
            continue

        # check keyword
        token = _parse_keyword(char)
        if token:
            tokens.append(token)
            continue

        # others, throw error
        raise SyntaxError("%s is a invalid token" % char)

    return tokens
