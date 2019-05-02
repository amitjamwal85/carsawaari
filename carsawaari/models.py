from django.db import models

class TblCities(models.Model):
    name = models.CharField(max_length=30)
    state_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_cities'

