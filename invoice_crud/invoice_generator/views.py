from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import InvoiceModel, InvoiceDetailModel
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the invoice_generator index.")

@csrf_exempt
def create_invoice(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            invoice_id = data.get('invoice_id')
            customer_name = data.get('name')

            InvoiceModel.objects.create(
                InvoiceID=invoice_id,
                CustomerName=customer_name
            )

            return JsonResponse({'message': 'Invoice created successfully!'})
        except Exception as e:
            print("1")
            print(e)
            return JsonResponse({'internal server error occured': str(e)}, status=500)
    else:
        print("hi".e)
        return JsonResponse({'error': 'Only POST requests allowed'}, status=405)

@csrf_exempt
def create_invoice_detail(request,id):
    if request.method == 'POST':
        print(id)
        try:
            data = json.loads(request.body)
            inovice_id = data.get('id')
            description = data.get('description')
            unit_price = data.get('unit_price')
            quantity = data.get('quantity')
            price = data.get('price')
            invoice = InvoiceModel.objects.filter(InvoiceID = inovice_id).first()
            if invoice is None:
                return JsonResponse({'error': 'Invoice not found'}, status=400)
            print(invoice)
            print(invoice)
            InvoiceDetailModel.objects.update_or_create(
                id = id,
                defaults={
                    'InvoiceModelID':invoice,
                    'Description':description,
                    'UnitPrice':unit_price,
                    'Quantity':quantity,
                    'Price':price
                }
            )

            return JsonResponse({'message': 'Invoice Detail created successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests allowed'}, status=405)
    
@csrf_exempt
def delete_invoice(request,id):
    if request.method == 'DELETE':
        try:
            invoice = InvoiceModel.objects.get(id=id)
            if invoice is None:
                return JsonResponse({'error': 'Invoice not found'}, status=400)
            invoice_detail = InvoiceDetailModel.objects.filter(InvoiceModelID = invoice).first()
            print(invoice_detail)
            invoice_detail.delete()
            invoice.delete()
            return JsonResponse({'message': 'Invoice deleted successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only DELETE requests allowed'}, status=405)

@csrf_exempt
def get_invoice(request,id):
    if request.method == 'GET':
        try:
            invoice = InvoiceModel.objects.get(id=id)
            if invoice is None:
                return JsonResponse({'error': 'Invoice not found'}, status=400)
            invoice_detail = InvoiceDetailModel.objects.filter(InvoiceModelID = invoice).first()
            invoice_detail_response = {}
            invoice_detail_response['invoice_id'] = invoice.InvoiceID
            invoice_detail_response['customer_name'] = invoice.CustomerName
            invoice_detail_response['date'] = invoice.Date
            invoice_detail = InvoiceDetailModel.objects.filter(InvoiceModelID = invoice).all()
            data ={}
            for detail in invoice_detail:
                    data['description'] = detail.Description
                    data['quantity'] = detail.Quantity
                    data['unit_price'] = detail.UnitPrice
                    data['price'] = detail.Price
                    invoice_detail_response['data'] = data
            return JsonResponse({'message': 'Invoice fetched successfully!','invoice':invoice_detail_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only GET requests allowed'}, status=405)
    
@csrf_exempt
def get_invoices(request):
    if request.method == 'GET':
        try:
            invoices = InvoiceModel.objects.all()
            if invoices is None:
                return JsonResponse({'error': 'Invoice not found'}, status=400)
            invoice_response = []
            for invoice in invoices:
                invoice_detail_response = {}
                invoice_detail_response['invoice_id'] = invoice.InvoiceID
                invoice_detail_response['customer_name'] = invoice.CustomerName
                invoice_detail_response['date'] = invoice.Date
                invoice_detail = InvoiceDetailModel.objects.filter(InvoiceModelID = invoice).all()
                data ={}
                for detail in invoice_detail:
                    data['description'] = detail.Description
                    data['quantity'] = detail.Quantity
                    data['unit_price'] = detail.UnitPrice
                    data['price'] = detail.Price
                    invoice_detail_response['data'] = data
                invoice_response.append(invoice_detail_response)
            return JsonResponse({'message': 'Invoice fetched successfully!', 'invoice':invoice_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only GET requests allowed'}, status=405)