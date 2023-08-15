code_product1, units_product1, price_product1 = input().split(" ")
code_product2, units_product2, price_product2 = input().split(" ")

valor_final = (int(units_product1) * float(price_product1)) + (int(units_product2) * float(price_product2))
print(f'VALOR A PAGAR: R${valor_final: .2f}') 