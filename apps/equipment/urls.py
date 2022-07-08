from rest_framework.routers import SimpleRouter
from apps.equipment import views

router = SimpleRouter()
router.register('api/equipment', views.EquipmentViewSet)
router.register('api/equipment-type', views.EquipmentTypeViewSet)
urlpatterns = router.urls
