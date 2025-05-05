import csv
import json
import shutil

def task1_create_file():
    """Create a new text file and write 'Hello, world!' to it."""
    with open('hello.txt', 'w') as file:
        file.write("Hello, world!")

def task2_read_file():
    """Read the contents of a file and print them to the console."""
    try:
        with open('hello.txt', 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")

def task3_append_file():
    """Append a new line of text to an existing file."""
    try:
        with open('hello.txt', 'a') as file:
            file.write("\nThis is an appended line.")
    except FileNotFoundError:
        print("File not found.")

def task4_count_lines():
    """Count and print the number of lines in a file."""
    try:
        with open('hello.txt', 'r') as file:
            lines = file.readlines()
            print(f"Number of lines: {len(lines)}")
    except FileNotFoundError:
        print("File not found.")

def task5_find_word():
    """Find whether a specific word exists in the file and how many times."""
    try:
        word_to_find = "world"  # Example word to search for
        count = 0
        with open('hello.txt', 'r') as file:
            for line in file:
                words = line.split()
                count += words.count(word_to_find)
        print(f"The word '{word_to_find}' appears {count} times.")
    except FileNotFoundError:
        print("File not found.")

def task6_copy_file():
    """Copy the contents of one file to another."""
    try:
        shutil.copyfile('hello.txt', 'hello_copy.txt')
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")

def task7_replace_word():
    """Replace a specific word in the file with another word."""
    try:
        old_word = "world"
        new_word = "Python"
        with open('hello.txt', 'r') as file:
            content = file.read()
        
        updated_content = content.replace(old_word, new_word)
        
        with open('hello.txt', 'w') as file:
            file.write(updated_content)
        print("Word replaced successfully.")
    except FileNotFoundError:
        print("File not found.")

def task8_read_csv():
    """Read a CSV file and print each row."""
    try:
        with open('data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print("CSV file not found.")

def task9_write_csv():
    """Write a list of dictionaries to a CSV file."""
    data = [
        {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
        {'Name': 'Bob', 'Age': 30, 'City': 'Chicago'},
        {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
    ]
    
    with open('output.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Age', 'City']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print("CSV file created successfully.")

def task10_json_file():
    """Create a JSON file from a Python dictionary and read it back."""
    data = {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "courses": ["Math", "Science"]
    }
    
    # Write to JSON file
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    # Read from JSON file
    with open('data.json', 'r') as file:
        loaded_data = json.load(file)
        print("Data read from JSON file:")
        print(loaded_data)