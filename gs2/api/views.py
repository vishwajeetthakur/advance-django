from django.shortcuts import render
import io 
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer 
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method=="POST":
        json_data = request.body # get data in json form
        stream = io.BytesIO(json_data) # create stream of json data
        pythondata = JSONParser().parse(stream)

        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save() 
            res = {"msg" : "data inserted"} 
            json_data_render = JSONRenderer().render(res)

            return HttpResponse(json_data_render, content_type="application/json")
        

        json_data_render = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data_render, content_type="application/json")

    return JsonResponse("error", safe=False)