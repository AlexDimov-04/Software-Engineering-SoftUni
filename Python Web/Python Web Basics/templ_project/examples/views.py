import datetime
import random
from django.shortcuts import render

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age
    
some_student = Student('Alex', 18)

def index(request):
    context = {
        "title": "Home",
        "random": random.randrange(1, 100),
        'nested': {
            'second': 'second value',
        },
        'student': some_student,
        'students': ['Aria', 'Emanuela', 'Erik'],
        'now': datetime.date.today() 
    }

    return render(request, "examples/index.html", context=context)
