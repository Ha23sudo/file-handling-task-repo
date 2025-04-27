# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    # TODO: Create a new text file and write "Hello, world!" to it.
    pass
def task1_create_file():
    with open("hello_world.txt", "w") as file:
        file.write("Hello, world!")


def task2_read_file():
    # TODO: Read the contents of a file and print them to the console.
    pass
def task2_read_file():
    with open("hello_world.txt", "r") as file:
        content = file.read()
        print(content)

def task3_append_file():
    # TODO: Append a new line of text to an existing file.
    pass
def task3_append_file():
    with open("hello_world.txt", "a") as file:
        file.write("\nThis is a new line!")


def task4_count_lines():
    # TODO: Count and print the number of lines in a file.
    pass
def task4_count_lines():
    with open("hello_world.txt", "r") as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")


def task5_find_word():
    # TODO: Find whether a specific word exists in the file and how many times.
    pass
def task5_find_word(word):
    with open("hello_world.txt", "r") as file:
        content = file.read()
        count = content.count(word)
        if count > 0:
            print(f"The word '{word}' exists {count} times in the file.")
        else:
            print(f"The word '{word}' does not exist in the file.")

def task6_copy_file():
    # TODO: Copy the contents of one file to another.
    pass
def task6_copy_file(source_file, destination_file):
    with open(source_file, "r") as src, open(destination_file, "w") as dest:
        dest.write(src.read())
    print(f"Contents copied from '{source_file}' to '{destination_file}'.")

def task7_replace_word():
    # TODO: Replace a specific word in the file with another word.
    pass
def task7_replace_word(old_word, new_word):
    with open("hello_world.txt", "r") as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open("hello_world.txt", "w") as file:
        file.write(content)
    print(f"Replaced '{old_word}' with '{new_word}' in the file.")
import csv


def task8_read_csv():
    # TODO: Read a CSV file and print each row.
    pass
import csv

def task8_read_csv(file_name):
    with open(file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)


def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    pass
import csv

def task9_write_csv(file_name, data):
    with open(file_name, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to '{file_name}'.")


def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    pass
import json

def task10_json_file(file_name, data):
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"JSON data written to '{file_name}'.")
    
    with open(file_name, "r") as json_file:
        content = json.load(json_file)
        print("Read JSON data:")
        print(content)
