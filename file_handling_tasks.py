def task1_create_file():
    # Create a new text file and write "Hello, world!" to it.
    with open("example.txt", "w") as file:
        file.write("Hello, world!")

def task2_read_file():
    # Read the contents of a file and print them to the console.
    try:
        with open("example.txt", "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("The file does not exist.")

def task3_append_file():
    # Append a new line of text to an existing file.
    with open("example.txt", "a") as file:
        file.write("\nAppending a new line to the file.")

def task4_count_lines():
    # Count and print the number of lines in a file.
    try:
        with open("example.txt", "r") as file:
            line_count = sum(1 for line in file)
            print(f"Number of lines in the file: {line_count}")
    except FileNotFoundError:
        print("The file does not exist.")

def task5_find_word(word):
    # Find whether a specific word exists in the file and how many times.
    try:
        with open("example.txt", "r") as file:
            contents = file.read()
            count = contents.lower().split().count(word.lower())
            print(f"The word '{word}' appears {count} times in the file.")
    except FileNotFoundError:
        print("The file does not exist.")

def task6_copy_file():
    # Copy the contents of one file to another.
    try:
        with open("example.txt", "r") as source_file:
            contents = source_file.read()
        with open("copy_of_example.txt", "w") as destination_file:
            destination_file.write(contents)
        print("File copied successfully.")
    except FileNotFoundError:
        print("The source file does not exist.")

def task7_replace_word(old_word, new_word):
    # Replace a specific word in the file with another word.
    try:
        with open("example.txt", "r") as file:
            contents = file.read()
        updated_contents = contents.replace(old_word, new_word)
        with open("example.txt", "w") as file:
            file.write(updated_contents)
        print(f"The word '{old_word}' has been replaced with '{new_word}'.")
    except FileNotFoundError:
        print("The file does not exist.")

import csv

def task8_read_csv():
    # Read a CSV file and print each row.
    try:
        with open("example.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print("The CSV file does not exist.")

import csv

def task9_write_csv():
    # Write a list of dictionaries to a CSV file.
    data = [
        {"Name": "Alice", "Age": 25, "City": "New York"},
        {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "City": "Chicago"}
    ]
    with open("output.csv", "w", newline="") as csv_file:
        fieldnames = ["Name", "Age", "City"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)
    print("CSV file created successfully.")

import json

def task10_json_file():
    # Create a JSON file from a Python dictionary and read it back.
    data = {
        "Name": "Alice",
        "Age": 25,
        "City": "New York"
    }
    # Write the dictionary to a JSON file.
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)
    print("JSON file created successfully.")

    # Read the JSON file.
    with open("data.json", "r") as json_file:
        loaded_data = json.load(json_file)
        print("Data read from JSON file:", loaded_data)
