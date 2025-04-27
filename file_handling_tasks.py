# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    # TODO: Create a new text file and write "Hello, world!" to it.
    pass
    with open('hello.txt', 'w') as file:
        file.write("Hello, world!")
def task2_read_file():
    # TODO: Read the contents of a file and print them to the console.
    pass 
     with open('hello.txt', 'r') as file:
        contents = file.read()
        print(contents)

def task3_append_file():
    # TODO: Append a new line of text to an existing file.
    pass
        with open('hello.txt', 'a') as file:
        file.write("\nThis is an appended line.")

def task4_count_lines():
    # TODO: Count and print the number of lines in a file.
    pass
        with open('hello.txt', 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")

def task5_find_word():
    # TODO: Find whether a specific word exists in the file and how many times.
    pass
      with open('hello.txt', 'r') as file:
        contents = file.read()
        count = contents.count(word)
        if count > 0:
            print(f"The word '{hello}' was found {count} times.")
        else:
            print(f"The word '{hello}' was not found.")

def task6_copy_file():
    # TODO: Copy the contents of one file to another.
    pass
        with open('hello.txt', 'r') as source_file:
        contents = source_file.read()
        with open('copy_of_hello.txt', 'w') as dest_file:
        dest_file.write(contents)

def task7_replace_word():
    # TODO: Replace a specific word in the file with another word.
    pass
     with open('hello.txt', 'r') as file:
        contents = file.read()
        contents = contents.replace(old_word, new_word)
     with open('hello.txt', 'w') as file:
        file.write(contents)

def task8_read_csv():
    # TODO: Read a CSV file and print each row.
    pass
        with open('data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    pass    
        with open('output.csv', 'w', newline='') as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    pass
    # Create JSON file
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    # Read JSON file
    with open('data.json', 'r') as json_file:
        loaded_data = json.load(json_file)
        print(loaded_data)
