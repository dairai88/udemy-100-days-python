"""day 26 list comprehension and the NATO alphabet"""
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (key, value) in student_data_frame.items():
    print(key)
    print(value)
    print("----------")

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student, row.score)
    print("---------------------")
