# Заменяемые слова
replacements = {
    "Armor": "Броня",
    "Gaiters": "Брюки",
    "Gauntlet": "Перчатки",
    "Helmet": "Шлем",
    "Boots": "Сапоги",
    "Blade": "Блейд",
    "Divider": "Дивайдер",
    "Bow": "Лук",
    "Mace": "Магия",
    "Shield": "Щит",
    "Splinter": "Кастеты",
    "Spear": "Копьё",
    "Dual Sword": "Дуалы",
    "Slayer": "Дагер",
    "Axe": "Топор",
    "Robe": "Роба",
    "Heavy": "Тяжёлая",
    "Light": "Лёгкая",
    "? lvl": "3 ур",
    "Wings": "Крылья",
    # "Platinum": "Платинум"
    "Crocodile": "Крокодила"
}

def replace_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Делаем замены
        for en, ru in replacements.items():
            content = content.replace(en, ru)

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Файл '{filename}' успешно обработан.")
    except Exception as e:
        print(f"Ошибка: {e}")

# Пример использования
replace_words_in_file("platinum.txt")  # замените на имя вашего файла
