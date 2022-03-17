from django.db import models
from django.utils import timezone
from django.urls import reverse


# create a function that can handle deadlines
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


# create a class that represents a database model
class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    # create a method that returns the URL for the particular data item,
    # to avoid hard-coding the URL and its parameters
    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_data = models.DateTimeField(auto_now_add=True)
    due_time = models.DateTimeField(default=one_week_hence)
    # the ForeigKey links the ToDoItem back to its ToDoList
    # this is a one-to-many relationship
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('item-update',
                       args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return f'{self.title}: due {self.due_time}'

    # a Meta class allows you to set some useful options(ordering for ToDoItem records
    class Meta:
        ordering = ["due_date"]
