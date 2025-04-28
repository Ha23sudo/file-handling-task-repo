# file_handling_tasks.py

import csv
import json

def task1_create_file():
    with open('example.txt', 'w') as file:
        file.write('Hello, world!')

def task2_read_file():
    with open('example.txt', 'r') as file:
        contents = file.read()
        print(contents)

def task3_append_file():
    with open('example.txt', 'a') as file:
        file.write('\nThis is a new line.')

def task4_count_lines():
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        print(f"Total number of lines: {len(lines)}")

def task5_find_word():
    word_to_find = 'Hello'
    with open('example.txt', 'r') as file:
        contents = file.read()
        count = contents.count(word_to_find)
        print(f"The word '{word_to_find}' appears {count} times.")

def task6_copy_file():
    with open('example.txt', 'r') as src, open('copy_of_example.txt', 'w') as dst:
        contents = src.read()
        dst.write(contents)

def task7_replace_word():
    old_word = 'Hello'
    new_word = 'Hi'
    with open('example.txt', 'r') as file:
        contents = file.read()
    contents = contents.replace(old_word, new_word)
    with open('example.txt', 'w') as file:
        file.write(contents)

def task8_read_csv():
    with open('example.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def task9_write_csv():
    data = [
        {'Name': 'Alice', 'Age': 25},
        {'Name': 'Bob', 'Age': 30},
        {'Name': 'Charlie', 'Age': 22}
    ]
    with open('example.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def task10_json_file():
    data = {
        'name': 'Alice',
        'age': 25,
        'city': 'Wonderland'
    }
    # Write to JSON file
    with open('example.json', 'w') as json_file:
        json.dump(data, json_file)

    # Read back from JSON file
    with open('example.json', 'r') as json_file:
        loaded_data = json.load(json_file)
        print(loaded_data)

        