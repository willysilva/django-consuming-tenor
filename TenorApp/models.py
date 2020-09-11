from django.db import models

# Create your models here.
class Tenor(models.Model):
    id= models.IntegerField(auto_created=False, primary_key=True, serialize=False, verbose_name='ID')
    votes=models.IntegerField(default=0)
    downvotes=models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
