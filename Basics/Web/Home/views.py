from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer,CarSerializer
from .models import Person
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def home(request):
    if request.method=='POST':
        data=request.data
        print(data["name"])
    elif request.method=='GET':
        print(request.GET.get('search'))    
    return Response({"message":"Hellllo"})

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def people(request):
    if request.method=='GET':
        objs=Person.objects.all()
        serializer=PersonSerializer(objs,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        data1=request.data
        print("********* ",data1)
        serializer=PersonSerializer(data=data1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=='PUT':
        data1=request.data
        print("********* ",data1)
        # person = get_object_or_404(Person, id=data1.get('id')) 
        person=Person.objects.get(id=data1['id'])
        serializer=PersonSerializer(person,data=data1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=='PATCH':
        data1=request.data
        print("********* ",data1)
        person = get_object_or_404(Person, id=data1.get('id')) 
        serializer=PersonSerializer(person,data=data1,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data=request.data
        obj=Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"message":"Person Deleted"})
