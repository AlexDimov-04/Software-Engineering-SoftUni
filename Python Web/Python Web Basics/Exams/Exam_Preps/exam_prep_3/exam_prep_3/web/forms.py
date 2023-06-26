from django import forms
from exam_prep_3.web.models import Profile, Car


class ProfileBaseForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class ProfileCreateForm(ProfileBaseForm):
    pass

class ProfileEditForm(ProfileBaseForm):
    password = forms.CharField()

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']

class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            Profile.objects.all().delete()
        return self.instance

class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CarCreateForm(CarBaseForm):
    pass

class CarEditForm(CarBaseForm):
    pass

class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
     if commit:
        self.instance.delete()
     return self.instance