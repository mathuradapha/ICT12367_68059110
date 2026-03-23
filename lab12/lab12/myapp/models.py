from django.db import models

class Person(models.Model):

    citizen_id = models.CharField(max_length=13)   # รหัสประชากร
    name = models.CharField(max_length=100)        # ชื่อจริง
    nickname = models.CharField(max_length=50)     # ชื่อเล่น
    age = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name