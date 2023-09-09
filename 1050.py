codigos = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

ddd = int(input())

local = ""

for codigo in codigos:
    if ddd == codigo:
        local += codigos[ddd]
    
if local == "":
    local += "DDD nao cadastrado"

print(local)