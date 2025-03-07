
'''
---
'r': 읽기 모드
'w': 쓰기 모드 (파일이 존재하면 내용을 덮어씀)
'a': 추가 모드 (파일 끝에 내용을 추가)
'b': 바이너리 모드 (예: 'rb', 'wb')
---
'''

'''
# 파일 쓰기
with open('example.txt', 'w') as f:
    f.write("Hello, world\n")
    f.write("This is a new line.")
---   
# 한줄 씩 읽기
with open('example.txt', 'r', encoding='utf-8') as file:  
    line = file.readline()  
    while line:  
        print(line,end="")  # 파일 내용 출력 (줄 바꿈 없이)  
        line = file.readline()
# 전체 읽기
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    
# 전체를 줄 단위로 읽기
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
        
---
# 바이너리 파일 쓰기(오디오나 이미지)
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04')

# 바이너리 파일 읽기
with open('example.bin', 'rb') as file:
    data = file.read()
    print(data)
---
# csv 파일 처리
import csv
with open("example.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])     

# csv 파일 쓰기
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
---
# csv 파일 처리
import csv
with open("example.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])     

# csv 파일 쓰기
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
# Json 파일처리
import json

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# 쓰기
with open("example.json", "w") as file:
    json.dump(data, file, indent=4)
    
# 읽기
with open("example.json", "r") as file:
    data = json.load(file)
    print(data)
    
    
---

import csv

students = [
    {'name': 'Alice', 'math': 90, 'science': 85, 'english': 88},
    {'name': 'Bob', 'math': 78, 'science': 81, 'english': 92},
    {'name': 'Charlie', 'math': 95, 'science': 89, 'english': 85}
]

# CSV 파일에 학생 성적 데이터 쓰기
with open("student.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name','math','science','english'])

    writer.writeheader()
    for student in students:
        writer.writerow(student)
    
# CSV 파일에서 학생 성적 데이터 읽기
with open("student.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
    
---

# 디렉토리 내 파일 검색

import os
import glob

directory = '.'
pattern = '*.txt'

files = glob.glob(os.path.join(directory, pattern))
print(f"Text files in {directory}:")
for file in files:
    print(file)

# 경로 결합
# 경로를 결합 하려면 os.path.join(a, b)

import os

directory = "example_dir"
filename = "example.txt"

file_path = os.path.join(directory, filename)
print(f"Full file path: {file_path}")
    
---

# 절대 경로 얻기

import os

relative_path = "example.txt"
absolute_path = os.path.abspath(relative_path)

print(f"절대 경로: {absolute_path}")


'''