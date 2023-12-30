from django.db import models

from django.db import migrations, models


class cotegory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class basedatel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    value = models.PositiveIntegerField(default=0)
    type = models.ForeignKey(to=cotegory, on_delete=models.PROTECT)
    coin = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    

    
class baton(models.Model):
    name = models.CharField(max_length=128, unique=True)
    value = models.PositiveIntegerField(default=0)
    type = models.ForeignKey(to=cotegory, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    

"""
#Бля не знаю нахуя это
from appueu.models import cotegory
category = cotegory(name="ПИЗДА", type="ПИЗДЕЦ")
category.save()


#Чтение и создание
from appueu.models import cotegory
category = cotegory.objects.get(id=1)

cotegory.objects.create(name="ПИСЮНЧИК")


"""








