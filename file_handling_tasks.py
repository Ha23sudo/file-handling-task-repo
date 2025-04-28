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
    file=open("file.txt",'r')
    line=file.read()
    w=input("Enter a word to replace ")
    newword=input("Enter new word ")
    count=line.count(w)
    if count==0:
        print("Word not found")
    else:
        update=line.replace(w,newword)
        file=open("file.txt",'w')
        file.write(update)        
    pass

def task8_read_csv():
    # TODO: Read a CSV file and print each row.
    import csv
    file=open("file.txt",'r')
    values=csv.reader(file)
    for i in values:
        print(i)
    pass

def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    data =[
        {'Fruit':'Lychee','Color':'White'},{'Fruit':'Orange','Color':'Orange'}
    ]
    file=open("file.csv.txt",'w')
    file.write("Fruit,Color\n")
    for i in data:
        line=f"{i['Fruit']},{i['Color']}\n"
        file.write(line)
    file.close()    
    pass

def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    pass

#task1_create_file()
#task2_read_file()
#task3_append_file()
#task4_count_lines()
#task5_find_word()
#task6_copy_file()
#task7_replace_word()
#task8_read_csv()
task9_write_csv()