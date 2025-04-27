# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.
import csv
import json
def task1_create_file():
     with open("OSSD.txt","w") as f:#open file OSSD.txt
        f.write("Hello, world!")#helloworld message

def task2_read_file():
    with open("OSSD.txt","r") as f:#open file in read mode
        print(f.read())#read and print

def task3_append_file():
    with open("OSSD.txt","a") as f:#open file to append 
        f.write("\nappended.")#add appended line

def task4_count_lines():
    with open("OSSD.txt","r") as f:
        lines=f.readlines()
        print(f"Total lines: {len(lines)}")#pint lines number

def task5_find_word():
    word="Hello"#search the word
    with open("OSSD.txt","r") as f:
        content=f.read()#read file in string
        count=content.count(word)#count word appearance
        print(f"'{word}' appears {count} times.")#print

def task6_copy_file():
    with open("OSSD.txt","r") as src, open("copy.txt","w") as dst:
        dst.write(src.read())

def task7_replace_word():
    old_word="Hello"#word to replace
    new_word="Hi"#word to replace with
    with open("OSSD.txt","r") as f:
        content = f.read()
    content = content.replace(old_word, new_word)#replace all old words
    with open("OSSD.txt","w") as f:
        f.write(content)

def task8_read_csv():
    with open("data.csv",newline="") as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            print(row)#print row

def task9_write_csv():
    pdata = [
        {"Name": "Ahmad", "Age": 30},
        {"Name": "Bilal", "Age": 25}
    ]
    with open("output.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Age"])
        writer.writeheader()
        writer.writerows(pdata)

def task10_json_file():
    data = {"name": "Javed", "age": 30}
    with open("data.json", "w") as f:
        json.dump(data, f)
    with open("data.json", "r") as f:
        loaded = json.load(f)
        print(loaded)#print dictionary
