from django.db import models

# Create your models here.
class Reactie(models.Model):
    naam = models.CharField(max_length=200)
    bericht = models.TextField()
    datum = models.DateTimeField()

    def __unicode__(self):
        return "%s | %s | %s" % (naam, datum, bericht)