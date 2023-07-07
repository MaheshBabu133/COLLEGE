from rest_framework import serializers

from app.models import *
class CollegeMS(serializers.ModelSerializer):
    class Meta:
        model=College
        fields="__all__"