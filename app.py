from lexico import extraerTokens
from parsear import Parser

entrada=open('prueba2.txt','r').read()

tokens=extraerTokens(entrada)

print('_'*50)
for i in tokens:
    print(i)

print('_'*50)   
parser=Parser(tokens)
parser.parse()