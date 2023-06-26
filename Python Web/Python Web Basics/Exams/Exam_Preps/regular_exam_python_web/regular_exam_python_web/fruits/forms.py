from django import forms
from regular_exam_python_web.fruits.models import Profile, Fruits

class ProfileBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),  
            "password": forms.PasswordInput(
                 attrs={
                     'placeholder':'Password',
                     'autocomplete': 'off',
                     'data-toggle': 'password'
                }
            )
        }

class CreateProfileForm(ProfileBaseForm):
    pass

class EditProfileForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = " First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['image_url'].label = "Image URL"
        self.fields['age'].label = "Age"

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image_url', 'age']

class DeleteProfileForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Fruits.objects.all().delete()
            Profile.objects.all().delete()
        return self.instance

class FruitBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Fruits
        fields = '__all__'

        widgets = {
                'name': forms.TextInput(
                    attrs={
                        'placeholder': 'First Name'
                    }
                ),
                'image_url': forms.TextInput(
                    attrs={
                        'placeholder': 'Fruit Image URL',
                    }
                ),
                'description': forms.Textarea(
                    attrs={
                        'placeholder': 'Fruit Description'
                    }
                    
                ),
                'nutrition': forms.Textarea(
                    attrs={
                        'placeholder': 'Nutrition Info'
                    }
                ),
            }

class FruitCreateForm(FruitBaseForm):
    pass

class FruitEditForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['image_url'].label = "Image URL"
        self.fields['description'].label = "Description"
        self.fields['nutrition'].label = "Nutrition"
        
class FruitDeleteForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['image_url'].label = "Image URL"
        self.fields['description'].label = "Description"

        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
     if commit:
        self.instance.delete()
     return self.instance
    
    class Meta:
        model = Fruits
        fields = ['name', 'image_url', 'description']
