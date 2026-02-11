from django import forms
from .models import Employee,Course,Teacher,Productf,Studentf 

#employee form
#modelForm -->it will create form using model fileds
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #[name,age,salary,joiningDate,post]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__' 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productf
        fields = '__all__' 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Studentf
        fields = '__all__' 