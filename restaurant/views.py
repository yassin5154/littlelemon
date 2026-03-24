# restaurant/views.py

from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Booking, Menu, Category, Order, Cart
from .serializers import BookingSerializer, MenuSerializer, CategorySerializer, OrderSerializer, CartSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return render(request, 'home.html')

# Pagination pour menu
class MenuPagination(PageNumberPagination):
    page_size = 5  # nombre d'items par page

# Menu API avec pagination, tri et filtrage
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price']            # tri possible par prix
    search_fields = ['category__name']     # filtrer par nom de catégorie
    pagination_class = MenuPagination


# API viewsets start here
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]  # anyone can see menu

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # Limiter les cartes au user connecté
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        date = request.data.get('reservation_date')
        slot = request.data.get('reservation_slot')

        if Booking.objects.filter(reservation_date=date, reservation_slot=slot).exists():
            return Response(
                {"error": "This slot is already booked"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)