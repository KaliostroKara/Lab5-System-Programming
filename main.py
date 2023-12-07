from lexer import lexer
from expr_parser import parser
from visualize import render_ast

# Тестовий арифметичний вираз
expression = "1 + 9 * (9 - 1) ^ 5 / 10 "

# Лексичний аналіз
lexer.input(expression)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# Синтаксичний аналіз і побудова AST
ast = parser.parse(expression)

# Виведення результатів
print("Обчислене значення:", ast.eval())
print("Згенерований код:", ast.generate_code())

# Візуалізація AST
render_ast(ast, 'ast')
