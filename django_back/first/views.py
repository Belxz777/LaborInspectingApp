from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

from first.serializer import UserSerializer

from .models import Users, JobTitle, Project, Task, WorkOnTask
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
def index(request):
    return HttpResponse("Добавил requriments.txt реализовал CR пока без Delete ,  Роман не лох")


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            users = users.filter(title__icontains=title)
        
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = UserSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=201)
        return JsonResponse(tutorial_serializer.errors, status=400)


