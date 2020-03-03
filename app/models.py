from django.db import models

# Create your models here.
class ThingToDo(models.Model):
    thing = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Things to Do'

    def __str__(self):
        return self.thing
