from django.urls import reverse, resolve
from django.test import SimpleTestCase
from invoice_generator.views import create_invoice,create_invoice_detail,delete_invoice,get_invoice,get_invoices

class TestUrls(SimpleTestCase):
  def test_create_invoice_url_resolves(self):
    url = reverse('create_invoice')
    self.assertEquals(resolve(url).func, create_invoice)
  
  def test_create_invoice_detail_url_resolves(self):
    url = reverse('create_invoice_detail', args=[1])
    self.assertEquals(resolve(url).func, create_invoice_detail)
  
  def test_delete_invoice_url_resolves(self):
    url = reverse('delete_invoice', args=[1])
    self.assertEquals(resolve(url).func, delete_invoice)
  
  def test_get_invoice_url_resolves(self):
    url = reverse('get_invoice', args=[1])
    self.assertEquals(resolve(url).func, get_invoice)
  
  def test_get_invoices_url_resolves(self):
    url = reverse('get_invoices')
    self.assertEquals(resolve(url).func, get_invoices)
  
