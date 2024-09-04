from django import forms
from .models import Category, Meal, Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'phone', 'cv')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'cv': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'CV'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Получаем текущего пользователя из kwargs
        self.vacancy = kwargs.pop('vacancy', None)
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['cv'].required = False

    def save(self, commit=True):
        employee = super(EmployeeForm, self).save(commit=False)
        if self.user:
            employee.user = self.user
        if self.vacancy:
            employee.vacancy = self.vacancy
        if commit:
            employee.save()
        return employee


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

