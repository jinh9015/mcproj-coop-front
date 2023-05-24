from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# django.contrib.auth.forms 패키지의 UserCreationForm 클래스 상속, email 속성 추가
# UserCreationForm 속성 (username, password1, password2)
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")