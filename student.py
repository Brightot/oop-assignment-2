# student.py

# This class represents a student
# Each student has an ID, a name and a dictionary of grades

class Student:

    def __init__(self, student_id, name):
        # storing student id
        self._student_id = student_id

        # storing student name
        self._name = name

        # dictionary to store subject and grade
        # example: {"Math": 85}
        self._grades = {}

    # this method adds a subject and grade
    def add_grade(self, subject, grade):

        # if the subject is already stored, do nothing
        if subject in self._grades:
            return False

        # otherwise add the grade
        self._grades[subject] = grade
        return True

    # this method prints student information nicely
    def __str__(self):
        return f"{self._student_id} - {self._name} - {self._grades}"