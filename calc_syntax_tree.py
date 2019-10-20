#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
# This script is used to
# Version : 1.0.0.1
# usage :
#
#
###############################################################

from stack import Stack
from common_info import StackIsNotBalance


def _syntax_tree_to_stack(node, token_stack):
    """
    right order traverse to create stack, example : "(2+3)*2" stack is [*, 2, + , 3, 2]
    token stack only contain number and operator
    :param node:
    :param token_stack:
    :return: list
    """
    token_stack.push(node.token)
    if node.right:
        _syntax_tree_to_stack(node.right, token_stack)
    if node.left:
        _syntax_tree_to_stack(node.left, token_stack)


def _calc_stack(token_stack):
    """

    :param token_stack:
    :return:
    """
    stack = Stack()

    while not token_stack.is_empty():
        token = token_stack.pop()
        if token.is_number():
            stack.push(int(token.value))
            continue

        if token.is_operator():
            # 1. get two number from stack, right number is first
            # 2. calc, then push result into stack
            right = stack.pop()
            left = stack.pop()
            operator = token.value

            if operator == '+':
                ret = left + right
            elif operator == '-':
                ret = left - right
            elif operator == '*':
                ret = left * right
            elif operator == '/':
                ret = left / right
            else:
                raise SyntaxError("unsupported operator : %s" % operator)

            stack.push(ret)
            continue

        raise SyntaxError("invalid token %s" % str(token))

    ret = stack.pop()
    if not stack.is_empty():
        raise StackIsNotBalance(str(stack))

    return ret


def calc_syntax_tree(syntax_tree):
    token_stack = Stack()
    _syntax_tree_to_stack(syntax_tree, token_stack)
    return _calc_stack(token_stack)
