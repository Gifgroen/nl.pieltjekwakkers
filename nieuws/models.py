from django.db import models

# Create your models here.
class Artikel(models.Model):
    titel = models.CharField(max_length=256)
    bericht = models.TextField()
    datum = models.DateTimeField('publicatie datum')

    def __unicode__(self):
        return '(title: %s, message: %s, date %s)' % (self.titel, self.bericht, self.datum)