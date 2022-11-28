from django.db import models

class Institutes(models.Model):
    number_Institute = models.TextField(
        verbose_name='институт'
    )
    group=models.TextField(
        verbose_name='номер',

    )
    id_group= models.TextField(
        verbose_name='id',
        primary_key=True,
    )
    def __str__(self):
        return f'{self.id_group}'
    class Meta:
        verbose_name='группа'
        verbose_name_plural = 'группы'

class timetable(models.Model):

        number_week= models.TextField(
         verbose_name='день',
        )
        day_week=models.TextField(
        verbose_name='день неделе'
        )
        lesson_score=models.TextField(
        verbose_name='пара'
        )
        time=models.TextField(
         verbose_name='время'
        )
        cabinet=models.TextField(
         verbose_name='кабинет'
        )
        object=models.TextField(
         verbose_name='предмет'
        )
        teacher=models.TextField(
         verbose_name='преподаватель'
        )
        idd = models.ForeignKey(Institutes, on_delete=models.PROTECT,null=True)

        def __str__(self):
            return f'#{self.pk}/{self.number_week}/{self.idd}'
        class Meta:
            verbose_name = 'расписание'
            verbose_name_plural = 'расписание'

