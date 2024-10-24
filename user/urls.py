from rest_framework.routers import SimpleRouter


from . import views



router = SimpleRouter()
router.register(r'profile', views.ProfileView, basename='profile')

urlpatterns = router.urls
