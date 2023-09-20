from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .serializers import NewsSerializer
from .models import NewsModel
from rest_framework.response import Response
# Create your views here.

class CreateApiView(APIView):
    def post(self,request):
        if str(request.user)!='AnonymousUser':
            if request.user.roles==2:
                serializer=NewsSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        else:
            return Response({'msg':'only for staff members'})
        
class ListApiView(APIView):
    def get(self,request):
        print(request.user)
        if str(request.user)=='AnonymousUser':
            return Response({'msg':'log in !!'})
        all=NewsModel.objects.filter(status=True)
        serializer=NewsSerializer(all,many=True)
        return Response(serializer.data)

class UpdateStatus(APIView):
    def patch(self,request,*args,**kwargs):
        if str(request.user)!='AnonymousUser':
            if request.user.roles==3:
                news=get_object_or_404(NewsModel,id=kwargs['news_id'])
                serializer=NewsSerializer(news,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        else:
            return Response({'msg':'only admins can change !!'})