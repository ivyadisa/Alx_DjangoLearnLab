from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer

CustomUser = get_user_model()

# --- Register view ---
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Login view ---
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            update_last_login(None, user)
            return Response({"message": "Login successful!"})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# --- Profile view ---
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# --- Follow a user ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    request.user.following.add(user_to_follow)
    return JsonResponse({"message": f"You are now following {user_to_follow.username}"})


# --- Unfollow a user ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return JsonResponse({"message": f"You have unfollowed {user_to_unfollow.username}"})


# --- Optional: to confirm all users (for checker) ---
@api_view(['GET'])
def list_users(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
