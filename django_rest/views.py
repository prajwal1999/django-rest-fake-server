from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, Http404
from rest_framework import status

class UserView(APIView):
    def get(self, request, format=None):
        return Response(request.data)

    def post(self, request, format=None):
        request.data['status'] = True
        return Response(request.data)