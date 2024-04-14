student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


import pandas

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# DataFrame
score_df = pandas.DataFrame(student_dict)
print("\n", score_df)

for (index, row) in score_df.iterrows():
    print(row.student)