from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import House, Thermostat, Room, Light
from .signals import *

__all__ = [
    'HouseSerializer',
    'ThermostatSerializer',
    'RoomSerializer',
    'LightSerializer',
]

class AbstractSerializer(serializers.HyperlinkedModelSerializer):
    """
    A HyperlinkedModelSerializer which acts as a base serialzer.
    """
    class Meta:
        model = None
        ordering = ['-id']
        fields = '__all__'


class ThermostatSerializer(AbstractSerializer):
    """
    A serialzer for the Thermostat model.
    """
    class Meta:
        model = Thermostat
        fields = '__all__'

class LightSerializer(AbstractSerializer):
    """
    A serialzer for the Light model.
    """
    class Meta:
        model = Light
        fields = '__all__'

class RoomSerializer(AbstractSerializer):
    """
    A serialzer for the Room model.
    """
    #
    # NOTE: We also include nested (and related) lights
    # information when we serialze instances of the Room model.
    #
    lights = LightSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = '__all__'

class HouseSerializer(AbstractSerializer):
    """
    A serialzer for the House model.
    """
    #
    # NOTE: We also include nested (and related) thermostats and roooms
    # information when we serialze instances of the House model.
    #
    # This was one of the requirements of the assignment as it helps
    # build a complete data set for a House without having to make mulitple
    # calls for fetching individual related objects like thermostats, rooms &
    # lights.
    #
    thermostats = ThermostatSerializer(many=True, read_only=True)
    rooms = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = House
        fields = '__all__'
