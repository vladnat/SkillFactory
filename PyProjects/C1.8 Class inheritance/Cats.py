from Pet import Pets

cats = [
    Pets(nickname='Барон', gender='мальчик', age=2),
    Pets(nickname='Сэм', gender='мальчик', age=2)
]

for pet in cats:
    pet.get_cats()