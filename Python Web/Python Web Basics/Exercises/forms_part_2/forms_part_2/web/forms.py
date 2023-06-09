from django import forms
from forms_part_2.web.models import ToDo
from forms_part_2.web.validators import ValueInRangeValidator
from forms_part_2.web.validators import validate_text 
from django.core.validators import MinValueValidator

class ToDoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(validate_text,),
    )
    is_done = forms.BooleanField(
        required=False
    )
    priority = forms.IntegerField(
        validators=(ValueInRangeValidator(1, 10), MinValueValidator),
    )

    def clean_priority(self):
        raise forms.ValidationError('Erorr!!!!')
    
class ToDoCreateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'