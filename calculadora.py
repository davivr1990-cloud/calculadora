def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def potencia(a: float, b: float) -> float:
    return a ** b


def resto(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível calcular o resto por zero.")
    return a % b


def ler_numero(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número válido.\n")


def mostrar_menu() -> None:
    print("\n" + "=" * 35)
    print("      CALCULADORA SIMPLES      ")
    print("=" * 35)
    print("Escolha uma operação:")
    print("  1 - Soma          (+)")
    print("  2 - Subtração     (-)")
    print("  3 - Multiplicação (*)")
    print("  4 - Divisão       (/)")
    print("  5 - Potência      (^)")
    print("  6 - Resto         (%)")
    print("  0 - Sair")
    print("-" * 35)


def main() -> None:
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo da calculadora. Até mais!")
            break

        if opcao not in {"1", "2", "3", "4", "5", "6"}:
            print("Opção inválida. Tente novamente.")
            continue

        a = ler_numero("Digite o primeiro número: ")
        b = ler_numero("Digite o segundo número: ")

        try:
            if opcao == "1":
                resultado = somar(a, b)
                operador = "+"
            elif opcao == "2":
                resultado = subtrair(a, b)
                operador = "-"
            elif opcao == "3":
                resultado = multiplicar(a, b)
                operador = "*"
            elif opcao == "4":
                resultado = dividir(a, b)
                operador = "/"
            elif opcao == "5":
                resultado = potencia(a, b)
                operador = "^"
            elif opcao == "6":
                resultado = resto(a, b)
                operador = "%"
            else:
                print("Opção inválida.")
                continue

            print(f"\nResultado: {a} {operador} {b} = {resultado}\n")
        except ValueError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()

