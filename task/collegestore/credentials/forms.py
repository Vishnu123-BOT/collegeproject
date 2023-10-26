from django import forms
from.models import Student,Course
from collegestoreapp.models import Department
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['course'].queryset = Course.objects.none()

    if 'department' in self.data:
        try:
            department_id=int(self.data.get('department'))
            self.fields['course'].queryset=Course.objects.filter(department_id=department_id).all()
        except(ValueError,TypeError):
            pass
    elif self.instance.pk:
        self.fields['course'].queryset=self.instance.department.course_set.all()