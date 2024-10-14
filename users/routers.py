from rest_framework.routers import DefaultRouter

from .api_viewset import UsersViewset


router = DefaultRouter()
router.register("users", UsersViewset, 'users')

urlpatterns = router.urls