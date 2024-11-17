from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from .models import *
import numpy as np
from scipy.optimize import linprog
from django.http import HttpResponse
from datetime import datetime, timedelta
#import pyotp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import os
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
import requests

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from App.serializers import *


#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination

from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.conf import settings
#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from App.serializers import *

from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view
from django.db.models import Sum
from django.db import transaction

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))








class LatestVersionView(APIView):
    def get(self, request):
        latest_version = "7"
        return JsonResponse({"latest_version": latest_version})




class AddWatejaWoteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()

        # Automatically fill in fields from the user
        data['AmesajiliwaNa'] = user.username

        # Ensure 'KiasiAnachokopa' is provided
        kiasi_anachokopa = data.get('KiasiAnachokopa', None)
        if not kiasi_anachokopa:
            return Response(
                {"error": "KiasiAnachokopa is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        
        kiasi_anachokopa = int(kiasi_anachokopa)
        
        
        # Perform calculations
        rejesho_kwa_siku = round(kiasi_anachokopa / 30, 0)
        jumla_ya_deni = kiasi_anachokopa  # Assuming the initial debt is the same as the loan amount

        # Assign calculated fields to the data
        data['RejeshoKwaSiku'] = int(rejesho_kwa_siku)
        data['JumlaYaDeni'] = jumla_ya_deni
        

        serializer = WatejaWoteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            # Email notification to admin
            myemail = "juniordimoso8@gmail.com"
            subject = "Gegwajo Microfinance"
            message = (
                f"Mteja amesajiliwa kikamilifu"
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [myemail]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetAllWatejaWoteView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            # categoryId = int(request.query_params.get('id'))
            # TypeId = int(request.query_params.get('TypeId'))
            


            queryset = WatejaWote.objects.all(
                #FoodGroup__Jina__icontains = "Vyanzo vya Protini na Mafuta"
                # productCategory__id__icontains = categoryId,
                # Type__id__icontains = TypeId
                ).order_by('JinaKamiliLaMteja')

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = WatejaWoteSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)











#------------------CART AND CART ITEMS_-----================


class WatejaWoteCartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # kama unatumia JWT weka hiyo tu
    # permission_classes =[IsAuthenticated]

    #RETRIEVE CART ITEMS FROM A CART
    def get(self, request):
        #http://127.0.0.1:8000/Cart/HotelOrder/?pages=1&page_size=2
        #user = request.user
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed

            #orders = HotelOrder.objects.all().order_by('-id')
            #CategoryId = int(request.query_params.get('CategoryId'))
            queryset = WatejaWoteCart.objects.all(
                #user=user,
                #closed_order_state=False
                # CategoryId=CategoryId
                )
            main_total_price = queryset.aggregate(Sum('total_price'))['total_price__sum']

            # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = WatejaWoteCartSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
                'main_total_price':main_total_price,
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

    def post(self, request):
        data = request.data
        # user = request.user
        JinaKamiliLaMteja = request.query_params.get('JinaKamiliLaMteja')

        cart, _ = WatejaWoteCart.objects.get_or_create(
            JinaKamiliLaMteja=JinaKamiliLaMteja, 
            ordered=False
            )
        Mteja = WatejaWote.objects.get(id=data.get('Mteja'))

        
            

        #price = product.price
        quantity = 1 #data.get('quantity')

        KiasiChaRejeshoChaSiku = data.get('KiasiChaRejeshoChaSiku')
        
        #hakikisha kiasi unachoingiza cha rejesho kisiwekidogo ya 
        #nusu ya rejesho lake la kila siku
        rejesho_lake_kwa_siku = Mteja.RejeshoKwaSiku / 2
        if int(KiasiChaRejeshoChaSiku) < rejesho_lake_kwa_siku:
            return Response({
                'error': f'Kiasi ulichoingiza kipo chini ya Tsh. {rejesho_lake_kwa_siku} ambacho ni nusu ya rejesho la mteja analotakiwa kurejesha kila siku.'
            }, status=status.HTTP_400_BAD_REQUEST)


        cart_items = WatejaWoteCartItems(
            cart=cart, 
            JinaKamiliLaMteja=JinaKamiliLaMteja, 
            Mteja=Mteja, 
            KiasiChaRejeshoChaSiku=KiasiChaRejeshoChaSiku, 
            quantity=quantity,
            # table=table,
            # room=room,
            # Customer=Customer
            # CustomerFullName=CustomerFullName,
            # PhoneNumber=PhoneNumber,
            # CustomerAddress=CustomerAddress
            )
        cart_items.save()


        KiasiAnachokopa = Mteja.KiasiAnachokopa
        JumlaYaDeni_Value = Mteja.JumlaYaDeni

        remained_deni = JumlaYaDeni_Value - int(KiasiChaRejeshoChaSiku)
        Mteja.JumlaYaDeni = remained_deni  # Update the field on the Mteja instance

        kiasi_alicholipa = KiasiAnachokopa - remained_deni
        Mteja.KiasiAlicholipa = kiasi_alicholipa

        Mteja.save()  # Save the changes to the database

        # Decrease the product quantity in stock
        # product.ProductQuantity -= quantity
        # product.save()

        cart_items = WatejaWoteCartItems.objects.filter(
            JinaKamiliLaMteja=JinaKamiliLaMteja, 
            cart=cart.id
        )

        total_price = 0
        total_Kilos = 0
        for items in cart_items:
            total_price += items.KiasiChaRejeshoChaSiku
            

        cart.total_price = total_price
        

        cart.save()
        return Response({'success': 'Items Added To Your Cart'})



    #TO UPDATE CART ITEMS
    #Eg:
    # {
    #     "id":11,
    #     "quantity":6
    # }
    def put(self, request):
        data = request.data
        cart_item = WatejaWoteCartItems.objects.get(id=data.get('id'))
        quantity = 1 #data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Item Updated Sccussfully'})



    #TO DELETE ITEM IN A CART
    #Eg:
    #Pass id of the product
    # {
    #     "id":9

    # }
    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = WatejaWoteCartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = WatejaWoteCart.objects.filter(user=user, ordered=False).first()
        queryset = WatejaWoteCartItems.objects.filter(cart=cart)
        serializer = WatejaWoteCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)




#TO DELETE SELECTED CART ITEM
class WatejaWoteDeleteCartItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        cartId = request.query_params.get("cartId")

        user = request.user

        try:
            cart_item = WatejaWoteCartItems.objects.get(id=cartId)

            # Increase the product quantity back to stock
            # cart_item.product.ProductQuantity += cart_item.quantity
            # cart_item.product.save()

            cart_item.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except WatejaWoteCartItems.DoesNotExist:
            return Response({"error": "Product not found in the cart"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



