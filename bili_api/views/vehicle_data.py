from rest_framework.generics import ListAPIView
from ..serializers.vehicle_data import *
from ..models.vehicle_data import *
################################################################################

# class VehicleBodyListView(ListAPIView):
#     queryset = VehicleBody.objects.all()
#     serializer_class = VehicleBodyListSerializer
#
#
# class VehicleTransmissionListView(ListAPIView):
#     queryset = VehicleTransmission.objects.all()
#     serializer_class = VehicleTransmissionListSerializer
#
#
# class VehicleModelListView(ListAPIView):
#     queryset = VehicleModel.objects.all()
#     serializer_class = VehicleModelListSerializer
#
#
# class VehicleMakeListView(ListAPIView):
#     queryset = VehicleMake.objects.all()
#     serializer_class = VehicleMakeListSerializer
#
# class VehicleFuelListView(ListAPIView):
#     queryset = VehicleFuel.objects.all()
#     serializer_class = VehicleFuelListSerializer


class VehiclePropListView(ListAPIView):
    def get_serializer_class(self):
        feature = self.kwargs['feature']
        print(feature)
        if feature == "make":
            return VehicleMakeListSerializer
        elif feature == "model":
            return VehicleModelListSerializer
        elif feature == "body":
            return VehicleBodyListSerializer
        elif feature == "fuel":
            return VehicleFuelListSerializer
        elif feature == "transmission":
            return VehicleTransmissionListSerializer

    def get_queryset(self):
        feature = self.kwargs['feature']
        print(feature)

        if feature == "make":
            return VehicleMake.objects.all()
        elif feature == "model":
            return VehicleModel.objects.all()
        elif feature == "body":
            return VehicleBody.objects.all()
        elif feature == "fuel":
            return VehicleFuel.objects.all()
        elif feature == "transmission":
            return VehicleTransmission.objects.all()
