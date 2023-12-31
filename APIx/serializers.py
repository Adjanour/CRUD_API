from rest_framework import serializers
from APIx.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('Id','Name')
        many = True