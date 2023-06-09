import datetime
import random
from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


some_student = Student("Alex", 18)


def index(request):
    context = {
        "title": "Home",
        "random": random.randrange(1, 100),
        "nested": {
            "second": "second value",
        },
        "student": some_student,
        "students": ["Aria", "Emanuela", "Erik", "Erik"],
        "students_second": [],
        "now": datetime.date.today(),
        "numbers": [1, 2, 3, 4, 5],
        'letters': ['a', 'e', 'i', 'o', 'g', 'r', 'b', 'w', 'b', 'p'],
        'students_obj': [
            Student('Lili', 23),
            Student('Moni', 20),
            Student('Yavor', 30)
        ],
        'logged_in': True
    }

    return render(request, "examples/partials/index.html", context=context)


def contact_view(request, name):
    return redirect("index")


def about_view(request):
    return render(request, 'examples/partials/about.html')