from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

# model object --single student data 

def student_details(request, pk):
    stu = Student.objects.get(id=pk) 
    serializer = StudentSerializer(stu) # complex_data --> python_obejct 
    # json_data = JSONRenderer().render(serializer.data) # python_object --> json_data

    # return HttpResponse(json_data, content_type='application/json') # json_data --> http_response

    # set safe = True whn ur data is dict , when your data is list(non-dict) put safe=False
    return JsonResponse(serializer.data, safe=True)


# query set  -- all  student data 

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True) # complex_data --> python_obejct 
    json_data = JSONRenderer().render(serializer.data) # python_object --> json_data

    return HttpResponse(json_data, content_type='application/json') # json_data --> http_response

    
