#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
# This script is used to parse tokens from lexical_parse.py, and return a syntax binary tree
# Version : 1.0.0.1
# usage :
#
#
###############################################################

from binary_tree import Node
from common_info import TYPE_NUM, TYPE_OPERATOR, TYPE_SCOPE, TYPE_EXPRESSION, MAX_PRIORITY, operator_priority_info
from calc_token import Token


def _split_sub_expression(tokens):
    """
    split sub expression with "()", example : "(2 + 3) * 2" split as "2+3" * 2;
    box sub expression with "()" as a expression token;
    if there is "()" in "()", only box the outermost "()"
    :param tokens:
    :return:
    """
    token_without_parentheses = []
    sub_expression_tokens = []
    left_parentheses_count = 0
    for token in tokens:
        token_type = token.type
        if token_type != TYPE_SCOPE and left_parentheses_count == 0:
            token_without_parentheses.append(token)
            continue

        token_value = token.value
        if token_value == '(':
            left_parentheses_count += 1
            # if find first '(', do not append it into sub_expression_tokens
            if left_parentheses_count == 1:
                continue
        elif token_value == ')':
            left_parentheses_count -= 1
            if left_parentheses_count == 0:
                # create sub expression token
                token_without_parentheses.append(Token(TYPE_EXPRESSION, sub_expression_tokens))
                sub_expression_tokens = []
                continue
            elif left_parentheses_count < 0:
                raise SyntaxError("parentheses is not balance")
        sub_expression_tokens.append(token)

    if left_parentheses_count != 0:
        raise SyntaxError("parentheses is not balance")

    return token_without_parentheses


def _find_lowest_priority_operator(tokens):
    """
    find lowest priority operator, because calc from left to right, if 2 operate has same priority,
    the right one is lower than the left one
    :param tokens: token list without parentheses, because scope token has higher priority
    :return: int, lowest_priority_operator_index, if not find, return -1
    """
    lowest_priority_operator_index = -1
    lowest_priority_operator_priority = MAX_PRIORITY + 1
    for i, token in enumerate(tokens):
        token_type = token.type
        if token_type != TYPE_OPERATOR:
            continue

        token_value = token.value
        priority = operator_priority_info[token_value]
        if priority <= lowest_priority_operator_priority:
            lowest_priority_operator_priority = priority
            lowest_priority_operator_index = i

    return lowest_priority_operator_index


def parse_token(tokens):
    """
    parse tokens from lexical_parse.py;
    1. trait tokens in "()" as a expression token;
    2. find the lowest operator;
    3. binary split tokens with lowest operator;
    4. process left tokens and right tokens
    :param tokens: token list, the toke could be number, operator, scope and expression
    :return: syntax binary tree
    """
    token_size = len(tokens)
    if token_size == 0:
        raise SyntaxError("empty token")
    elif token_size == 1:
        token = tokens[0]
        token_type = token.type
        token_value = token.value
        if token_type == TYPE_OPERATOR:
            raise SyntaxError("expression should be number or sub expression, but %s is an operator" % token_value)
        elif token_type == TYPE_SCOPE:
            raise SyntaxError("expression should be number or sub expression, but %s is a parentheses" % token_value)
        elif token_type == TYPE_NUM:
            return Node(token)
        else:
            # expression need to binary split
            tokens = token_value

    # token is a expression, split it with operator
    # split tokens with ()
    token_without_parentheses = _split_sub_expression(tokens)

    # find lowest operator
    lowest_priority_operator_index = _find_lowest_priority_operator(token_without_parentheses)
    if lowest_priority_operator_index == -1:
        raise SyntaxError("can not find operator")

    # split
    left_sub_tokens = token_without_parentheses[:lowest_priority_operator_index]
    right_sub_tokens = token_without_parentheses[lowest_priority_operator_index + 1:]
    node = Node(token_without_parentheses[lowest_priority_operator_index])
    node.left = parse_token(left_sub_tokens)
    node.right = parse_token(right_sub_tokens)
    return node
