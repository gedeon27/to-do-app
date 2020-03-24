from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    thing = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    its_list = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Things to Do'

    def __str__(self):
        return self.thing


class UserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks_listed = models.ManyToManyField(Task, related_name='tasks_listed')

    def __str__(self):
        return self.user.username + "'s to-do-list'"
