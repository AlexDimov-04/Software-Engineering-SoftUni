from django.core.exceptions import ValidationError

def first_char_validator(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")
    
def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Fruit name should contain only letters!")