from rest_framework.routers import SimpleRouter


from . import views



router = SimpleRouter()
router.register(r'penjualan', views.PenjualanView, basename='penjualan')
router.register(r'items', views.ProdukItemView, basename='items')

urlpatterns = router.urls
