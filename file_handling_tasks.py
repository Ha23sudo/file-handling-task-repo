# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    # TODO: Create a new text file and write "Hello, world!" to it.
    
    with open('hello.txt','w') as f:
        f.write("Hello world")   

def task2_read_file():
    # TODO: Read the contents of a file and print them to the console.
    with open('hello.txt', 'r') as f:
        content = f.read()
        print(content)


def task3_append_file():
    # TODO: Append a new line of text to an existing file.
    with open('hello.txt', 'a') as f: 
        f.write("\n Fawad Khan Lodhi") 

def task4_count_lines():
    # TODO: Count and print the number of lines in a file.
    with open('hello.txt', 'r') as f:
        lines = f.readlines() 
        line_count = len(lines)  
        print(f"Number of lines in hello.txt: {line_count}")


def task5_find_word():
    # TODO: Find whether a specific word exists in the file and how many times.
    with open('hello.txt', 'r') as f:
        content = f.read()
        word_count = content.lower().count('python') 
        print(f"The word 'Python' appears {word_count} times in hello.txt.")


def task6_copy_file():
    # TODO: Copy the contents of one file to another.
    with open('hello.txt', 'r') as source, open('hellone.txt', 'w') as dest:
        content = source.read() 
        dest.write(content)  


def task7_replace_word():
    # TODO: Replace a specific word in the file with another word.
    with open('hello.txt', 'r') as f:
        content = f.read()
    content = content.replace('world', '')
    with open('hello.txt', 'w') as f:
        f.write(content)


def task8_read_csv():
    # TODO: Read a CSV file and print each row.
    with open('students_scores.csv', 'r') as f:
        lines = f.readlines()
    for line in lines[1:]:
        name = line.split(',')[0]  
        print(name)


def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    students = [
    ['Name', 'Score'],
    ['John Doe', 85],
    ['Jane Smith', 92],
    ['Alice Brown', 78],
    ['Bob White', 88]
]

    with open('students_scores.csv', 'w') as f:
        for student in students:
            f.write(','.join(map(str, student)) + '\n')



def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    pass
