from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer, DetailSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
@api_view(['POST'])
def registration_views(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
            'username':user.username,
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token)
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response({'Error':"Couldn't create account"})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_views(request):
   try:
    user = request.user
    data = {
        'id':user.id,
        'username':user.username,
        'email':user.email,
    }
    return Response(data, status=status.HTTP_200_OK)
   except ObjectDoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    