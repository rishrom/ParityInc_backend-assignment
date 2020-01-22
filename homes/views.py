from copy import deepcopy
from uuid import UUID

from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *
from .models import House, Thermostat, Room, Light, \
    LightStateChangeInformation, ThermostatStateChangeInformation, \
    RoomStateChangeInformation

class BaseViewSet(viewsets.ModelViewSet):
    """
    The base view set with common fields and overidden implementation of the
    partial_update and update methods that come with django-rest_framework's
    ModelViewSet.
    """
    queryset = None
    serializer_class = None
    #
    # Ensures that the APIs cannot be accessed without being authentication.
    #
    # We can enhance this to a more object based or role based authorization
    # but for now, for the scope of this assignment, basic authentication
    # (using super user via the admin panel) has been used.
    #
    permission_classes = [IsAuthenticated]

    def get_state_change_model(self):
        """
        A helper method to fetch the model which needs to be populated with
        the state change information.

        This needs to be overridden by classes inheriting from this class.
        """
        return (None, None)

    def update(self, request, *args, **kwargs):
        """
        We overridde the update method (called on the HTTP verbs PUT & PATCH)
        to keep track of changes made to any of the following models:
        Lights, Thermostats or Rooms
        """

        #
        # We pass on the 'partial' update information to the serializer if
        # we find it in the keyword-arguments.
        #
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        #
        # Store a local copy of the instance's data before it gets overwritten
        # by the incoming Request Data.
        #
        serializer_data = self.get_serializer(instance).data

        #
        # Use 'this' classes serialzer to partially (or otherwise) update the
        # instance object with the incoming Request data.
        #
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        new_state = dict(request.data.items())

        #
        # We are ony interested in the values that were updated by this
        # request and will not be storing the entire overwritten instance
        # data.
        #
        current_state = {}
        for key in new_state.keys():
            #
            # If we find a key in the new state, only then fetch the value
            # for that key in the previous state and update the
            # current_state subsequently.
            #
            value = serializer_data[key]

            #
            # UUIDs need some special handling for nested objects so we convert
            # them to string before attempting to store the data in our
            # persistance layer
            #
            value = str(value) if isinstance(value, UUID) else value
            current_state.update({
                key : value
            })

        #
        # Check if the incoming requets data is valid and continue to overwrite
        # the instance if all fields and their data types are as per
        # expectation.
        #
        serializer.is_valid(raise_exception=True)
        serializer.save()

        (state_change_model, tracked_model) = self.get_state_change_model()
        #
        # We've used a generic handler and a helper function so that we
        # DO NO REPEAT ourselves by having to write this same overridden
        # function for all the ViewSets.
        #
        #
        # NOTE: state_change_model can be None - for example we do not track
        # changes made to a house object.
        #
        if state_change_model:
            params = {
                'previous_state' : current_state,
                'next_state' : new_state,
                tracked_model : instance
            }
            state_change_instance = state_change_model(**params)
            state_change_instance.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """
        Overidding the partial_update handler so that all are updates are
        handled by the update() method.
        """
        #
        # This among other things ensures that all changes are tracked for the
        # models we do wich to track - Thermostat, Room and Light
        #
        kwargs.update({'partial' : True})
        return self.update(request, *args, **kwargs)

class HouseViewSet(BaseViewSet):
    """
    A Vietset which fetches all information related to House objects.
    """
    #
    # NOTE: We use an explicit order_by to prevent pagination throwing random
    # reults.
    #
    queryset = House.objects.all().order_by('-id')
    serializer_class = HouseSerializer

class RoomViewSet(BaseViewSet):
    """
    A Vietset which fetches all information related to Room objects.
    """
    #
    # NOTE: We use an explicit order_by to prevent pagination throwing random
    # reults.
    #
    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSerializer
    def get_state_change_model(self):
        #
        # We overridde the base classes' method to inform the update()
        # that changes to this class will be tracked using the
        # RoomStateChangeInformation model.
        #
        return (RoomStateChangeInformation, 'room')

class ThermostatViewSet(BaseViewSet):
    """
    A Vietset which fetches all information related to Thermostat objects.
    """
    #
    # NOTE: We use an explicit order_by to prevent pagination throwing random
    # reults.
    #
    queryset = Thermostat.objects.all().order_by('-id')
    serializer_class = ThermostatSerializer

    def get_state_change_model(self):
        #
        # We overridde the base classes' method to inform the update()
        # that changes to this class will be tracked using the
        # ThermostatStateChangeInformation model.
        #
        return (ThermostatStateChangeInformation, 'thermostat')

class LightViewSet(BaseViewSet):
    """
    A Vietset which fetches all information related to Ligt objects.
    """
    #
    # NOTE: We use an explicit order_by to prevent pagination throwing random
    # reults.
    #
    queryset = Light.objects.all().order_by('-id')
    serializer_class = LightSerializer

    def get_state_change_model(self):
        #
        # We overridde the base classes' method to inform the update()
        # that changes to this class will be tracked using the
        # LightStateChangeInformation model.
        #
        return (LightStateChangeInformation, 'light')
