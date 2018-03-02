from django.db import models

# Create your models here.
class SetNo(models.Model):
    setno = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.setno)

class Question(models.Model):
    setno = models.ForeignKey(SetNo, on_delete=models.CASCADE)
    ques_text = models.TextField(max_length=3000)
    ans_text = models.TextField(max_length=1000)

    def __str__(self):
        return "Set no: %s\nQuestion: %s\nAnswer: %s".format(self.setno, self.ques_text, self.ans_text)

class Contestant(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    points = models.IntegerField(default=0)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    setno = models.ForeignKey(SetNo, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "Username: {0}\n".format(self.username)