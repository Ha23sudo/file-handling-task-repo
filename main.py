# file_handling_tasks.py

import csv
import json

def task1_create_file():
    # Create a new text file and write "Hello, world!" to it.
    with open('hello.txt', 'w') as file:
        file.write("Hello, world!")

def task2_read_file():
    # Read and print contents of a file.
    with open('hello.txt', 'r') as file:
        contents = file.read()
        print(contents)

def task3_append_file():
    # Add a new line to an existing file.
    with open('hello.txt', 'a') as file:
        file.write("\nThis is a new appended line.")

def task4_count_lines():
    # Count total number of lines in a text file.
    with open('hello.txt', 'r') as file:
        lines = file.readlines()
        print(f"Total number of lines: {len(lines)}")

def task5_find_word():
    # Count how many times a word appears in a file.
    word_to_find = 'Hello'
    with open('hello.txt', 'r') as file:
        content = file.read()
        count = content.count(word_to_find)
        print(f"The word '{word_to_find}' appears {count} times.")

def task6_copy_file():
    # Copy contents from one file to another.
    with open('hello.txt', 'r') as source_file:
        content = source_file.read()
    with open('hello_copy.txt', 'w') as destination_file:
        destination_file.write(content)

def task7_replace_word():
    # Replace a word in the file with another.
    old_word = 'Hello'
    new_word = 'Hi'
    with open('hello.txt', 'r') as file:
        content = file.read()
    updated_content = content.replace(old_word, new_word)
    with open('hello.txt', 'w') as file:
        file.write(updated_content)

def task8_read_csv():
    # Read and display content of a CSV file.
    with open('sample.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def task9_write_csv():
    # Write structured data into a CSV file.
    data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]
    with open('people.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def task10_json_file():
    # Write a dictionary to JSON and read it back.
    data = {
        "name": "Alice",
        "age": 25,
        "city": "Wonderland"
    }
    with open('data.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    with open('data.json', 'r') as jsonfile:
        loaded_data = json.load(jsonfile)
        print(loaded_data)

def main():
    print("Running Task 1: Create File")
    task1_create_file()

    print("\nRunning Task 2: Read File")
    task2_read_file()

    print("\nRunning Task 3: Append File")
    task3_append_file()

    print("\nRunning Task 4: Count Lines")
    task4_count_lines()

    print("\nRunning Task 5: Find Word")
    task5_find_word()

    print("\nRunning Task 6: Copy File")
    task6_copy_file()

    print("\nRunning Task 7: Replace Word")
    task7_replace_word()

    print("\nRunning Task 8: Read CSV")
    task8_read_csv()

    print("\nRunning Task 9: Write CSV")
    task9_write_csv()

    print("\nRunning Task 10: JSON Handling")
    task10_json_file()

if __name__ == "__main__":
    main()
