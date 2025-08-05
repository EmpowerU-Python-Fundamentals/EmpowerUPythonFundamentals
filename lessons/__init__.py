import json
import os
import csv
from dataclasses import dataclass, asdict, field
from io import StringIO


@dataclass
class StudentInfo:
    name_github: str = ""
    name_moodle: str = ""
    hw_root_folder_name: str = ""
    name_discord: str = ""
    homework_completion: dict = field(
        default_factory=lambda: {f"hw{i:02d}": False for i in range(6, 15)}
    )

    CSV_HEADERS = [
        "name_github",
        "name_moodle",
        "hw_root_folder_name",
        "name_discord",
    ] + [f"hw{i:02d}" for i in range(6, 15)]

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

    def to_csv_row(self):
        data_dict = self.to_dict()
        row_values = []
        for header in self.CSV_HEADERS:
            if header in data_dict:
                row_values.append(data_dict[header])
            elif header in data_dict.get("homework_completion", {}):
                row_values.append(data_dict["homework_completion"][header])
            else:
                row_values.append(None)
        return tuple(row_values)


def get_subdirectories(directory):
    # Перевіряємо, чи існує директорія і чи це саме директорія
    if not os.path.isdir(directory):
        print(f"Помилка: Директорії '{directory}' не існує.")
        return []

    # Використовуємо list comprehension для створення списку субдиректорій
    return [
        name
        for name in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, name))
    ]

STUDENTS = {}
# Приклад для поточної директорії
current_directory = "./hw"
subdirs_current = get_subdirectories(current_directory)
print(f"Субдиректорії в поточній директорії: {subdirs_current}")
for subdir in subdirs_current:
    print(f"Обробка субдиректорії: {subdir}")
    subdirs = get_subdirectories(f"{current_directory}/{subdir}")
    for key in subdirs:
        if key not in STUDENTS:
            STUDENTS[key] = StudentInfo(
                name_github=key
            )
            STUDENTS[key].homework_completion[subdir] = True
    print(f"\tСубдиректорії: {subdirs}")


from pprint import pprint
print(sorted(STUDENTS.keys()))
pprint(STUDENTS)

['Aboiko', 'AndriiNavy', 'Astronaunt-08', 'Astronaut-08', 'ByteCraftMaster', 'Danil-Shevchenko', 'ElveeBolt', 'Eugen1017', 'Hryhorii1203', 'IhorTre', 'IlliaChystoiev', 'KShust', 'KritAnatolii', 'Leraaaaa-codder', 'Makartvit', 'NightOutlaw', 'PCkyrylo2569', 'Print777', 'ReiGarr', 'RexSplode', 'Schevchenko0207', 'Serg-Pro', 'Serg_Pro', 'Shevchenko0207', 'UBIVATOR161', 'VadHk', 'VasiaZozulia', 'VikaLiakh', 'ViktorChuikov', 'VolodymyrSkaskiv', 'WorkTimwan', 'YuryyBright', 'ZenBay', 'alchemyks', 'anatoleek', 'bezoOleksa', 'brylinskyi', 'deboramay', 'dimonstools', 'f00a0a', 'fedchuna', "fedchuna'", 'illyagoncharov', 'imvikushka', 'inna-rst', 'ivansstef', 'ivze0115', 'kgorova', 'krekhtiuk', 'lerakovaliuk', 'lhalam', 'lians', 'maksymminin', 'mankret', 'marlit7', 'nezhumira', 'nyckolay', 'oleksandr-zeero', 'olymp7', 'omeliana-omeliana', 'picter-max', 'saudeawd', 'tolkov69', 'twlf', 'twlfh', 'uliana', 'urrussov', 'vikaliakh', 'vlbezbozhnyi', 'vonco8888', 'vpavlikk', 'yarusol', 'yuliaklimchuk']