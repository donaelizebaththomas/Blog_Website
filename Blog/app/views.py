from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

from app.models import BlogPost
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from app.serializers import BlogPostSerializer, BlogPostCreateUpdateSerializer, UserSerializer, UserRegistrationSerializer, \
    UserDetailSerializer, UserUpdateSerializer

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


# BlogPostViewSet
class BlogPostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing, creating, updating, and deleting BlogPost objects.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        # Automatically set the logged-in user as the author of the blog post
        serializer.save(author=self.request.user)


# UserViewSet
class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and managing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


# UserLoginAPIView
class UserLoginAPIView(APIView):
    """
    Handle user login and return the authentication token.
    """

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# UserRegisterAPIView
class UserRegisterAPIView(APIView):
    """
    Register a new user
    """

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserDetailSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# UserDetailAPIView (optional if you want to allow retrieving user details using viewsets)
class UserDetailAPIView(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve user details.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

class user_logout(APIView):
        def get(self, request):
            # Delete the token associated with the logged-in user to logout
            self.request.user.auth_token.delete()
            return Response({'msg': "Logout successful"}, status=status.HTTP_200_OK)
