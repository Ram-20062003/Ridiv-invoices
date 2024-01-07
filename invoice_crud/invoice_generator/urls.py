from django.urls import path
from invoice_generator import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('create_invoice', views.create_invoice, name='create_invoice'),
    path('create_invoice_detail/<int:id>', views.create_invoice_detail, name='create_invoice_detail'),
    path('<int:id>', views.get_invoice, name='get_invoice'),
    path('delete_invoice/<int:id>', views.delete_invoice, name='delete_invoice'),
    path('invoices', views.get_invoices, name='get_invoices')
]