# Suppose you are a teacher, and you have different student records containing id and
# marks list in each student where student have taken different number of subjects. You
# have to store data and to compute average marks of each student and display
# Expected output
# {1: [23, 45, 50], 2: [34, 45]}
# {1: 39.333333333333336, 2: 39.5}

student_records = {
    1: [22, 45, 50],
    2: [34, 45, 45, 90]
}
average_marks = {}
for student_id, marks in student_records.items():
    total_marks = sum(marks)
    average = total_marks / len(marks)
    average_marks[student_id] = average
print("Student Records:")
print(student_records)
print("Average Marks:")
print(average_marks)
