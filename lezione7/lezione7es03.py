class Animal:

    def __init__(ani, name: str, legs: int):
        ani.name: str = name
        ani.legs: str = legs

spider = Animal("Spider", 8)
rat = Animal("Rat.", 3)

print(f'Nome ={spider.name},  Legs = {spider.legs}')
print(f'Nome ={rat.name},  Legs = {rat.legs}')

rat.legs = 4
print(f'Legs = {rat.legs}')