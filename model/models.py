from django.db import models
from datetime import date


class Language(models.Model):
    name = models.CharField('Язык', max_length=150)
    description = models.TextField('Описание')
    level_learning = models.PositiveSmallIntegerField('Уровень изучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Tools(models.Model):
    name = models.CharField('Инструмент', max_length=150)
    description = models.TextField('Описание')
    level_learning = models.PositiveSmallIntegerField('Уровень изучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'


class Libraries(models.Model):
    name = models.CharField('Библиотека', max_length=150)
    description = models.TextField('Описание')
    level_learning = models.PositiveSmallIntegerField('Уровень изучения')
    language = models.ForeignKey(to=Language, on_delete=models.PROTECT, verbose_name='Языки',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'


class Projects(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    url_to_git = models.URLField(verbose_name='Ссылка на гит')
    url_to_test = models.URLField(verbose_name='Ссылка на проект для тестирования')
    date_start_project = models.DateField(default=date.today)
    languages = models.ManyToManyField(Language, verbose_name='Языки')
    libraries = models.ManyToManyField(Libraries, verbose_name='Бибилиотеки')
    tools = models.ManyToManyField(Tools, verbose_name='Инструменты')
    image = models.ImageField('Изображения проекта', upload_to='projects/')
    future_changes = models.TextField('Будущие изменения проекта')
    slug_project = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

# Create your models here.
class FeedBack(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя отправителя')
    email = models.EmailField(max_length=255, verbose_name='Email отправителя')
    message = models.TextField(verbose_name='Текст сообщения')
    time_create = models.DateField(default=date.today)
    ip_adress = models.GenericIPAddressField(verbose_name='Ip=adress отправителя')

    class Meta:
         verbose_name = 'Обратная связь'
         verbose_name_plural = 'Обратная связь'


    def __str__(self):
        return f'Вам письмо от {self.name}'