import re

text = 'pincher12'
default = re.compile('p.n.')
# busque todos que contenham esse padrão
check = default.findall(text)
print(check)

# retorne tudo menos o caracter i
different_a = re.compile('[^i]')
check2 = different_a.findall(text)
print(check2)

#busque o caracter que começa com p e retorne seu valor
starts_p = re.compile('^p')
check3 = starts_p.findall(text)
print(check3)

#usar o "r" é importante para indicar que é a sintaxe do regex, e não de algo como uma quebra de linha \n

# \d retorna qualquer algarismo de 0 a 9
numbers = re.compile(r'\d')
check4 = numbers.findall(text)
print(check4)

#  \D retorna qualquer caracter que não seja um algarismo de 0 a 9
different_num = re.compile(r'\D')
check5 = different_num.findall(text)
print(check5)

tex2 = '''

pincher 12 @pi12

'''
# \s busca todos os caracteres que sejam vazios
empty = re.compile(r'\s')
check5 = empty.findall(tex2)
print(check5)

# \S busca tods que não sejam varios
different_empty = re.compile(r'\S')
check6 = different_empty.findall(tex2)
print(check6)

# \w busca todos que são alfanúmericos
# \W busca todos que não são alfanúmericos
alphanumeric = re.compile(r'\w')
check7 = alphanumeric.findall(tex2)
print(check2)

# match método de checagem que retorna a posição do item e se deu match
check_match =  different_empty.match(tex2)
print(check_match)

# fingiter método de checagem que permite ser utilizado na estrutura for para retornar o match de cada item
num = numbers.finditer(text)
for n in num:
    print(n)


character_set = re.compile(r'[a-zA-Z0-9]')
check8 = character_set.findall(tex2)
print(check8)

# define o padrão de 3 caracteres, o primeiro de a-z, segundo espaço e terceiro 0-9
p = re.compile(r'[a-zA-Z] [0-9]')

# + aparece uma ou mais vezes
p = re.compile(r'[a-zA-Z]+')

# * aparece 0 ou mais vezes
p = re.compile(r'[a-zA-Z]*')

# ? aparece 0 ou um
