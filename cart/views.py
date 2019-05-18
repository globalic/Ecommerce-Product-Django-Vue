from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from variants.models import Variant
from .models import Cart
from .serializers import CartSerializer


@api_view()
@permission_classes([AllowAny])
def cart_home(request):
    if request.user.is_authenticated:
        print('noiceeeeeeeeeeeeeeeeeeeeeeee')
    else:
        print('not noiceeeeeeeeeeeeeeeee')
    cart = Cart.objects.get_or_new(request)
    serialized_cart = CartSerializer(cart)
    cart_products = [x.id for x in cart.products.all()]
    details = Variant.objects.get_details(cart_products)
    return Response({'cart': serialized_cart.data, 'variants': details})


@api_view()
@permission_classes([AllowAny])
def cart_edit(request, product_id):
    try:
        product = Variant.objects.get(id=product_id)
    except Variant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cart = Cart.objects.get_or_new(request)
    if product in cart.products.all():
        cart.products.remove(product)
        action = 'removed'
    else:
        cart.products.add(product)
        action = 'added'
    return Response({'action': action}, status=status.HTTP_200_OK)