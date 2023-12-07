import ply.lex as lex

# Список токенов
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'LPAREN',
    'RPAREN',
)

# Регулярні вирази для токенів
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POWER   = r'\^'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Числовий токен
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Правила ігнорування пробілів
t_ignore  = ' \t'

# Обробка помилок
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Створення лексера
lexer = lex.lex()
