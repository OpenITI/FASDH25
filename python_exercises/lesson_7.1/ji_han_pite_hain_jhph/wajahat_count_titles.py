import os

folder_path = "C:/Users/Dell/Downloads/FASDH25/python_exercises/lesson_7.1/ji_han_pite_hain_jhph/"

# Print all files in the directory
print("Files in directory:", os.listdir(folder_path))
import os

folder_path = "C:/Users/Dell/Downloads/FASDH25/python_exercises/lesson_7.1/ji_han_pite_hain_jhph/"
filename = "1382ShawkatThanwi.JiHanPitayHayn.FASDH2025013-urd1"

file_path = os.path.join(folder_path, filename)

try:
    with open(file_path, 'r', encoding='utf8') as file:
        content = file.readlines()
    print("File loaded successfully!")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
