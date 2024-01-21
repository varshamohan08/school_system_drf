from datetime import datetime
from django.shortcuts import redirect, render
from announcement_app.forms import AnnouncementForm
from announcement_app.models import Announcement
from announcement_app.serializers import AnnouncementSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user_app.permissions import IsEditorUser, IsAdminUser

# Create your views here.
class AnnouncementAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'PUT':
            return [IsAdminUser()]
        elif self.request.method == 'POST':
            return [IsEditorUser()]
        else:
            return super().get_permissions()
        
    
        
    def get(self, request):
        try:
            if request.user.user_details.role in ['Admin', 'Editor']:
                announcements = Announcement.objects.all().order_by('-id')
                seraializer_data = AnnouncementSerializer(announcements, many=True)
                return render(request, "announcement.html", {"announcements": seraializer_data.data, "role": request.user.user_details.role, "username": request.user.username})
                # return Response({'detail': seraializer_data.data}, status=status.HTTP_200_OK)
            elif Announcement.objects.filter(status = 'Approved').exists():
                announcements = Announcement.objects.filter(status = 'Approved', expiration_date__gte = datetime.now()).order_by('-id')
                seraializer_data = AnnouncementSerializer(announcements, many=True)
                return render(request, "announcement.html", {"announcements": seraializer_data.data, "role": request.user.user_details.role, "username": request.user.username})
                return Response({'detail': seraializer_data.data}, status=status.HTTP_200_OK)
            return render(request, "announcement.html", {"announcements": []})
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        
    def put(self, request):
        try:
            if not Announcement.objects.filter(id = request.data.get('id')):
                raise Exception('Announcement not found')
            else:
                announcement = Announcement.objects.get(id = request.data.get('id'))
            if announcement.status == 'Pending':
                announcement.status = request.data.get('status')
                announcement.approved_by = request.user
                announcement.approved_at = datetime.now()
                announcement.save()
                return Response({'detail': 'Status updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Announcement already '+str(announcement.status)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AddAnnouncement(APIView):
    permission_classes = [IsAuthenticated, IsEditorUser]

    def get(self, request, *args, **kwargs):
        form = AnnouncementForm()
        return render(request, 'add_announcement.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.created_by = request.user
            announcement.created_at = datetime.now()
            announcement.save()
            return redirect('announcement_app:announce')

        return render(request, 'add_announcement.html', {'form': form})
    # def post(self, request):
    #     try:
    #         data = request.data
    #         data['created_by'] = request.user.id
    #         validate_data = AnnouncementSerializer(data=data, context={'request': request})
    #         if validate_data.is_valid():
    #             validate_data.save()
    #             return Response({'detail': 'Announcement created successfully'}, status=status.HTTP_201_CREATED)
    #         return Response({'detail': validate_data.errors}, status=status.HTTP_401_UNAUTHORIZED)
        
    #     except Exception as e:
    #         return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)