from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", initial="Bob", help_text="Maybe, Bob?");
    age = forms.IntegerField(label="Возраст", widget=forms.PasswordInput);
    field_order = ["age", "name"]
