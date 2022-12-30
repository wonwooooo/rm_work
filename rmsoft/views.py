from django.shortcuts import render

# Create your views here.

import sqlite3
from .models import Company, Client, Product, Order
from django.http import JsonResponse, HttpResponse, Http404
import datetime, json

from django.core import serializers



""" ---------------------
    상품정보 조회 API
--------------------- """
def product(request):
    if request.method == "GET":
        product_list = []
        product = Product.objects.all()

        total_product = 0
        for p in product:
            c = Company.objects.filter(id=p.p_company_name_id)

            product_list.append({"product_name" : p.p_name, 
                                 "product_price" : p.p_price, 
                                 "product_registerdate" : p.p_registerdate.strftime('%Y-%m-%d-%H-%M-%S'), 
                                 "product_company_name" : c[0].company_name})
            total_product += 1
        return JsonResponse({"total_product" : total_product, "list" : product_list}, safe=False)



""" ---------------------
    등록업체 조회 API
--------------------- """
def company(request):
    if request.method == "GET":
        company_list = []
        company = Company.objects.all()

        total_company = 0
        for c in company:
            company_list.append({"company_name" : c.company_name, 
                                 "company_boss_name" : c.company_boss_name, 
                                 "company_tel_number" : c.company_tel_number})
            total_company += 1
        return JsonResponse({"total_company" : total_company, "list" : company_list}, safe=False)



""" ---------------------
    구매자 조회 API
--------------------- """
def client(request):
    if request.method == "GET":
        client_list = []
        client = Client.objects.all()

        total_client = 0
        for c in client:
            phone_number = c.client_phone_number.replace(c.client_phone_number[-3:-1], '**')
            client_list.append({"client_name" : c.client_name,
                                "clinet_phone_number" : phone_number})
            total_client += 1
        return JsonResponse({"total_client" : total_client , "list" : client_list} , safe=False)



""" ---------------------
    구매정보 조회 API
--------------------- """
def order(request):
    if request.method == "GET":
        order_list = []
        order = Order.objects.all()

        total_order = 0
        for o in order:
            # p = Product.objects.filter(id=o.o_p_id_id)
            p = Product.objects.all()
            c = Client.objects.filter(id=o.o_client_id_id)

            order_list.append({"product_name" : p[0].p_name, 
                               "client_name" : c[0].client_name, 
                               "product_price" : p[0].p_price, 
                               "order_date" : o.o_date, 
                               "order_number" : o.o_number})

            total_order += 1
        return JsonResponse({"total_order" : total_order, "list" : order_list}, safe=False)


# def order(request):
#     if request.method == "GET":
#         order_list = []
#         order = Order.objects.all()
#         product = Product.objects.all()
#         client = Client.objects.all()

#         for o in order:
#             order_list.append({"o_p_id" : o_p_id,
#                                 컬럼2 : 컬럼이름값,실제값})
#             total_order += total_order
#         return JsonResponse({고정된형태})

