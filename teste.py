linha = '\033[1;96m=\033[m' * 75
texto = "APARELHOS"
fat1 = texto[0:3]
fat2 = texto[3:6]
fat3 = texto[6:]
print(linha)
print(f'''\nFatiando a palavra {texto}, temos '{fat1}', '{fat2}' e '{fat3}.'

Pegando a primeira caractere de cada fatiamento, temos '{fat1[0]}', '{fat2[0]}' e '{fat3[0]}'.''')
print(f'\n{linha}')
