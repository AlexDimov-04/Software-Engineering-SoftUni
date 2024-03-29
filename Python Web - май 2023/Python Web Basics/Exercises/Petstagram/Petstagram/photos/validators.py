from django.core.exceptions import ValidationError

def image_size_validator_5mb(image_object):

    max_size = 5 * 1024 * 1024

    if image_object.size > max_size:
        return ValidationError('Image size can no be larger than 5MB')

