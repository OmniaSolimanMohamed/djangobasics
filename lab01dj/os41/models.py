from django.db import models
class Track(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length = 50, null=True, default="unknown")
    lname = models.CharField(max_length = 50, null=True, default="unknown")
    age = models.IntegerField()
    student_track = models.ForeignKey(Track, on_delete=models
    .CASCADE)
    def __str__(self):
        return self.fname + ' ' + self.lname


    def is_grad (self):
        if self.age >20:
            return True
        else:
            return False

    is_grad.short_description = 'Posr grad std'
    is_grad.boolean = True