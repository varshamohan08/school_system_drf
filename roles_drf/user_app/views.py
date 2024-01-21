from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from user_app.models import UserDetails
from django.core.exceptions import PermissionDenied
from user_app.permissions import IsAdminUser
from user_app.serializers import UserDetailsSerializer

# Create your views here.

class userRegistration(APIView):
    def get(self, request):
        return render(request, "registration.html", {"error_message": None})

    def post(self, request):
        validated_data = request.data
        user = User.objects.create_user(
            username=request.data.get('username'),
            email=request.data.get('email'),
            password=request.data.get('password')
        )
        if user is not None:

            user_details = UserDetails.objects.create(
                user=user,
                name=request.data.get('name'),
                email=request.data.get('email'),
                role=request.data.get('role'),
                country=request.data.get('country'),
                nationality=request.data.get('nationality'),
                mobile=request.data.get('mobile'),
            )
            return redirect('user_app:login')
            # return Response({'detail': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return render(request, "registration.html", {"error_message": "Invalid credentials"})
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class userLogin(APIView):
    def get(self, request):
        return render(request, "login.html", {"error_message": None})
    
    def post(self,request):

        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            request.session['access_token'] = access_token
            return redirect('/announcement/announce')

            # return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        else:
            return render(request, "login.html", {"error_message" : 'Sorry, your password or email was incorrect. Please double-check.'})

      
class userLogout(APIView):
    def get(self, request):
        logout(request)
        # return render(request, "login.html", {"error_message": None})
        return redirect('user_app:login')
            
class userCommonApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        validated_data = UserDetailsSerializer(request.user.user_details)
        return Response({'data' : validated_data.data}, status = status.HTTP_200_OK)

    def put(self, request):

        current_password = request.data['current_password']
        new_password = request.data['new_password']

        user = request.user
        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Current password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
            
class userApi(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request):
        user_details = UserDetailsSerializer(UserDetails.objects.all(), many=True)
        return render(request, "user_list.html", {"users": user_details.data})