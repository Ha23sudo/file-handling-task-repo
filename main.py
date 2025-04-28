# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

import csv
import json

def task1_create_file():
    # Create a new text file and write "Hello, world!" to it.
    with open('hello_world.txt', 'w') as file:
        file.write("Hello, world!")

def task2_read_file():
    # Read the contents of a file and print them to the console.
    try:
        with open('hello_world.txt', 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")

def task3_append_file():
    # Append a new line of text to an existing file.
    with open('hello_world.txt', 'a') as file:
        file.write("\nThis is an appended line.")

def task4_count_lines():
    # Count and print the number of lines in a file.
    try:
        with open('hello_world.txt', 'r') as file:
            lines = file.readlines()
            print(f"Number of lines: {len(lines)}")
    except FileNotFoundError:
        print("File not found.")

def task5_find_word():
    # Find whether a specific word exists in the file and how many times.
    word_to_find = "world"
    try:
        with open('hello_world.txt', 'r') as file:
            contents = file.read()
            count = contents.count(word_to_find)
            print(f"The word '{word_to_find}' appears {count} times.")
    except FileNotFoundError:
        print("File not found.")

def task6_copy_file():
    # Copy the contents of one file to another.
    try:
        with open('hello_world.txt', 'r') as source_file:
            contents = source_file.read()
        with open('copy_hello_world.txt', 'w') as dest_file:
            dest_file.write(contents)
    except FileNotFoundError:
        print("File not found.")

def task7_replace_word():
    # Replace a specific word in the file with another word.
    word_to_replace = "world"
    replacement_word = "universe"
    try:
        with open('hello_world.txt', 'r') as file:
            contents = file.read()
        contents = contents.replace(word_to_replace, replacement_word)
        with open('hello_world.txt', 'w') as file:
            file.write(contents)
    except FileNotFoundError:
        print("File not found.")

def task8_read_csv():
    # Read a CSV file and print each row.
    try:
        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("CSV file not found.")

def task9_write_csv():
    # Write a list of dictionaries to a CSV file.
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def task10_json_file():
    # Create a JSON file from a Python dictionary and read it back.
    data = {"name": "Alice", "age": 30, "city": "New York"}
    
    # Writing to JSON file
    with open('data.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
    
    # Reading from JSON file
    with open('data.json', 'r') as jsonfile:
        loaded_data = json.load(jsonfile)
        print(loaded_data)

