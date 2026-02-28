from inputs import *

class Player:
    def __init__(self, nickname,abilidades,itens,hp = 100,mana=50,ataque = 0,agilidade = 0,inteligencia = 0,raca = 'Humano',sub_raca = 'Nenhuma',classe = 'Paladino',sexo='Masculuino',lv = 1,exp_atual = 0,exp_total = 1000):
        # Nome:
        self.nickname = nickname

        # Definições
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

        # lista de Abilidades e Itens
        self.abilidades = abilidades
        self.itens = itens

    def apresentar_player(self):
        # Nome
        print(f'Nickname: {self.nickname}')

        # Definições
        print(f'Raça: {self.raca}')
        print(f'Sub raça: {self.sub_raca}')
        print(f'Class: {self.classe}')
        print(f'Sexo: {self.sexo}')

        # XP
        print(f'Level: {self.level}')
        print(f'Experiencia: {self.exp_atual}/{self.exp_total}')

        # Status
        print(f'Vida: {self.hp}')
        print(f'Ataque: {self.ataque}')
        print(f'agilidadelidade: {self.agilidade}')
        print(f'Inteligencia: {self.inteligencia}')
        print(f'Mana: {self.mana}')
        print('-' * 30)

        # lista de Abilidades e Itens
        print(f'Abilidades: {self.abilidades}')
        print(f'Iventario: {self.itens}')

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
        print('')
        print('Crie seu Personagem!')
        print('')
        print(f'Defina o seu Nickname:')
        print('')
        name = input_str('> ')
        sex_ = definir_sexo()
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
        sub_raca_ = definir_sub_raca(raca_p)
        print('')
        c_ = definir_classe(raca_p)
        print('')
        v1,m1,at1,ag1,i1 = definir_status(raca_p,c_)
        return Player(name,[],[],v1,m1,at1,ag1,i1,raca_p,sub_raca_,c_,sex_)

def definir_sub_raca(r1):
    x1 = 0
    if r1 == 'Humano':
        return 'Humano'

    elif r1 == 'Raça Feral':
        print('')
        print('Defina sua Sub-Classe:')
        print('')
        for i in b1:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
        esc_c = input_int('> ')
        sub_b1 = b1[esc_c - 1]
        print('')
        return sub_b1

    elif r1 == 'Infernais':
        print('')
        print('Defina sua Sub-Classe:')
        print('')
        for i in d1:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
        sub_c = input_int('> ')
        sub_d1 = d1[sub_c - 1]
        print('')
        return sub_d1

    elif r1 == 'Goblin':
        return 'Goblin'

    else:
        print('Defina sua Sub-Raça')
        print('')

def definir_classe(ra_):
    cl_ = 0
    if ra_ == 'Humano':
        print('')
        print(f'Defina o sua Classe:')
        print('')
        x1 = 0
        for i in r_ch:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
        cl_ = input_int('> ')
        print('')
        return r_ch[cl_ - 1]

    elif ra_ == 'Raça Feral':
        print('')
        print(f'Defina o sua Classe:')
        print('')
        x1 = 0
        for i in r_cb:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
        cl_ = input_int('> ')
        print('')
        return r_cb[cl_ - 1]

    elif ra_ == 'Infernais':
        print('')
        print(f'Defina o sua Classe:')
        print('')
        x1 = 0
        for i in r_cd:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
        cl_ = input_int('> ')
        print('')
        return r_cd[cl_ - 1]

    elif ra_ == 'Goblin':
        print('')
        print(f'Defina o sua Classe:')
        print('')
        x1 = 0
        for i in r_cg:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
        cl_ = input_int('> ')
        print('')
        return r_cg[cl_ - 1]

def definir_sexo():
    while True:
        print('')
        print(f'Defina o seu Sexo:')
        print('')
        print('[1] Masculino')
        print('[2] Feminino')
        print('')
        sexo = input_int('> ')
        print('')
        if sexo == 1:
            return 'Masculuino'
        elif sexo == 2:
            return 'Feminino'
        else:
            print('Defina seu Sexo')
            print('')

def definir_status(ra1,cl1):
    if ra1 == 'Humano':
        if cl1 == 'Bardo':
            vida = 115
            mana = 85
            ataque = 15
            agilidade = 16
            inteligencia = 18
            return vida,mana,ataque,agilidade,inteligencia
        elif cl1 == 'Mago':
            vida = 100
            mana = 125
            ataque = 12
            agilidade = 11
            inteligencia = 26
            return vida, mana, ataque, agilidade, inteligencia
        elif cl1 == 'Paladino':
            vida = 150
            mana = 75
            ataque = 21
            agilidade = 12
            inteligencia = 15
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Cavaleiro':
            vida = 165
            mana = 35
            ataque = 23
            agilidade = 10
            inteligencia = 10
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Arqueiro':
            vida = 120
            mana = 55
            ataque = 21
            agilidade = 20
            inteligencia = 14
            return vida, mana, ataque, agilidade, inteligencia

    elif ra1 == 'Raça Feral':
        if cl1 == 'Ladino':
            vida = 120
            mana = 40
            ataque = 24
            agilidade = 23
            inteligencia = 11
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Feiticeiro':
            vida = 110
            mana = 115
            ataque = 15
            agilidade = 13
            inteligencia = 23
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Berserker':
            vida = 180
            mana = 20
            ataque = 27
            agilidade = 15
            inteligencia = 7
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Druida':
            vida = 135
            mana = 105
            ataque = 17
            agilidade = 14
            inteligencia = 21
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Hunter':
            vida = 140
            mana = 45
            ataque = 23
            agilidade = 19
            inteligencia = 12
            return vida, mana, ataque, agilidade, inteligencia

    elif ra1 == 'Infernais':
        if cl1 == 'Bruxo':
            vida = 110
            mana = 115
            ataque = 18
            agilidade = 12
            inteligencia = 24
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Dark Knight':
            vida = 165
            mana = 70
            ataque = 25
            agilidade = 13
            inteligencia = 14
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Invocador':
            vida = 100
            mana = 125
            ataque = 11
            agilidade = 10
            inteligencia = 26
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Mentalista':
            vida = 100
            mana = 130
            ataque = 13
            agilidade = 13
            inteligencia = 27
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Sanguinário':
            vida = 150
            mana = 60
            ataque = 25
            agilidade = 18
            inteligencia = 11
            return vida, mana, ataque, agilidade, inteligencia

    elif ra1 == 'Goblin':
        if cl1 == 'Assasino':
            vida = 115
            mana = 40
            ataque = 25
            agilidade = 24
            inteligencia = 12
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Artífice':
            vida = 125
            mana = 100
            ataque = 16
            agilidade = 13
            inteligencia = 25
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Bruxo':
            vida = 105
            mana = 120
            ataque = 17
            agilidade = 13
            inteligencia = 25
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Arqueiro':
            vida = 115
            mana = 55
            ataque = 22
            agilidade = 22
            inteligencia = 14
            return vida, mana, ataque, agilidade, inteligencia

        elif cl1 == 'Ladino':
            vida = 120
            mana = 45
            ataque = 24
            agilidade = 25
            inteligencia = 12
            return vida, mana, ataque, agilidade, inteligencia

def exibir(pl):
    pl.abrir_menu(pl)

# Raças:
p_racas = ['Humano','Raça Feral','Infernais','Goblin']

# Sub Raças:
beast_sr = ['Weretiger','Lobisomem','Minotauro','Sátiro','Lizardfolk']
b1 = beast_sr

demon_sr = ['Succubo','Incubus','Diabretes/IMP','Demoniacos','Specter','Flame Demon']
d1 = demon_sr

# Classes:
r_ch = ['Bardo','Mago','Paladino','Cavaleiro','Arqueiro'] # Vampiro
r_cb = ['Ladino','Feiticeiro','Berserker','Druida','Hunter']
r_cd = ['Bruxo','Dark Knight','Invocador','Mentalista','Sanguinário']
r_cg = ['Assasino','Artífice','Bruxo','Arqueiro','Ladino']

# Secretas:
#    Human:    Necromante
#    Feral:    Centauro
#    Infernal: Lord_Demon
#    Goblin:   General Gobli

cria_p = Player.criar_player(None)

exibir(cria_p)
