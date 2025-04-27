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
    #CSV file is a simple text file that has values seprated by commas for better readability, sort of a excel sheet
    import csv
    f=open(r"C:\\Users\\hp\\OneDrive\\Desktop\\4th Semester\\Python\\taskfile.csv.txt", 'r')
    values=csv.reader(f)
    for row in values: 
        print(row)
    pass

def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    #create a dictionary , it should have keys and some values  
 data = [
    {'Name': 'Aayan', 'Age': '21', 'GPA': '3.4'},
    {'Name': 'Ali', 'Age': '20', 'GPA': '3.0'},
    {'Name': 'Farhan', 'Age': '21', 'GPA': '3.5'},
    {'Name': 'Hamza', 'Age': '22', 'GPA': '2.9'}
]
# Open a file for writing
 f = open(r"C:\Users\hp\OneDrive\Desktop\4th Semester\Python\taskfile.csv.txt", 'w')
 f.write('Name,Age,GPA\n') #for headings
# Write each students data
 for row in data:
    line = f"{row['Name']},{row['Age']},{row['GPA']}\n"
    f.write(line)
 f.close()
pass

def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    import json
    data = {
    "Name": "Aayan",
    "Age": 21,
    "GPA": 3.4
    }
    f=open(r"C:\Users\hp\OneDrive\Desktop\4th Semester\Python\task10.json", 'w')
    json.dump(data,f) #this creates a file from python and adds data to it using dump command
    f.close()
    f=open(r"C:\Users\hp\OneDrive\Desktop\4th Semester\Python\task10.json", 'r')
    newdata=json.load(f)
    print(newdata)
    pass

#add functions here properly for a menu based program
x=0
while x!=1:
    print("\n      WELCOME TO PYTHON FILE HANDLING SIMULATOR \n")
    print("<---------------- HERE IS A MENU OF WHAT YOU CAN DO IN THIS SIMULATOR ------------>")
    print("Press 1 :       TO  create a new text file and write Hello, world! to it.")
    print("Press 2 :       TO  read the contents of a file and print them to the console.")
    print("Press 3 :       TO  append a new line of text to an existing file.")
    print("Press 4 :       TO  count and print the number of lines in a file.")
    print("Press 5 :       TO  find whether a specific word exists in the file and how many times.")
    print("Press 6 :       TO  copy the contents of one file to another.")
    print("Press 7 :       TO  replace a specific word in the file with another word.")
    print("Press 8 :       TO  read a CSV file and print each row.")
    print("Press 9 :       TO  write a list of dictionaries to a CSV file.")
    print("Press 10 :      TO  create a JSON file from a Python dictionary and read it back.")
    print("Press 11 ******************** TO EXIT THE PROGRAM ******************************")
    choice=int(input("Enter your choice :"))
    if choice ==1:
        task1_create_file()
    elif choice==2:
        task2_read_file()
    elif choice==3:
        task3_append_file()
    elif choice==4:
        task4_count_lines()
    elif choice==5:
        task5_find_word()
    elif choice==6:
        task6_copy_file()
    elif choice==7:
        task7_replace_word()
    elif choice==8:
        task8_read_csv()
    elif choice==9:
        task9_write_csv()
    elif choice==10:
        task10_json_file()
    else:
        print("------> THANK YOU FOR USING THIS SIMULATOR , SEEE YOU NEXT TIME :) ")
        x=1