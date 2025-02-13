from django.db import models

class UserLocation(models.Model):
    ip_address = models.GenericIPAddressField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.latitude}, {self.longitude}"
