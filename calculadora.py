def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):    
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b


def formatar_numero(valor):
    if isinstance(valor, float) and valor.is_integer():
        return int(valor)
    return valor


def obter_numero(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            valor = float(entrada)
            return int(valor) if valor.is_integer() else valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")


def exibir_menu_inicial():
    print("==========================================")
    print(" CALCULADORA EM PYTHON")
    print("==========================================")
    print(" 1 - Adição")
    print(" 2 - Subtração")
    print(" 3 - Multiplicação")
    print(" 4 - Divisão")
    print(" 0 - Sair")
    print()


def main():
    primeira_execucao = True

    while True:
        # Apresentação do menu (completo na primeira vez, resumido nas repetições)
        if primeira_execucao:
            exibir_menu_inicial()
            primeira_execucao = False
        else:
            print("\n---------- MENU PRINCIPAL ----------")

        opcao = input("Escolha uma opção: ").strip()

        # Opção de encerramento
        if opcao == "0":
            print("Programa encerrado.")
            break

        # Validação da opção
        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida! Escolha uma opção de 0 a 4.")
            continue

        # Entrada dos números
        num1 = obter_numero("Primeiro número: ")
        num2 = obter_numero("Segundo número: ")

        # Processamento das quatro operações matemáticas
        if opcao == "1":
            operador = "+"
            resultado = somar(num1, num2)
            print()
            print(f"Resultado: {formatar_numero(num1)} {operador} {formatar_numero(num2)} = {formatar_numero(resultado)}")

        elif opcao == "2":
            operador = "-"
            resultado = subtrair(num1, num2)
            print()
            print(f"Resultado: {formatar_numero(num1)} {operador} {formatar_numero(num2)} = {formatar_numero(resultado)}")

        elif opcao == "3":
            operador = "*"
            resultado = multiplicar(num1, num2)
            print()
            print(f"Resultado: {formatar_numero(num1)} {operador} {formatar_numero(num2)} = {formatar_numero(resultado)}")

        elif opcao == "4":
            operador = "/"
            if num2 == 0:
                print()
                print("Erro: divisão por zero não é permitida.")
            else:
                resultado = dividir(num1, num2)
                print()
                print(f"Resultado: {formatar_numero(num1)} {operador} {formatar_numero(num2)} = {formatar_numero(resultado)}")

        # Verificação se o usuário deseja realizar um novo cálculo
        resposta = input("\nOutro cálculo? (s/n): ").strip().lower()
        if resposta != "s":
            print("Programa encerrado.")
            break


if __name__ == "__main__":
    main()

