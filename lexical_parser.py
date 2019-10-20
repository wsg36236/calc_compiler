#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
# This script is used to parse lexical with state machine
# Version : 1.0.0.1
# usage :
#
#
###############################################################


import common_info
from calc_token import Token
from stack import Stack


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
    :return: list, Token list, from left to right in expression
    """
    # reverse char list for stack, so it pop char from the begin of expression
    char_list = list(expression)
    # append a space at the end of %char_list%, to fetch the last number in expression
    tokens = []
    buff = ""
    i = 0

    while i < len(char_list):
        char = char_list[i]
        i += 1

        # check number
        # if char is a digit, continue to fetch char until char is not a digit or char_list is parsed completely
        if char.isdigit():
            buff += char
            while i < len(char_list):
                char = char_list[i]
                i += 1

                if char.isdigit():
                    buff += char
                else:
                    # rollback
                    i -= 1
                    break
            tokens.append(Token(common_info.TYPE_NUM, buff))
            buff = ""
            continue

        # if char is not a number, fetch last number
        if buff:
            token = "".join(buff)
            tokens.append(Token(common_info.TYPE_NUM, token))
            buff = []

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
