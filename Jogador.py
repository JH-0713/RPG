from ftplib import parse150
from xml.etree.ElementPath import prepare_child

from inputs import *

class Player:
    def __init__(self, nickname,abilidades,itens,hp = 100,mana=50,ataque = 0,agilidade = 0,inteligencia = 0,raca = 'Humano',sub_raca = 'Nenhuma',classe = 'Paladino',sexo='Masculuino',lv = 1,exp_atual = 0,exp_total = 1000):
        # Nome:
        self.nickname = nickname

        # Raca e classe
        self.sexo = sexo
        self.raca = raca
        self.sub_raca = sub_raca
        self.classe = classe

        # XP
        self.level = lv
        self.exp_atual = exp_atual
        self.exp_total = exp_total

        # Status
        self.hp = hp
        self.mana = mana
        self.ataque = ataque
        self.agilidade = agilidade
        self.inteligencia = inteligencia

        # listas de player
        self.abilidades = abilidades
        self.itens = itens

    def apresentar_player(self):
        print(f'Nickname: {self.nickname}')
        print(f'Raça: {self.raca}')
        print(f'Sub raça: {self.sub_raca}')
        print(f'Class: {self.classe}')
        print(f'Level: {self.level}')
        print(f'Vida: {self.hp}')
        print(f'Ataque: {self.ataque}')
        print(f'agilidadelidade: {self.agilidade}')
        print(f'Inteligencia: {self.inteligencia}')
        print(f'Mana: {self.mana}')
        print(f'Sexo: {self.sexo}')
        print(f'Abilidades: {self.abilidades}')
        print(f'Iventario: {self.itens}')
        print(f'Experiencia: {self.exp_atual}/{self.exp_total}')
        print('-' * 30)

    def abrir_menu(self,pl_):
        while True:
            print('')
            print('Menu:')
            print('')
            print('[1] Status')
            print('[2] Skills')
            print('[3] Abrir Iventario')
            print('[0] Fechar Menu')
            print('')
            esc1 = input_int('> ')
            if esc1 == 1:
                pl_.abrir_status()
            elif esc1 == 2:
                pl_.abrir_skills(self.abilidades)
            elif esc1 == 3:
                pl_.abrir_inventario(self.itens)
            elif esc1 == 0:
                break
            else:
                print('')
                print('Clique na tecla [Enter] para Continar:')
                input('> ')
                print('')


    def abrir_inventario(self,l1):
        x1 = 0
        if len(l1) == 0:
            print('')
            print('Nenhum Item Encontrado!')
            print('')
            print('Clique na tecla [Enter] para Continar:')
            input('> ')
            print('')
        else:
            print('')
            print('Selecione o Item:')
            for i in l1:
                x1 += 1
                print(f'[{x1}] {i}')
            print('-' * 30)
            print('')
            item1 = input_int('> ')
            print('')

    def abrir_status(self):
        print('')
        print('Status:')
        print('')

        print(f'\033[4mNome:\033[0m',end='      ')
        print(f'{self.nickname}')

        print('\033[4mRaça:\033[0m', end='      ')
        print(f'{self.raca}')

        print('\033[4mSub Raça:\033[0m', end='  ')
        print(f'{self.sub_raca}')

        print('\033[4mClasse:\033[0m',end='    ')
        print(f'{self.classe}')

        print('\033[4mVida:\033[0m',end='      ')
        print(f'{self.hp}')

        print('\033[4mSTR:\033[0m', end='       ')
        print(f'{self.ataque}')

        print('\033[4mDEX:\033[0m', end='       ')
        print(f'{self.agilidade}')

        print('\033[4mINT:\033[0m', end='       ')
        print(f'{self.inteligencia}')

        print('\033[4mMana:\033[0m',end='      ')
        print(f'{self.mana}')

        print('\033[4mSexo:\033[0m',end='      ')
        print(f'{self.sexo}')

        print('\033[4mLv:\033[0m',end='        ')
        print(f'{self.level}')

        print('\033[4mXP:\033[0m',end='        ')
        print(f'{self.exp_atual}/{self.exp_total}')

        print('')
        print('Clique na Tecla [Enter] para Continuar:')
        input('> ')

    def abrir_skills(self,a1):
        print('')
        print('Skills:')
        print('')
        x1 = 0
        for i in a1:
            x1 += 1
            print(f'[{x1}] {i}')
            print('')
        print('')
        print('Clique na Tecla [Enter] para Continuar:')
        input('> ')

    def criar_player(self):
        print('Crie seu Personagem!')
        print('')
        print(f'Defina o seu Nickname:')
        print('')
        name = input_str('> ')
        print('')
        print(f'Defina o seu Sexo:')
        print('')
        print('[1] Masculino')
        print('[2] Feminino')
        print('')
        sexo = input_int('> ')
        sexo_p = definir_sexo(sexo)
        print('')
        print(f'Defina o sua Raça:')
        print('')
        x1 = 0
        for i in p_racas:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
        esc1 = input_int('> ')
        raca_p = p_racas[esc1 - 1]
        print('')
        if raca_p == 'Humano':
            print('')
            print('Defina sua Classe:')
            print('')
            x1 = 0
            for i in human_c:
                x1 += 1
                print(f'[{x1}] {i}')
            print('')
            esc2 = input_int('> ')
            clas_p = human_c[esc2 - 1]
            print('')
            if clas_p == human_c[esc2 - 1]:
                p1 = Player(name, [], [], 130, 40, 14, 8, 7, raca_p, sub_raca_p, clas_p, sexo_p)
                return p1

        else:
            print('Error')


def definir_classe(r1):
    if r1 == 'Humano':
        print('')
        print('Defina sua Classe:')
        print('')
        x1 = 0
        for i in human_c:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
        esc2 = input_int('> ')
        clas_p = human_c[esc2 - 1]
        print('')


def definir_sexo(s1):
    while 1:
        if s1 == 1:
            return 'Masculuino'
        elif s1 == 2:
            return 'Feminino'
        else:
            print('')
            print('Insira o numero de correto')
            print('')
            pass

def exibir():
    pl = Player.criar_player(None)
    pl.apresentar_player()



p_racas = ['Humano','Homem Féra','Demonio','Goblin']

human_c = ['Cavaleiro','Mercenário','Paladino','Espadachim','Berserker']
h1 = human_c

beast_c = ['Weretiger','Lobisomem','Minotauro','Sátiro','Lizardfolk']
b1 = beast_c

demon_c = ['Succubo','Incubus','Diabretes/IMP','Shadowfiend','Specter','Flame Demon']
d1 = demon_c

goblin_c = ['Saqueador','Arqueiro','Gerreiro','Engenheiro','Assasino']
g1 = goblin_c

#exibir()
