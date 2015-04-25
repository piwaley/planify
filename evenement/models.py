from django.db import models

# Create your models here.


class Evenement(models.Model):
    nom = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField()
    date_event = models.DateField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    duree_event = models.CharField(max_length=256, null=False, blank=False)
    lieu = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    adresse = models.TextField()
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True, auto_now_add=True)

    def _duree(self):
        return 'Cet evenement debutera le %s pour finir le %s' \
            % (self.date_debut, self.date_fin)
    duree = property(_duree)

    def __unicode__(self):
        return '%s' % self.nom


class Task(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    deadline = models.DateField()
    evenement = models.ForeignKey(Evenement)
    description = models.TextField()

    def _describe_task(self):
        return "%s need to be completed before %s for %s event" \
            % (self.title, self.deadline, self.evenement.nom)
    describe_task = property(_describe_task)

    def __unicode__(self):
        return "%s" % self.nom

