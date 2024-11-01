print("LOJA DE ROUPA DO SENAC")
print("==========================")

Valor_Carteira = input("Quanto você tem? $: ")
CorFavorita = input("Qual a sua cor favorita? ")
CarrinhoCheio = False

print("===============================")

if int(Valor_Carteira) >= 30 and CorFavorita == "verde":
    if Valor_Carteira >= 32 and Valor_Carteira<38: 
        print("Saia")
    if Valor_Carteira >= 40:
        print("Chaveiro")
    CarrinhoCheio = True
if int(Valor_Carteira) >= 80 and CorFavorita == "Vermelho":
    print("Comprou roupa vermelha")
    CarrinhoCheio = True
if CarrinhoCheio == False:
    print("Estoque indispovel para TODAS as cores")