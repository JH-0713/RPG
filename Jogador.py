from winreg import HKEY_CLASSES_ROOT
from inputs import *

class Player:
    def __init__(self, nickname,abilidades,itens,hp = 1500,mana=500,atk = 0,agi = 0,itn = 0,raca = 'Humano',classe = '',sexo='Masculuino',lv = 1,exp_atual = 0,exp_total = 1000):
        self.nickname = nickname
        self.raca = raca
        self.classe = classe
        self.level = lv
        self.hp = hp
        self.mana = mana
        self.atk = atk
        self.agi = agi
        self.itn = itn
        self.sexo = sexo
        self.abilidades = abilidades
        self.itens = itens
        self.exp_atual = exp_atual
        self.exp_total = exp_total

    def apresentar(self):
        print(f'Nickname: {self.nickname}')
        print(f'Raça: {self.raca}')
        print(f'Class: {self.classe}')
        print(f'Level: {self.level}')
        print(f'Vida: {self.hp}')
        print(f'Ataque: {self.atk}')
        print(f'Agilidade: {self.agi}')
        print(f'Inteligencia: {self.itn}')
        print(f'Mana: {self.mana}')
        print(f'Sexo: {self.sexo}')
        print(f'Abilidades: {self.abilidades}')
        print(f'Iventario: {self.itens}')
        print(f'Experiencia: {self.exp_atual}/{self.exp_total}')
        print('-' * 30)

    def abrir_menu(self,pl_):
        print('')
        print('Menu:')
        print('')
        print('[1] Status')
        print('[2] Skills')
        print('[3] Abrir Iventario')
        print('')
        esc1 = int(input('> '))
        if esc1 == 1:
            pl_.abrir_status()
        elif esc1 == 2:
            pl_.abrir_skills(self.abilidades)
        elif esc1 == 3:
            pl_.abrir_inventario(self.itens)



    def abrir_inventario(self,l1):
        x1 = 0
        if len(l1) == 0:
            print('Nenhum Item Encontrado!')
            print('')
            print('Clique na tecla [Enter] para Continar:')
            input('> ')
            print('')
        else:
            for i in l1:
                x1 += 1
                print(f'[{x1}] {i}')
            print('-' * 30)
            print('')
            print('Selecione o Item')
            item1 = input_int('> ')
            print('')

    def abrir_status(self):
        print('')
        print('Status:')
        print('')

        print(f'\033[4mNome:\033[0m',end='      ')
        print(f'{self.nickname}')

        print('\033[4mRaça:\033[0m', end='    ')
        print(f'{self.raca}')

        print('\033[4mClasse:\033[0m',end='    ')
        print(f'{self.classe}')

        print('\033[4mVida:\033[0m',end='      ')
        print(f'{self.hp}')

        print('\033[4mAtaque:\033[0m', end='      ')
        print(f'{self.atk}')

        print('\033[4mAgilidade:\033[0m', end='      ')
        print(f'{self.agi}')

        print('\033[4mInteligencia:\033[0m', end='      ')
        print(f'{self.itn}')

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

    def crirar_player(self):
        print('Crie seu Personagem!')
        print('')
        print(f'Defina o seu Nickname:')
        print('')
        self.nickname = input_str('> ')
        print('')
        print(f'Defina o seu Nickname:')
        print('')
        self.raca = input_str('> ')
        print('')




def exibir(p_):
    print('-' * 30)
    p_.apresentar()
    p_.abrir_menu(p_)

p1 = Player('jh',[],[],classe='Paladino')
#p2 = Player('hj','Paladino',3500,150,[],[])
#exibir(p1)
#exibir(p2)

human_c = ['Cavaleiro','Mercenário','Paladino','Espadachim','Berserker']

def definir_racas(r1):
    print('')
    x1 = 0
    for i in human_c:
        if r1 in i:
            if r1 == i[x1]:
                r1 = i[x1]
                x1 += 1
            print('raça ja definida')

definir_racas(p1.raca)
