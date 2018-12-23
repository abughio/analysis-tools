from django.db import models


class Usecase(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    preConditions = models.CharField(max_length=2000)
    postConditions = models.CharField(max_length=2000)

    def __str__(self):
        return  self.name

class Scenario(models.Model):
    SCENARIO_TYPES = (
        ("Normal Flow", "Normal Flow"),
        ("Alternate Flow", "Alternate Flow"),
        ("Exception Flow", "Exception Flow")
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=SCENARIO_TYPES)
    usecase = models.ForeignKey(Usecase,on_delete=models.CASCADE,related_name="scenarios")

    def __str__(self):
        return self.type.__str__()+" - "+self.name.__str__()

class Step(models.Model):
    stepNo = models.IntegerField()
    description = models.CharField(max_length=500)
    scenario = models.ForeignKey(Scenario,on_delete=models.CASCADE,related_name="steps")

    def __str__(self):
        return self.stepNo.__str__()+". "+self.description.__str__()
