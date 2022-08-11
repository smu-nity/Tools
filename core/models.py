from django.db import models

YEAR_CHOICES = (("2015", "15학번"), ("2016", "16학번"), ("2017", "17학번"), ("2018", "18학번"), ("2019", "19학번"), ("2020", "20학번"), ("2021", "21학번"), ("2022", "22학번"))
DEPARTMENT_CHOICES = (("컴퓨터과학전공", "컴퓨터과학전공"), ("전기공학전공", "전기공학전공"), ("지능IOT융합전공", "지능IOT융합전공"))

class Information(models.Model):
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return f'{self.year} : {self.department}'