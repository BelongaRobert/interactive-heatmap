from django.db import models
from django.db.models import DecimalField, TextField, CharField

# Create your models here.
class ipv4 (models.Model):
    network = CharField(max_length=20)
    geoname_id = TextField()
    registered_country_geoname_id = TextField()
    represented_country_geoname_id = TextField()
    is_anonymous_proxy = TextField()
    is_satellite_provider = TextField()
    postal_code = TextField()
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)
    accuracy_radius = TextField()

    def __str__(self):
        return self.name


"""class MycsvModel (CsvModel):
    network = IgnoredField()
    geoname_id = IgnoredField()
    registered_country_geoname_id = IgnoredField()
    represented_country_geoname_id = IgnoredField()
    is_anonymous_proxy = IgnoredField()
    is_satellite_provider = IgnoredField()
    postal_code = IgnoredField()
    latitude = DecimalField()
    longitude = DecimalField()
    accuracy_radius = IgnoredField()

    def __str__(self):
        return self.name
 """