from jinja2 import Environment, FileSystemLoader, select_autoescape
import random

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')

clases_base = {
    "wizard" : {
        "strength" : random.randint(1,3),
        "agility" : random.randint(1,3),
        "intelligence" : 15,
        "luck" : random.randint(1,3),
        "temper" : random.randint(1,3)
    },
    "warrior" : {
        "strength" : 15,
        "agility" : random.randint(1,3),
        "intelligence" : random.randint(1,3),
        "luck" : random.randint(1,3),
        "temper" : random.randint(1,3)
    },
    "hunter" : {
        "strength" : random.randint(1,3),
        "agility" : 15,
        "intelligence" : random.randint(1,3),
        "luck" : random.randint(1,3),
        "temper" : random.randint(1,3)
    },
    "assassin" : {
        "strength" : random.randint(1,3),
        "agility" : random.randint(1,3),
        "intelligence" : random.randint(1,3),
        "luck" : 15,
        "temper" : random.randint(1,3)
    },
    "bard" : {
        "strength" : random.randint(1,3),
        "agility" : random.randint(1,3),
        "intelligence" : random.randint(1,3),
        "luck" : random.randint(1,3),
        "temper" : 15
    }
}

skills = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]

skill_list = random.sample(skills, 3)

question = int(input("Введите количество карточек: "))
for i in range(question):
    name = input("Введите имя: ")
    race = input("Введите рассу: ")
    character_class = input("Введите свой класс: ")
    rendered_page = template.render(
        image = f".\images\{character_class}.png",
        name = name[i],
        race = race[i],
        character_class = character_class[i],
        strength = clases_base[character_class]["strength"][i],
        agility = clases_base[character_class]["agility"][i],
        intelligence = clases_base[character_class]["intelligence"][i],
        luck = clases_base[character_class]["luck"][i],
        temper = clases_base[character_class]["temper"][i],
        first_skill = skill_list[1][i],
        second_skill = skill_list[2][i],
        third_skill = skill_list[3][i]
    )

with open(f'.\characters\index_{i}.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)