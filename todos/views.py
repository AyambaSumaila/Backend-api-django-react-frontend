from django.shortcuts import render
from rest_framework import generics   # type: ignore
from .models import Todo 
from .serializers import TodoSerializer 
# Create your views here.

#LIst to todo view 
class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

    #Detail Todo view
class DetailTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer


