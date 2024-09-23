from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 

# Create your views here.
def say_Hello(request):
    return HttpResponse("Hello from Little Lemon!")

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})