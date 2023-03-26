import pathlib
from pathlib import Path
import requests


"""Cохраняем всех персонажей (имена), которые снимались в фильмах с Дарт Вейдером"""

class Darth_vader():

    # Узнаем в каких фильмах снимался Дарт Вейдер
    def get_films(self):

        base_url = "https://swapi.dev/api/"   # Базовая URL
        darth_resource = "people/4/"          # Ресурс метода GET для получения информации о Дарт Вейдере

        darth_url = base_url + darth_resource
        print(f'Исходная URL:\n{darth_url}')

        # Отправим GET запрос, чтобы узнать в каких фильмах играл Дарт Вейдер
        result_films = requests.get(darth_url)
        result_films.encoding = 'utf-8'
        print(f'Ответ GET запроса:\n{result_films.text}')

        # Сохраним себе список фильмов в которых играл Дарт Вейдер
        check_films = result_films.json()
        films = check_films.get("films")
        print(f'Фильмы с участием Дарт Вейдера:\n{films}')
        return films


    def get_names(self, films):
        # Получим список всех героев из фильмов с Дарт Вейдером
        # Для этого отправим запрос по каждому фильму и сохраним себе список героев
        groups_heroes = []
        for hero in films:
            result_hero = requests.get(hero)
            result_hero.encoding = 'utf-8'
            check_hero = result_hero.json()
            list_hero = check_hero.get("characters")
            groups_heroes.append(list_hero)
        print(f'Вложенный список всех героев:\n{groups_heroes}')

        # Преобразуем двухуровневый список в одноуровневый
        heroes = []
        for group in groups_heroes:
            heroes.extend(group)
        print(f'Одноуровневый список всех героев:\n{heroes}')

        # Удалим из списка повторяющиеся значения
        unique_heroes = set(heroes)
        print(f'Уникальный список всех героев:\n{unique_heroes}')

        # Узнаем имена наших героев, для этого отправим запросы по каждому герою
        list_names = []
        for names in unique_heroes:
            result_name = requests.get(names)
            result_name.encoding = 'utf-8'
            check_name = result_name.json()
            name = check_name.get("name")
            list_names.append(name)
        print(f'Список имён наших героев:\n{list_names}')

        # Сохраним список имён в текстовый файл предварительно очистив файл
        file_path = Path(pathlib.Path.cwd(), "hero_names.txt")
        try:
            file_path.unlink()
            print("Файл hero_names успешно удален\n")
        except FileNotFoundError:
            print("Файл hero_names не найден!\n")

        for name in list_names:
            save_names = open('hero_names.txt', 'a', encoding='utf-8')
            save_names.write(f'{name}\n')
            save_names.close()
        print("Имена героев успешно сохранены в файл hero_names.txt")


characters = Darth_vader()
list_films = characters.get_films()
characters.get_names(list_films)







