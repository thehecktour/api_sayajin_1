from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ManagersModel
from .serializer import ManagerSerializer

class AllManagers(APIView):

    def get(self, request):

        managers = ManagersModel.objects.all()
        managers_serializer = ManagerSerializer(managers, many=True)
        return Response(managers_serializer.data)
    
    def post(self, request):

        data = {
            'name' : request.data.get('name'),
            'age' : request.data.get('age'),
            'champions' : request.data.get('champions'),
            'champion_name' : request.data.get('champion_name'),
        }

        serializer_manager = ManagerSerializer(data=data)

        if serializer_manager.is_valid():
            serializer_manager.save()
            return Response(serializer_manager.data)
        else:
            return Response(serializer_manager.errors)