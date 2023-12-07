import ply.yacc as yacc
from lexer import tokens  # Імпорт токенів із лексера

# Імпортуємо класи для AST з файлу ast_nodes.py
from ast_nodes import NumNode, BinOpNode

# Правила граматики та побудова AST

def p_express_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression'''
    p[0] = BinOpNode(p[2], p[1], p[3])

def p_express_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_express_number(p):
    'expression : NUMBER'
    p[0] = NumNode(p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Створення парсера

parser = yacc.yacc()
