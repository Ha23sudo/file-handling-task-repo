# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    # TODO: Create a new text file and write "Hello, world!" to it.
    with open("file_handling.txt", "w") as file:
        file.write("Hello, world!")
    pass

def task2_read_file():
    # TODO: Read the contents of a file and print them to the console.
    with open("file_handling.txt", "r") as file:
        contents = file.read()
        print(contents)

    pass

def task3_append_file():
    # TODO: Append a new line of text to an existing file.
    with open("file_handling.txt", "a") as file:
        file.write("\n My Name is Zain.")

    pass

def task4_count_lines():
    # TODO: Count and print the number of lines in a file.
    with open("file_handling.txt", "r") as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")

    pass

def task5_find_word():
    # TODO: Find whether a specific word exists in the file and how many times.
    word_to_find = input("Enter the word you want to search for: ")
    with open("file_handling.txt", "r") as file:
        contents = file.read()
        count = contents.count(word_to_find)
        if count > 0:
            print(f"The word '{word_to_find}' was found {count} times.")
        else:
            print(f"The word '{word_to_find}' was not found in the file.")
    pass

def task6_copy_file():
    # TODO: Copy the contents of one file to another.
        with open("file_handling.txt", "r") as source_file:
            contents = source_file.read()
    
        with open("copy_of_file_handling.txt", "w") as destination_file:
            destination_file.write(contents)
    
            print("File copied successfully.")
            pass

def task7_replace_word():
    # TODO: Replace a specific word in the file with another word.
    old_word = input("Enter the word you want to replace: ")
    new_word = input("Enter the new word: ")

    with open("file_handling.txt", "r") as file:
        contents = file.read()

    contents = contents.replace(old_word, new_word)

    with open("file_handling.txt", "w") as file:
        file.write(contents)

    print(f"All occurrences of '{old_word}' have been replaced with '{new_word}'.")

    pass
import csv
def task8_read_csv():
    # TODO: Read a CSV file and print each row.
    with open("data.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    pass


def task9_write_csv():
    data = [
        {"Name": "Ali", "Age": 23},
        {"Name": "Zain", "Age": 21},
        {"Name": "asad", "Age": 25}
    ]

    with open("output.csv", "w", newline='') as file:
        fieldnames = ["Name", "Age"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print("Data written to output.csv successfully.")

    pass

def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    pass
