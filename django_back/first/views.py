from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

from first.serializer import UserSerializer

from .models import Users, JobTitle, Project, Task, WorkOnTask
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
def index(request):
    return HttpResponse("Добавил requriments.txt ,  Роман не лох")


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


def create_user(request):
 if request.method == "POST":
    job_title_id = request.POST.get('job_title_id') 
    age = request.POST.get('age')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    father_name = request.POST.get('father_name')

    maindata  =JsonParser().parse(request.body)
    user = Users.objects.create(
    job_title_id=job_title_id, 
    age=age,
    first_name=first_name,
    last_name=last_name,
    father_name=father_name
  )
  
    data = {
    'id': user.id,
    'job_title': user.job_title_id, 
    'age': user.age,
    'first_name': user.first_name,
    'last_name': user.last_name,
    'father_name': user.father_name
  }

    return JsonResponse(data)
   
      
 


def retrieve_user(request, user_id):
  user = Users.objects.get(id=user_id)
  
  data = {
    'id': user.id,
    'job_title': user.job_title_id,
    'age': user.age, 
    'first_name': user.first_name,
    'last_name': user.last_name,
    'father_name': user.father_name
  }
  
  return JsonResponse(data,safe=False)

def delete_user(request, user_id):
  user = Users.objects.get(id=user_id)
  user.delete()

  return JsonResponse({'message': 'User deleted'})
