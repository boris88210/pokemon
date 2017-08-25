from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile

class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return password2
    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(user.password)
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    nickname = forms.CharField(label='暱稱', max_length=50)
    friendCode = forms.CharField(label='3DS-FC', max_length=20)
    email = forms.CharField(label='E-mail', max_length=50)
    
    class Meta:
        model = UserProfile
        fields = ['nickname', 'friendCode', 'email']
