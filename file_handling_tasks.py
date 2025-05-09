# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    # TODO: Create a new text file and write "Hello, world!" to it.
     file=open("file.txt",'w')
    file.write("Hello, World!")
    file.close()
    pass

def task2_read_file():
    # TODO: Read the contents of a file and print them to the console.
    file=open("file.txt",'r')
    content=file.read()
    print(content)
    file.close()
    pass

def task3_append_file():
    # TODO: Append a new line of text to an existing file.
    file=open("file.txt",'a')
    file.write(" How are you people")
    file.close()
    pass

def task4_count_lines():
    # TODO: Count and print the number of lines in a file.
    file=open("file.txt",'r')
    content=file.read()
    lines=content.count('\n')
    print(lines+1)
    file.close()
    pass

def task5_find_word():
    # TODO: Find whether a specific word exists in the file and how many times.
     file=open("file.txt",'r')
    content=file.read()
    word=content.count('\n')
    if word != 0:
        print("yes ,,,",word)
    else:
        print("no")    
    file.close()
    pass

def task6_copy_file():
    # TODO: Copy the contents of one file to another.
    file=open("file.txt",'r')
    file2=open("file2.txt",'w')
    for i in file:
        file2.write(i)
    file.close() 
    file2.close()   
    pass

def task7_replace_word():
    # TODO: Replace a specific word in the file with another word.
    old_word = "Hello"
    new_word = "Hi"
    with open("example.txt", "r") as f:
        content = f.read()
    content = content.replace(old_word, new_word)
    with open("example.txt", "w") as f:
        f.write(content)
    pass

def task8_read_csv():
    # TODO: Read a CSV file and print each row.
     with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    pass

def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
    with open("output.csv", "w", newline='') as f:
        fieldnames = ["name", "age"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    pass

def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    data = {"name": "Alice", "age": 25}
    with open("data.json", "w") as f:
        json.dump(data, f)

    with open("data.json", "r") as f:
        read_data = json.load(f)
        print(read_data)
    pass


# ------------------------------
# Function Calls for Testing
# ------------------------------


#    task1_create_file()
 #   task2_read_file()
 #   task3_append_file()
 #   task4_count_lines()
 #   task5_find_word()
 #   task6_copy_file()
 #   task7_replace_word()
 #   task2_read_file()       
#  task9_write_csv()
 #   task8_read_csv()
 #   task10_json_file()