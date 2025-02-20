'''
Sources:

listdir(): https://www.geeksforgeeks.org/python-os-listdir-method/
  *this returns all files and folders in a specified folder, it returns
     them conveniently into a list

join(): https://www.geeksforgeeks.org/python-os-path-join-method/
  *this joins all the components of a path together for you and 
     helpfully adds the correct / or \ based on what system you're on

splitext(): https://www.geeksforgeeks.org/python-os-path-splitext-method/
  *splits a path name into the root and extension (the extension is just
    the file ending like .txt, .png, .py)

rename(): https://www.geeksforgeeks.org/python-os-rename-method/
  *two parameters: old file path, new file path; let's us rename files
'''


from PIL import Image
import os
import random
import csv

def renumber_files():
    folder_path = r"C:\Users\Chelsea\Downloads\Rorschach Images"
    files = os.listdir(folder_path)
    num = 1

    for file in files:
        old_name = os.path.join(folder_path, file) #creates full path
        file, ext = os.path.splitext(old_name) #splits to preserve extension
        file_name = f"{num}{ext}" #creates new file name with extension
        new_name = os.path.join(folder_path, file_name) #joins with new path
        os.rename(old_name, new_name) #renames file
        num += 1

def choose_image():
    folder_path = r"C:\Users\Chelsea\Downloads\Rorschach Images"
    file = random.choice(os.listdir(folder_path)) 
    image_path = os.path.join(folder_path, file) 
    image = Image.open(image_path)
    image.show() 
    return file

def writing_to_file():
    csv_file = open("rorschach.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["subject name", "image name", "user response"])

    used_files = []
    user = input("What is your name?").lower()
    num = 5

    for i in range(num):
        image_name = choose_image()
        if image_name not in used_files:
            response = input("What does this image make you think of? Please describe in no more than two words")
            response = response.lower()

            csv_writer.writerow([user, image_name, response])
            used_files.append(i)
        else:
            num += 1

    csv_file.close()

writing_to_file()