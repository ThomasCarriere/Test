from django.db import models

class TicketIncident(models.Model):
    pub_date = models.DateTimeField('Date de publication')
    Description = models.CharField(max_length=500)
    Mail = models.CharField(max_length=100)

    def __str__(self):
        return self.Description
    
