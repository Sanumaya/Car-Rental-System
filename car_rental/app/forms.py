from django.forms import PasswordInput, forms

from app.models import UserDetail

class UserSignInForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    class Meta:
        # fields = "__all__" - to load all fields
        fields = ("first_name", "middle_name", "last_name", "contact", "email", "password") # selective fields
        model = UserDetail

class UserLoginForm(forms.ModelForm):
    class Meta:
        fields = ("email", "password")
        model = UserDetail
