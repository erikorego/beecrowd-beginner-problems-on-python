salario = float(input())

faixa_um = salario <= 2000
faixa_dois = (salario > 2000) and (salario <= 3000)
faixa_tres = (salario > 3000) and (salario <= 4500)
faixa_quatro = salario > 4500

if faixa_um:
    print("Isento")
elif faixa_dois:
    valor_taxado = salario - 2000
    taxa = valor_taxado * 0.08
    print(f"R$ {taxa:.2f}")
elif faixa_tres:
    valor_taxado = salario - 2000
    taxa_um = 1000 * 0.08
    taxa_dois = (valor_taxado - 1000) * 0.18
    taxa = taxa_um + taxa_dois
    print(f"R$ {taxa:.2f}")
elif faixa_quatro:
    valor_taxado = salario - 2000
    taxa_um  = 1000 * 0.08
    taxa_dois = 1500 * 0.18
    taxa_tres = (valor_taxado - 2500) * 0.28
    taxa = taxa_um + taxa_dois + taxa_tres
    print(f"R$ {taxa:.2f}")
