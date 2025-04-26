# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    # TODO: Create a new text file and write "Hello, world!" to it.
  f = open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling.txt", 'w')
  f.write("Hello World this is me ")
  f.close()
  f = open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling.txt", 'r')
  print(f.read())
  f.close()
pass

def task2_read_file():
    # TODO: Read the contents of a file and print them to the console.
    f = open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling.txt", 'r')
    print(f.read())
    f.close()
    pass

def task3_append_file():
    # TODO: Append a new line of text to an existing file.
    #using a type for appending the file
    f = open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling.txt", 'a')
    f.write("\nThis is a new line according to the senario")
    f = open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling.txt", 'r')
    print(f.read()) #rechecking on the console
    f.close()
pass

def task4_count_lines():
    # TODO: Count and print the number of lines in a file.
    f = open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling.txt", 'r')
    line=f.readlines() #storing all lines as a list including spaces
    count=len(line)
    print("The total number of lines is :", count)
    pass

def task5_find_word():
    # TODO: Find whether a specific word exists in the file and how many times.
    f = open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling.txt", 'r')
    line=f.readline()
    w=input("Enter a word to find in the file : ")
    count=0
    for line in f:  
        words=line.split()
        count+=words.count(w)
    if count==0:
        print("The word you want is not available in the file  ")
    else:
        print("Your word : '",w,"'  Occurs : ",count," times in the file")
    pass

def task6_copy_file():
    # TODO: Copy the contents of one file to another.
    f=open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling.txt", 'r')
    t=open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling 2.txt", 'w')
    for line in f:
        t.write(line)

    pass

def task7_replace_word():
    # TODO: Replace a specific word in the file with another word.
    f = open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling 2.txt ", 'r')
    line=f.read()
    w=input("Enter a word to replace in the file : ")
    newword=input("Enter a word to replace with : ")
    count=line.count(w)
    if count==0:
        print("The word you want is not available in the file  ")
    else:
         
         update=line.replace(w,newword)
         f = open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\GIT with File handling 2.txt", 'w')
         f.write(update)
    pass
def task8_read_csv():
    # TODO: Read a CSV file and print each row.
    pass

def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    pass

def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    pass

#add functions here properly for a menu based program
task7_replace_word()
