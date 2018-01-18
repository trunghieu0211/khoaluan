from rest_framework import serializers
from cosovatchats.models import Cosovatchat

class CosovatchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosovatchat
        fields = ('id','matruong','skytuc','sokytuc','sphonghoc','sthuvien','svandong','tongdientich')
