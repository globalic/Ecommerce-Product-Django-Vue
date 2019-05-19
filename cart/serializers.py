from rest_framework.serializers import ModelSerializer
from .models import Cart


class CartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = ['products', 'subtotal', 'total']
