from django.db import models
import django

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=100, default='Default_Name')
    surname = models.CharField(max_length=100, default='Default_Surname')
    user_email = models.CharField(max_length=120, unique=True)
    password = models.CharField(max_length=70)

    def __str__(self):
        return self.name + ' - ' + self.surname + ' - ' + self.user_email + ' - ' + self.password

class Product(models.Model):

    product_name = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name + ' - ' + str(self.owner)

class Lesson(models.Model):

    name = models.CharField(max_length=150, unique=True)
    link = models.CharField(max_length=1000)
    duration = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.link + ' - ' + str(self.duration) + ' - ' + str(self.product_id)

class Lesson_view(models.Model):

    CHOICE_STATUS = (
        ('Просмотрено', 'Просмотрено'),
        ('Не просмотрено', 'Не просмотрено')
    )

    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date_time_field = models.DateTimeField(null=False, default=django.utils.timezone.now)
    viewed_time = models.IntegerField()
    status = models.CharField(max_length=20, choices=CHOICE_STATUS, default='Не просмотрено')

    def save(self, *args, **kwargs):
        '''Вычисляем процент просмотра'''
        percentage_viewed = (self.viewed_time / self.lesson_id.duration) * 100

        if percentage_viewed >= 80:
            self.status = 'Просмотрено'
        else:
            self.status = 'Не просмотрено'

        super(Lesson_view, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.lesson_id) + ' - ' + ' - ' + str(self.date_time_field) + ' - ' + str(self.viewed_time) + ' - ' + self.status






