import json
import os
from dataclasses import dataclass, asdict, field


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

    def get_name(self):
        return f"{self.name_discord[:15]:<15}\t[ {self.name_github} ]"

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

    def print_homework_status(self):
        GREEN = "\033[92m"
        RED = "\033[91m"
        RESET = "\033[0m"

        status_items = []
        for hw, completed in self.homework_completion.items():
            if completed:
                status_items.append(f"{GREEN}{hw}{RESET}")
            else:
                status_items.append(f"{RED}{hw}{RESET}")

        status_string = " ".join(status_items)
        print(f"{self.get_name():<40}: {status_string}")


def get_subdirectories(directory):
    if not os.path.isdir(directory):
        return []

    return [
        name
        for name in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, name))
    ]


def read_students_from_file(file_path: str) -> dict[str, StudentInfo]:
    student_data = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                clean_line = line.strip()
                if not clean_line:
                    continue

                parts = clean_line.split(":", 1)
                if len(parts) != 2:
                    print(f"Format error in line: {clean_line}")
                    continue

                name_discord_raw = parts[0].strip()
                name_github_raw = parts[1].strip()

                name_discord = name_discord_raw.strip('"')
                name_github = name_github_raw.strip('"')

                student = StudentInfo(
                    name_discord=name_discord, name_github=name_github
                )

                student_data[name_github] = student

    except FileNotFoundError:
        print(f"Error: File at path '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return {}

    return student_data


STUDENTS = read_students_from_file("./hw/github_username.txt")
current_directory = "./hw"
subdirs_current = get_subdirectories(current_directory)
unidentified_students = set()
for subdir in subdirs_current:
    subdirs = get_subdirectories(f"{current_directory}/{subdir}")
    for key in subdirs:
        if key not in STUDENTS:
            unidentified_students.add(key)
        else:
            STUDENTS[key].homework_completion[subdir] = True

print("Unidentified students:")
for u_student in unidentified_students:
    print(f"\t{u_student}")
print(f"Student count:\t{len(STUDENTS)}\t{len(set(STUDENTS))}".center(70))
for name, student in {
    key: STUDENTS[key] for key in sorted(STUDENTS, key=lambda k: k.lower())
}.items():
    if any([value for _, value in student.homework_completion.items()]):
        student.print_homework_status()
