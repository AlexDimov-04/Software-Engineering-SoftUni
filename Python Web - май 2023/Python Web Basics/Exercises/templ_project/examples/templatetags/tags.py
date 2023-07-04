from django import template

register = template.Library()

@register.simple_tag()
def show_student_info(student):
    return f"Name: {student.name}, Age: {student.age}"