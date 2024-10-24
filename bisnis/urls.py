from rest_framework.routers import SimpleRouter


from . import views



router = SimpleRouter()
router.register(r'barang', views.BarangView, basename='barang')


urlpatterns = router.urls
