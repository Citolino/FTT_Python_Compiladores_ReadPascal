import re


def pegarPalavrasReservadas(textcode):
    allwords = re.findall(r"[\w']+", pascal_code)
    r = re.compile('|'.join([r'\b%s\b' % w for w in allwords]), flags=re.I)
    reservados = r.findall(pascal_keys)
    return reservados

def pegarTipoDeVariavel(textcode,varType):
    splitedcode = textcode.split()
    vars = []

    inicioVar = splitedcode.index("var")
    fimVar = splitedcode.index("begin")

    subSplitedCode = splitedcode[inicioVar + 1:fimVar]
    for idx, val in enumerate(subSplitedCode):
        if val == varType + ";":
            vars.append(subSplitedCode[idx - 2])
    
    return vars

def pegarFloats(textcode):
    return pegarTipoDeVariavel(textcode,"real")

def pegarInts(textcode):
    return pegarTipoDeVariavel(textcode,"integer")


pascal_keys=""
pascal_code=""

with open("pascal-keys.txt","r") as pkeys:
    pascal_keys = pkeys.read()

with open("p1.pas","r") as pkeys:
    pascal_code = pkeys.read().lower()

reservados = pegarPalavrasReservadas(pascal_code)
floats = pegarFloats(pascal_code)
ints = pegarInts(pascal_code)

print("reservadas: ",reservados)
print("floats: ",floats)
print("ints: ",ints)




# 1. ler arquivo
# 2. quebrar em tokens
# 3. usar regexp para verificar o tipo de token

# palavras reservadas - keywords
# float
# int
# variáveis -> regexp
# operações (+, -, *, ^, =, :=)

# Lex - Parser >>> WEB Scraping
