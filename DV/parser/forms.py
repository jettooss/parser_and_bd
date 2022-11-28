from django import  forms
from .models import Institutes,timetable



class InstitutesForm(forms.ModelForm):


    class Meta:
        model=Institutes
        fields=(
            'number_Institute',
            'group',
            'id_group',
        )
        widgets={

            'group':forms.TextInput,
            'id_group':forms.TextInput,
        }
class timetableForm(forms.ModelForm):


    class Meta:
        model=timetable
        fields=(

            'number_week',
            'day_week',
            'lesson_score',
            'time',
            'cabinet',
            'object',
            'teacher',
            'idd',
        )
        widgets={

            'number_week':forms.TextInput,
            # 'id_group':forms.TextInput,
        }