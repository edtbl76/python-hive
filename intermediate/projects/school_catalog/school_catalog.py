#!/usr/bin/env python3

class School:
    def __init__(self, name, level, number_of_students):
        self.name = name
        self.level = level
        self.number_of_students = number_of_students

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_number_of_students(self):
        return self.number_of_students

    def set_number_of_students(self, number_of_students):
        self.number_of_students = number_of_students

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.number_of_students} students."


class PrimarySchool(School):

    # We only need to define the members that are specific to THIS class.
    # name, number of students and level are all inherited from the parent
    def __init__(self, name, number_of_students, pickup_policy):
        super().__init__(name, "primary", number_of_students)
        self.pickup_policy = pickup_policy

    # Members are inherited, so we only need one getter
    def get_pickup_policy(self):
        return self.pickup_policy

    def __repr__(self):
        parent = super().__repr__()
        return parent + f" The pickup policy is {self.pickup_policy}"




# Driver Code
# SCHOOL
school = School("Westford Academy", "high", 1000)
print(school)
print(school.get_name())
print(school.get_level())
school.set_number_of_students(2000)
print(school.get_number_of_students())

# PRIMARY
florin = PrimarySchool("Florin", 300, "Pickup Allowed")
print(florin.get_pickup_policy())
print(florin)