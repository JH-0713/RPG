def input_int(mensagem):
    while True:
        try:
            num_int = int(input(mensagem))
            return num_int
        except ValueError:
            print('')
            print("digite apenas números")
            print('')



def input_float(mensagem, casas):
    while True:
        try:
            num_float = float(input(mensagem))
            return round(num_float, casas)
        except ValueError:
            print('')
            print("digite apenas números")
            print('')



def input_str(mensagem):
    while True:
        nome = str(input(mensagem))
        if not nome.isalpha():
            print('')
            print("digite apenas com letras")
            print('')
        else:
            return nome
