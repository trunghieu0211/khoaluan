from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class Cosovatchat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    matruong = models.CharField(max_length=10, blank=True, default='')
    skytuc = models.FloatField(default=0)
    sokytuc = models.FloatField(default=0)
    sphonghoc = models.FloatField(default=0)
    sthuvien = models.FloatField(default=0)
    svandong = models.FloatField(default=0)
    tongdientich = models.FloatField(default=0)

    class Meta:
        ordering = ('created',)

# from cosovatchats.models import Cosovatchat
# from cosovatchats.serializers import CosovatchatSerializer
# cs = Cosovatchat(matruong='BKA')
# cs.save()
# ser = CosovatchatSerializer(cs)
# ser.data