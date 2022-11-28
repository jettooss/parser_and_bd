from django.contrib import admin
from .models import Institutes,timetable
from .forms import InstitutesForm,timetableForm


@admin.register(Institutes)
class Institutes_admin(admin.ModelAdmin):
    # list_number_Institute=('number_Institute','group','id_group')
    list_display = ('number_Institute','group','id_group')
    search_fields = ('group','id_group')
    list_display_links = ('id_group',)

    # form=InstitutesForm
@admin.register(timetable)
class timetable_admin(admin.ModelAdmin):
        list_display = ( 'pk','number_week', 'day_week', 'lesson_score', 'time', 'cabinet', 'object', 'teacher','idd')
        list_display_links = ('pk',)
        search_fields = ('idd', )
        # form = timetableForm
# Register your models here.
