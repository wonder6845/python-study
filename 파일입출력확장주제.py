with open('example.txt', 'r+') as file:
    content = file.read()
    file.write('Additional content')
import os
os.chmod('example.txt', 0o644)