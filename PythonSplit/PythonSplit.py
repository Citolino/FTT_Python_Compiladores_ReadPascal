import re
import asyncio

async def pegarPalavrasReservadas(textcode):
    allwords = re.findall(r"[\w']+", pascal_code)
    r = re.compile('|'.join([r'\b%s\b' % w for w in allwords]), flags=re.I)
    reservados = r.findall(pascal_keys)
    return reservados

async def pegarTipoDeVariavel(textcode,varType):
    splitedcode = textcode.split()
    vars = []

    inicioVar = splitedcode.index("var")
    fimVar = splitedcode.index("begin")

    subSplitedCode = splitedcode[inicioVar + 1:fimVar]
    for idx, val in enumerate(subSplitedCode):
        if val == varType + ";":
            vars.append(subSplitedCode[idx - 2])
    
    return vars

async def pegarFloats(textcode):
    return await pegarTipoDeVariavel(textcode,"real")

async def pegarInts(textcode):
    return await pegarTipoDeVariavel(textcode,"integer")


pascal_keys=""
pascal_code=""

with open("pascal-keys.txt","r") as pkeys:
    pascal_keys = pkeys.read()

with open("p1.pas","r") as pkeys:
    pascal_code = pkeys.read().lower()



loop = asyncio.get_event_loop()

reservados = asyncio.gather(pegarPalavrasReservadas(pascal_code))
floats = asyncio.gather(pegarFloats(pascal_code))
ints = asyncio.gather(pegarInts(pascal_code))

all_groups = asyncio.gather(reservados, floats, ints)
results = loop.run_until_complete(all_groups)


print("reservadas: ",reservados._result[0])
print("floats: ",floats._result[0])
print("ints: ",ints._result[0])




# 1. ler arquivo
# 2. quebrar em tokens
# 3. usar regexp para verificar o tipo de token

# palavras reservadas - keywords
# float
# int
# variáveis -> regexp
# operações (+, -, *, ^, =, :=)

# Lex - Parser >>> WEB Scraping
