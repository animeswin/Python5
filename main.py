def maior_numero(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

resultado = maior_numero(10, 20, 15)
print(f"O maior número é: {resultado}")