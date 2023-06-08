from django.db import models


class place(models.Model):
    objects = None
    name_place = models.CharField(max_length=100, blank=False)
    name_region = models.CharField(max_length=100, blank=False)
    name_country = models.CharField(max_length=100, blank=False)
    location = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name_place} {self.name_region} {self.name_country}'


class note(models.Model):
    person_do_it = models.CharField('Имя пользователя', max_length=40)
    title = models.CharField('Название', max_length=70)
    note = models.TextField('Текст записи')

    def __str__(self):
        return self.title
