from inputs import *

class Itens:
    def __init__(self, nome_i,informacoes,classificacao,valor_item,quantidade=0):
        self.nome_i = nome_i
        self.classificacao = classificacao
        self.informacoes = informacoes
        self.valor_item = valor_item
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

    def classificar_item(self,it1):










cl_list = ['Quest','Utilitários','Consumíveis','Valor']
raridades = ['Comum','Incomum','Raro','Épico','Lendário','Mítico']

# Utilitários
list_util = ['Corda','Tocha','Mapa da Região','Sonar de Peixes','Picareta']

# Quest Boss
list_quest = ['Cebola Roxa','Galho Vivo','Chave de Castelo','Tampa de Lixeira','Papel com Letra de uma Musica','Carne Corroida','Par de Remos de Madeira','Sonar de Peixes','Papel com Mancha de Sangue','Tampa de Lixeira']

# Consumiveis
list_consu = ['Comida','Poções']
list_pocoes = ['Cura','Mana','Antídoto','Força','Agilidade']
list_food = ['Carne Crua','Fruta','Carne Assada','Pão','Mel','Peixe']

# Valor
list_money = ['Gemas','Minerios']
list_gemas = ['Diamante','Esmeralda','Safira','Rubi','Ametista','Topazio']
list_miner = ['Ferro','Ouro','Prata','Platina','Tungstênio','Mithril','Adamantita','Oricalco','Cristal de Mana']

# Diamante  Lendário
# Esmeralda  Épico
# Safira  Raro
# Rubi  Épico
# Ametista  Incomum
# Topazio  Incomum

# Ferro  Comum
# Ouro  Raro
# Prata  Incomum
# Platina  Épico
# Tungstênio  Raro
# Mithril  Lendário
# Adamantita  Mítico
# Oricalco  Lendário
# Cristal de Mana  Mítico


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