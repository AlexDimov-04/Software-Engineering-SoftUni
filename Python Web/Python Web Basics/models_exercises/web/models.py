from enum import Enum
from django.db import models

# class EmployeeLevel(Enum):
#     JUNIOR = 'Junior',
#     REGULAR = 'Regular',
#     SENIOR = 'Senior'


class Project(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=10, unique=True)
    deadline = models.DateField()


class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f"Id: {self.pk}; Name: {self.name}"


class Employee(models.Model):
    LEVEL_JUNIOR = "Junior"
    LEVEL_REGULAR = "Regular"
    LEVEL_SENIOR = "Senior"

    LEVELS = [
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    ]

    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=35, null=True)
    last_name = models.CharField(max_length=50)
    level = models.CharField(max_length=13, choices=LEVELS)
    age = models.IntegerField(default=0)
    text = models.TextField(unique=True)
    is_virgin = models.BooleanField()
    years_of_experience = models.PositiveIntegerField()
    hair_color = models.CharField(max_length=10)

    is_full_time = models.BooleanField(null=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    project = models.ManyToManyField(Project)

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        return f"Id: {self.pk}; Name: {self.full_name}"

class NullBlankDemo(models.Model):
    blank = models.IntegerField(blank=True, null=False)

    null = models.IntegerField(blank=False, null=True)

    blank_null = models.IntegerField(blank=True, null=True)

    default = models.IntegerField(blank=False, null=False)


