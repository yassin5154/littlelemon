from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import MenuViewSet, CategoryViewSet, OrderViewSet, CartViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # Les routes de l'API seront automatiquement ajoutées par le router
] 
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls