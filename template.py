from jinja2 import Environment, FileSystemLoader, select_autoescape
import random


CLASSES_BASE = {
    "wizard" : {
        "strength" : random.randint(1,3),
        "agility" : random.randint(1,3),
        "intelligence" : 15,
        "luck" : random.randint(1,3),
        "temper" : random.randint(1,3),
        "skills" : [
            "Огненный шар",
            "Ледяная стрела",
            "Электрический разряд",
            "Магический щит",
            "Телепортация",
            "Молния небес",
            "Кислотный туман",
            "Психический удар"
        ]
    },
    "warrior" : {
        "strength" : 15,
        "agility" : random.randint(1,3),
        "intelligence" : random.randint(1,3),
        "luck" : random.randint(1,3),
        "temper" : random.randint(1,3),
        "skills" : [
            "Мощный удар",
            "Размашистый взмах",
            "Бросок топора",
            "Щитовой удар",
            "Вихрь клинков",
            "Пронзающий удар",
            "Военный клич",
            "Землетрясение"
        ]
    },
    "hunter" : {
        "strength" : random.randint(1,3),
        "agility" : 15,
        "intelligence" : random.randint(1,3),
        "luck" : random.randint(1,3),
        "temper" : random.randint(1,3),
        "skills" : ["Меткий выстрел",
            "Зов природы",
            "Кровавая рана",
            "Стальной капкан",
            "Призыв ястреба",
            "Дезориентирующий выстрел",
            "Укус виверны",
            "Маскировка в листве"
        ]
    },
    "assassin" : {
        "strength" : random.randint(1,3),
        "agility" : random.randint(1,3),
        "intelligence" : random.randint(1,3),
        "luck" : 15,
        "temper" : random.randint(1,3),
        "skills" : [
            "Смертельный удар",
            "Незаметное приближение",
            "Ядовитый клинок",
            "Теневой клинок",
            "Внезапное исчезновение",
            "Мгновенный бросок",
            "Глушащий удар",
            "Фантомный шаг"
        ]
    },
    "bard" : {
        "strength" : random.randint(1,3),
        "agility" : random.randint(1,3),
        "intelligence" : random.randint(1,3),
        "luck" : random.randint(1,3),
        "temper" : 15,
        "skills" :  [
            "Стремительный прыжок",
            "Электрический выстрел",
            "Ледяной удар",
            "Стремительный удар",
            "Кислотный взгляд",
            "Тайный побег",
            "Ледяной выстрел",
            "Огненный заряд"
        ]
    }
}


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    card_quantity = int(input("Введите количество карточек: "))
    for i in range(card_quantity):
        name = list(input("Введите имя: "))
        race = input("Введите рассу: ")
        character_class = input("Введите свой класс: ")
        skill = random.sample(CLASSES_BASE[name]["skills"][character_class], 3)
        rendered_page = template.render(
            image = f".\images\{character_class}.png",
            name = name[i],
            race = race[i],
            character_class = character_class[i],
            strength = CLASSES_BASE[character_class]["strength"][i],
            agility = CLASSES_BASE[character_class]["agility"][i],
            intelligence = CLASSES_BASE[character_class]["intelligence"][i],
            luck = CLASSES_BASE[character_class]["luck"][i],
            temper = CLASSES_BASE[character_class]["temper"][i],
            first_skill = skill[0][i],
            second_skill = skill[1][i],
            third_skill = skill[2][i]
        )

    with open(f'.\characters\index_{character_class}.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == "__main__":
    main()
