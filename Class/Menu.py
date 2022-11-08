import os
from .Utils import *
from getch import getch
from print_color import print


class menu:

    def __init__(self, ind: str = '>', color: str = 'white'):
        self.execute: list = []
        self.__ENTER = 10
        self.__W = 119
        self.__S = 115
        self.__J = 106
        self.__K = 107
        self.menu = MENU
        self.color = color
        self.ind = ind+' '

    def __clear(self) -> None:
        os.system('clear')

    def __print_menu(self, keys) -> None:
        self.__clear()
        print(TITLE, format='bold', color='blue')
        print(DESCRIPTION, format='bold')
        for i, option in enumerate(keys):
            if self.ind in option:
                print(option, color=self.color, format='bold')
            else:
                if '-' in option:
                    spazi = ' '*(len(self.ind)-1)
                    print(f'{spazi} {option}', format='bold')
                else:
                    print(option)

    def run(self) -> None:
        for i in self.execute:
            i()
        print('Performed !!!')

    def start(self) -> int:
        self.__clear()
        index: int = 0
        keys = list(self.menu.keys())
        keys[index] = self.ind + keys[index]
        self.__print_menu(keys)
        keys = list(self.menu.keys())
        while True:
            key = ord(getch())
            if key in [self.__W, self.__K]:
                keys[index] = keys[index].replace(self.ind, '')
                self.__clear()
                if index == 0:
                    index = len(keys) - 1
                else:
                    index -= 1
                keys[index] = self.ind + keys[index]
                self.__print_menu(keys)
            elif key in [self.__S, self.__J]:
                self.__clear()
                keys[index] = keys[index].replace(self.ind, '')
                if index+1 < len(keys):
                    index += 1
                else:
                    index = 0
                keys[index] = self.ind + keys[index]
                self.__print_menu(keys)
            elif key == self.__ENTER:
                if 'Exit' in keys[index]:
                    exit()
                elif 'Run' in keys[index]:
                    self.run()
                elif '-' in keys[index]:
                    ...
                elif '✔️' in keys[index]:
                    keys[index] = keys[index].replace(
                        ' ✔', '').replace(self.ind+' ', '').strip()
                    print(self.menu.get(list(self.menu.keys())[index]))
                    self.execute.remove(self.menu.get(
                        list(self.menu.keys())[index]))
                    print(self.execute)
                    self.__print_menu(keys)
                else:
                    self.execute.append(self.menu.get(
                        list(self.menu.keys())[index]))
                    keys[index] += ' ✔️'
                    print(self.execute)
                    self.__print_menu(keys)
