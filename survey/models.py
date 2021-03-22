from django.db import models

# Create your models here.
class Survey(models.Model):
    label = models.IntegerField(default=0)
    image_path = models.CharField(max_length=100)
    labeled_by = models.CharField(max_length=100)

    def __str__(self):
        return self.image_path+" "+str(self.label)+" "+self.labeled_by