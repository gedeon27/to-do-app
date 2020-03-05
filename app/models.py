from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class UserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # tasks_stored = models.ManyToManyField(Task)

    def __str__(self):
        return self.user.username + "'s to-do-list'"


class Task(models.Model):
    thing = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    its_list = models.ForeignKey(UserList, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Things to Do'

    def __str__(self):
        return self.thing
