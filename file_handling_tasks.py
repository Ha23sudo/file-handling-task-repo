# file_handling_tasks.py

import csv
import json

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    with open("hello.txt", "w") as f:
        f.write("Hello, World!\n")

def task2_read_file():
    with open("hello.txt", "r") as f:
        content = f.read()
        print("File Content:\n", content)

def task3_append_file():
    with open("hello.txt", "a") as f:
        f.write("Fatima\n")

def task4_count_lines():
    with open("hello.txt", "r") as f:
        lines = f.readlines()
        print("Number of lines:", len(lines))

def task5_find_word():
    def count_word(filename, word):
        with open(filename, "r") as f:
            text = f.read()
            return text.count(word)

    print("Occurrences of 'Python':", count_word("hello.txt", "Python"))

def task6_copy_file():
    with open("hello.txt", "r") as source, open("copy.txt", "w") as dest:
        dest.write(source.read())

def task7_replace_word():
    with open("count.txt", "w") as f:
        f.write("I am working on python for the first time.\nI hope I learn a lot from a language like python.")

    with open("count.txt", "r") as f:
        content = f.read()

    content = content.replace("python", "java")

    with open("count.txt", "w") as f:
        f.write(content)

def task8_read_csv():
    with open("book1.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(row)

def task9_write_csv():
    with open("book1.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age'])
        writer.writerow(['Alice', 25])
        writer.writerow(['Joe', 20])
        writer.writerow(['Ian', 27])
        writer.writerow(['Max', 23])

def task10_json_file():
    data = {
        "name": "Fatima",
        "age": 22,
        "interests": ["Python", "File Handling", "CSV", "JSON"]
    }

    with open("data.json", "w") as f:
        json.dump(data, f)

    with open("data.json", "r") as f:
        loaded_data = json.load(f)
        print("Loaded JSON data:", loaded_data)

def main():
    task1_create_file()
    task2_read_file()
    task3_append_file()
    task4_count_lines()
    task5_find_word()
    task6_copy_file()
    task7_replace_word()
    task9_write_csv()
    task8_read_csv()
    task10_json_file()

if __name__ == "__main__":
    main()
