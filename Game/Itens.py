from inputs import *

class Itens:
    def __init__(self, nome_i,classificacao,quantidade=0):
        self.nome_i = nome_i
        self.classificacao = classificacao
        self.quantidade = quantidade

    def info_iten(self,list_i1):
        x1 = 0
        for i in list_i1:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
        if len(list_i1) != 0:
            print('Selecione o Item da Lista:')
            print('')
            i1 = input_int('> ')
        else:
            print('Nenhum Item Encontrado')
            print('')
            print('')
            print('Clique na Tecla [Enter] para Continuar:')
            input('> ')


    #def classificar_item(self):








cl_list = ['Quest','Utilitários','Consumíveis','Valor']

list_util = ['Corda','Tocha','Mapa da Região','Sonar de Peixes']
list_quest = ['Chave de Castelo','Tampa de Lixeira','Par de Remos de Madeira','Papel com mancha de Sangue','Cebola Roxa','Papel com Letra de uma Musica','']

# Bosses Secretos:

# Floresta
# Cebola Roxa -> Sherek * Dia
# Galho Vivo -> Salgueiro Lutador * Noite

# Villa
# Chave de Castelo -> Dracula * Dia
# Tampa de Lixeira -> 208125 * Dia

# Caverna
# Papel com Letra de uma Musica -> Bob Esponja da Caverna * Qualquer Horario
# Carne Corroida -> Reptile * Qualquer Horario

# Mar
# Par de Remos de Madeira -> Cthulhu * Noite
# Sonar de Peixes -> Monstro do Lago Ness * Dia

# Submundo
# Papel com Mancha de Sangue -> Mosca * Qualquer Horario
# Tampa de Lixeira -> 208125 * Dia
