from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import InvestmentViewSet

router = SimpleRouter()
router.register('', InvestmentViewSet, base_name='investments')

urlpatterns = router.urls