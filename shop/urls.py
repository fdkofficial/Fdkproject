from django.urls import path
from .import views

urlpatterns = [
    path("<int:id>",views.index,name="ShopHome"),
    path("about/",views.about,name="About"),
    path("contactUs/",views.contact,name="Contactus"),
    path("productView",views.pv,name="Pv"),
    path("tracker",views.tracker,name="Tracker"),
    path("search",views.search,name="Search"),
    path('upload_img',views.uploadf,name='upload'),
    path('categ',views.categ,name='Category'),
    #path('review/',views.reviews,name='review'),
    path('<int:id>vp',views.vp,name='vp'),
    path('Buy',views.buy,name='Buy'),
    path('cart',views.cart,name='cart'),
    path('search/',views.search,name='search'),
    path('<int:id>cartview',views.cartview,name='cartview'),
]
