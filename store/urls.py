from django.urls import path
#. means store folder
from . import views

app_name='store'
urlpatterns = [
    path('',views.all_products,name='all_products'),
    #item can be change by any thing
    path('item/<slug:slug>/',views.product_detail,name='product_detail'),
    path('search/<slug:category_slug>/',views.category_list,name='ategory_list'),

]
