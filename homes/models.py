import uuid
from model_utils import Choices

from django.contrib.postgres.fields import JSONField
from django.db import models

__all__ = [
    'House',
    'Thermostat',
    'Light',
    'Room',
]

class NameBaseModel(models.Model):
    """
    Base model with common fields.
    """
    name = models.CharField(max_length=200, help_text='Name')

    #
    # We use the following DateTimeFields to keep track of changes made to
    # individual objects.
    #
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created At')
    updated_at = models.DateTimeField(auto_now=True,
                                      help_text='Updated At')
    #
    # We use the UUIDField instead of the simplistic auto increment integer
    # which comes out of the box with Django.
    #
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, help_text='ID')
    class Meta:
        abstract = True

class House(NameBaseModel):
    """
    Store details about a house.
    """
    name = models.CharField(max_length=200, help_text='Name of the house.')
    def __str__(self):
        return self.name


class Thermostat(NameBaseModel):
    """
    Store thermostat data.
    """
    house = models.ForeignKey(House, related_name='thermostats',
                              on_delete=models.CASCADE,
                              help_text='Related house.')
    MODES = Choices(
        ('off', 'Off'),
        ('fan', 'Fan'),
        ('auto', 'Auto'),
        ('cool', 'Cool'),
        ('heat', 'Heat'))

    mode = models.CharField(choices=MODES, default=MODES.off,
                            max_length=5,
                            help_text='Current mode of the thermostat.')

    current_temperature = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        help_text='Current temperature at the thermostat.')

    temperature_set_point = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        help_text='Temperature set point.')

    def __str__(self):
        return self.name


class Room(NameBaseModel):
    """
    Store room information.
    """
    house = models.ForeignKey(House, related_name='rooms',
                              on_delete=models.CASCADE,
                              help_text='Related house.')
    current_temperature = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        help_text='Current temperature at the thermostat.')

    def __str__(self):
        return self.name


class Light(NameBaseModel):
    """
    Store Light information.
    """
    room = models.ForeignKey(Room, related_name='lights',
                             on_delete=models.CASCADE,
                             help_text='Related room.')
    STATE = Choices(
        ('on', 'On'),
        ('off', 'Off'))
    state = models.CharField(choices=STATE,
                             default=STATE.off, max_length=3,
                             help_text='Current state of the light.')

    def __str__(self):
        return self.name

class StateChangeBaseModel(models.Model):
    """
    Base model to store the state change information for Ligts, Thermostats
    and Rooms.
    """
    #
    # We use the following DateTimeFields to keep track of changes made to
    # individual objects.
    #
    created_at = models.DateTimeField(auto_now_add=True,
                                      help_text='Created At')
    updated_at = models.DateTimeField(auto_now=True,
                                      help_text='Updated At')
    #
    # We use the UUIDField instead of the simplistic auto increment integer
    # which comes out of the box with Django.
    #
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, help_text='ID')
    #
    # We use PostgreSQL's native JSON implementation to store the current and
    # (to be changed) new state of an object.
    #
    # Using JSONField gives us the flexibility to scale and adapt this base
    # model to any other model in our application.
    #
    # What it also allows us to do is to only keep track of changed fields
    # (if required) which prevents us from resorting to finding needle in a
    # haystack while tracking state changes over time.
    #
    previous_state = JSONField()
    next_state = JSONField()

    class Meta:
        abstract = True

class LightStateChangeInformation(StateChangeBaseModel):
    """
    Model to store changes made to a Light object over time.
    """
    light = models.ForeignKey(Light, related_name='lights',
                             on_delete=models.CASCADE,
                             help_text='Light Change Information')
    def __str__(self):
        return self.name

class ThermostatStateChangeInformation(StateChangeBaseModel):
    """
    Model to store changes made to a Thermostat object over time.
    """
    thermostat = models.ForeignKey(Thermostat, related_name='thermostats',
                             on_delete=models.CASCADE,
                             help_text='Thermostat State Change Information')
    def __str__(self):
        return self.name

class RoomStateChangeInformation(StateChangeBaseModel):
    """
    Model to store changes made to a Room object over time.
    """
    room = models.ForeignKey(Room, related_name='rooms',
                             on_delete=models.CASCADE,
                             help_text='Room State Change Information')
    def __str__(self):
        return self.name
