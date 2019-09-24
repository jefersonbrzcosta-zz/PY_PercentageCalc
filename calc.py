ask = int(input("Olá, seja bem vindo a calculadora de porcentagem.\n\nClique na opção desejada:\nDigite 1 e enter se quer sua resposta em porcentagem (%)\nDigite 2 e enter se quer sua resposta em valor\n"))

if ask == 1:
    valorTotal = float(input("Digite o valor total que deseja calcular\n"))
    porcentagem = float(input("Digite a porcentagem do valor total que deseja saber\n"))
    resultado = round(((porcentagem * valorTotal) / 100), 2)

    print(str(porcentagem) + "% de " + str(valorTotal) + " é: " + str(resultado)) 


if ask == 2:
    valorTotal = float(input("Digite o valor total que deseja calcular\n"))
    valor = float(input("Digite o valor que deseja saber a porcentagem\n"))
    resultado = round(((valor * 100) / valorTotal), 2)

    print(str(valor) + " se refere a " + str(resultado) + "% de " + str(valorTotal)) 
