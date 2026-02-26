class Player:
    def __init__(self, nickname,classe,hp,mana,abilidades,itens,genero='Masculuino',lv = 1):
        self.nickname = nickname
        self.classe = classe
        self.level = lv
        self.hp = hp
        self.mana = mana
        self.genero = genero
        self.abilidades = abilidades
        self.itens = itens

    def apresentar(self):
        print(f'Nickname: {self.nickname}')
        print(f'Class: {self.classe}')
        print(f'Level: {self.level}')
        print(f'Vida: {self.hp}')
        print(f'Mana: {self.mana}')
        print(f'Genero: {self.genero}')
        print(f'Abilidades: {self.abilidades}')
        print(f'Iventario: {self.itens}')
        print('-' * 30)

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
            item1 = input('> ')
            print('')


def exibir(p_):
    print('-' * 30)
    p_.apresentar()
    p_.abrir_inventario(p_.itens)


p1 = Player('jh','Necromante',2500,250,[],[1,2,3,4])
p2 = Player('hj','Paladino',3500,150,[],[])
exibir(p1)
exibir(p2)
