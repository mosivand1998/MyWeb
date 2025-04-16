from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.utils import timezone >>> has more applicable functions related to timezones
import timezones   # is for python not django
from rest_framework.permissions import IsAuthenticated
from .models import Package, Subscription
from .serializers import PackageSerializer, SubscriptionSerializer


class PackageView(APIView):
    def get(self,request):
        packages = Package.objects.filter(is_enable=True)
        serializer = PackageSerializer(packages,many=True)
        return Response(serializer.data)

class SubscriptionView(APIView):
    permission_class = [IsAuthenticated]


    def get(self,request):
        subscriptions = Subscription.objects.filter(
            user = request.user,
            expire_time__gt = timezones.now()

        )

        serializer = SubscriptionSerializer(subscriptions,many=True)
        return Response(serializer.data)
