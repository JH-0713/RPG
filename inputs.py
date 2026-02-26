def input_int(mensagem):
    while True:
        try:
            num_int = int(input(mensagem))
            return num_int
        except ValueError:
            print("digite apenas números")


def input_float(mensagem, casas):
    while True:
        try:
            num_float = float(input(mensagem))
            return round(num_float, casas)
        except ValueError:
            print("digite apenas números")


def input_str(mensagem):
    while True:
        nome = str(input(mensagem))
        if not nome.isalpha():
            print("digite apenas com letras")
        else:
            return nome
