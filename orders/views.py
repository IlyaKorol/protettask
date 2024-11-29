from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user = serializer.validated_data.get('user')
        if not user:
            raise ValidationError("User with this ID does not exist.")
        serializer.save()
