from django.contrib import admin
from django.urls import path
from common import __views
from app import views
from django.conf.urls.static import static
from django.conf import settings
__views.MODELS_PATH = 'app.models'
urlpatterns = [
    path('', views.index),
    path('view/<page>', __views.__view),
    path('all/<model>/<keyvalue>/<page>', __views.__all),#username=1&password=123|name=7
    # path('table/<model>/<page>', __views.__table),
    # path('get/<model>/<key>/<value>/<page>', __views.__get),
    path('form/<model>/<page>', __views.__form),
    # path('form/<model>/<listmodel>/<page>', __views.__form_list),
    path('edit/<model>/<id>/<page>', __views.__edit),
    path('update/<model>/<value>/<updateby>', __views.__update),
    # path('edit/<model>/<id>/<listmodel>/<page>', __views.__edit_list),
    path('delete/<model>/<id>', __views.__delete),
    path('save', __views.__save),
    path('login', views.login),
    path('logout', views.logout),
    path('pharmacy_products', views.pharmacy_products),
    path('products', views.products),
    path('view_products', views.view_products),
    path('cart', views.cart),
    # path('home', views.home),
    path('payment', views.payment),
    path('transactions', views.transactions),
    path('deletecart/<id>', views.deletecart),
    path('addconsulting', views.addconsulting),
    path('appoinment', views.appoinment),
    path('prescription', views.prescription),
    path('message', views.message),
    path('error', views.error),

]

# urlpatterns = static(settings.MEDIA_URL, document_root.settings.MEDIA_ROOT)