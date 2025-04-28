def task1_create_file():
    # Create a new text file and write "Hello, world!" to it
    with open('hello.txt', 'w') as file:
        file.write('Hello, world!')

def task2_read_file():
    # Read and print the contents of a file
    with open('hello.txt', 'r') as file:
        print(file.read())

def task3_append_file():
    # Append a new line of text to an existing file
    with open('hello.txt', 'a') as file:
        file.write('\nAppended line.')

def task4_count_lines():
    # Count and print the number of lines in a file
    with open('hello.txt', 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")

def task5_find_word():
    # Find if a specific word exists and count its occurrences
    word_to_find = 'Hello'
    with open('hello.txt', 'r') as file:
        content = file.read()
        count = content.count(word_to_find)
        print(f"'{word_to_find}' found {count} times.")

def task6_copy_file():
    # Copy contents from one file to another
    with open('hello.txt', 'r') as src, open('copy_hello.txt', 'w') as dest:
        dest.write(src.read())

def task7_replace_word():
    # Replace a word in the file and save changes
    with open('hello.txt', 'r') as file:
        content = file.read()
    new_content = content.replace('Hello', 'Hi')
    with open('hello.txt', 'w') as file:
        file.write(new_content)
task1_create_file()
task2_read_file()
task3_append_file()
task2_read_file()  # to see the appended content
task4_count_lines()
task5_find_word()
task6_copy_file()
task7_replace_word()
task2_read_file()  # to see the replaced content

