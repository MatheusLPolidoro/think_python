# 1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
try:
    eval('print("olá, mundo."')
except SyntaxError as ex:
    # Gera um SyntaxError: '(' was never closed
    print(ex)

# 2. Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
try:
    eval('print("oi)')
except SyntaxError as ex:
    # Gera um SyntaxError: unterminated string literal
    print(ex)

# 3. Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? e se escrever assim? 2++2?
print(-2) # Funciona
print(2++2) # Funciona

# 4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no python?
try:
    eval('print(02)')
except SyntaxError as ex:
    # Gera um SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
    print(ex)

# 5. O que acontece se você tiver dois valores sem nenhum operador entre eles?
try:
    eval('print(2 3)')
except SyntaxError as ex:
    # Gera um syntaxError: invalid syntax. Perhaps you forgot a comma?
    print(ex)
