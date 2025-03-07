import os
import shutil

def create_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"File {file_path} created.")

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory {directory_path} created.")
    else:
        print(f"Directory {directory_path} already exists.")
        
def move_file(src, dst):
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"Moved {src} to {dst}")
    else:
        print(f"Source file {src} does not exists.")
    
file_path = "example.txt"
content = "Hello, world!"
create_file(file_path, content)

directory_path = 'example_dir'
create_directory(directory_path)

new_file_path = os.path.join(directory_path, 'example.txt')
move_file(file_path, new_file_path)

contents = os.listdir(directory_path)
print(f"Contents of {directory_path}: ")
for item in contents:
    print(item)



    