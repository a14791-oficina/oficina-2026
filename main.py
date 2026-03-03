while True:

    menu = '''
+-----------------------------------------------------------+
|             Menu - ESCOLHA UMA OPÇÃO B1 a A5              |
+-----------------------------------------------------------+                                       |
| B1 - Número Positivo ou Negativo                          |
| B2 - Maior de Idade                                       |
| B3 - Número Par ou Ímpar                                  |
| B4 - Comparação de Dois Números                           |
| B5 - Password Simples                                     |                                          |
| I1 - Classificação de Nota                                |
| I2 - Classificação de Idade                               |
| I3 - Múltiplo de 3 e 5                                    |
| I4 - Login com Utilizador e Password                      |
| I5 - Número dentro de intervalo                           |                                     |
| A1 - Sistema Multibanco Simples                           |
| A2 - Maior de Quatro Números                              |
| A3 - Classificação de IMC                                 |
| A4 - Sistema de Desconto                                  |
| A5 - Verificação de Ano Bissexto                          |
|                                                           |
| 0 - Sair                                                  |
+-----------------------------------------------------------+
'''

    print(menu)

    opcao = input("Escolha uma opção: ").upper()

    
    if opcao == "B1":
        num = int(input("Insira um número: "))
        if num >= 0:
            print("O número é positivo!")
        else:
            print("O número é negativo!")

    elif opcao == "B2":
        idade = int(input("Qual é a tua idade: "))
        if idade >= 18:
            print("Maior de idade!")
        else:
            print("Menor de idade!")

    elif opcao == "B3":
        num = int(input("Insira um número: "))
        if num % 2 == 0:
            print("Número Par")
        else:
            print("Número Ímpar")

    elif opcao == "B4":
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        if n1 > n2:
            print(f"O maior número é {n1}")
        elif n2 > n1:
            print(f"O maior número é {n2}")
        else:
            print("Os números são iguais")

    elif opcao == "B5":
        senha = input("Insira a password: ")
        if senha == "Python":
            print("Password correta")
        else:
            print("Password incorreta")

    elif opcao == "I1":
        nota = int(input("Insira a sua nota: "))
        if nota < 10:
            print("Reprovado")
        elif nota <= 13:
            print("Suficiente")
        elif nota <= 17:
            print("Bom")
        elif nota <= 20:
            print("Excelente")

    elif opcao == "I2":
        idade = int(input("Insira a sua idade: "))
        if idade < 13:
            print("Ainda és uma criança")
        elif idade <= 17:
            print("És jovem")
        elif idade <= 64:
            print("És adulto")
        else:
            print("És sénior")

    elif opcao == "I3":
        numero = int(input("Digite um número: "))
        if numero % 3 == 0 and numero % 5 == 0:
            print("Múltiplo de 3 e 5")
        elif numero % 3 == 0:
            print("Múltiplo de 3")
        elif numero % 5 == 0:
            print("Múltiplo de 5")
        else:
            print("Não é múltiplo de 3 nem de 5")

    elif opcao == "I4":
        user = input("Username: ")
        password = int(input("Password: "))
        if user == "admin" and password == 1234:
            print("Login correto!")
        else:
            print("Tente novamente!")

    elif opcao == "I5":
        numero = int(input("Digite um número: "))
        if 10 <= numero <= 20:
            print("O número pertence ao intervalo")
        else:
            print("Não pertence ao intervalo")

    
    elif opcao == "A1":
        saldo = 1000
        levantar = float(input("Quanto quer levantar: "))
        if levantar <= saldo:
            print(f"Levantou {levantar} euros!")
        else:
            print("Saldo insuficiente!")

    elif opcao == "A2":
        numeros = []
        for i in range(4):
            numeros.append(int(input("Digite um número: ")))
        print(f"O maior número é {max(numeros)}")

    elif opcao == "A3":
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        imc = peso / (altura ** 2)

        if imc < 18.5:
            print("Baixo peso")
        elif imc <= 24.9:
            print("Normal")
        elif imc <= 29.9:
            print("Excesso de peso")
        else:
            print("Obesidade")

    elif opcao == "A4":
        valor = float(input("Valor da compra: "))
        if valor >= 100:
            desconto = valor * 0.1
        elif valor >= 50:
            desconto = valor * 0.05
        else:
            desconto = 0

        print(f"Desconto: {desconto}")
        print(f"Valor final: {valor - desconto}")

    elif opcao == "A5":
        ano = int(input("Digite um ano: "))
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print("Ano bissexto")
        else:
            print("Ano normal")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")