from django.core.exceptions import ValidationError

def validate_phone(value):
    if value is None:
        raise ValidationError('Phone cannot be `None`')
    if not value.startswith('0') and not value.startswith('+'):
        raise ValidationError("Phone must start with '0' or '+' ")