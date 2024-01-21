from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from announcement_app.models import Announcement
from assignment_app.forms import AnswerForm, AssignmentForm
from assignment_app.models import Answer, Assignment
from assignment_app.serializers import AnswerSerializer, AssignmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user_app.permissions import IsStaffAdminStudentUser, IsStaffUser, IsStudentUser, IsAdminUser

# Create your views here.
class AssignmentAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsStaffUser()]
        if self.request.method == 'GET':
            return [IsStaffAdminStudentUser()]
        else:
            return super().get_permissions()
        
    def get(self, request):
        try:
            assignments = Assignment.objects.all()
            seraializer_data = AssignmentSerializer(assignments, many=True)
            return render(request, "assignments.html", {"assignments": seraializer_data.data, "role": request.user.user_details.role, "username": request.user.username})
            return Response({'detail': seraializer_data.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AddAssignmentAPI(APIView):
    permission_classes = [IsAuthenticated, IsStaffUser]

    def get(self, request, *args, **kwargs):
        form = AssignmentForm()
        return render(request, 'add_assignment.html', {'form': form})
    
    def post(self, request):
        try:
            
            form = AssignmentForm(request.POST)
            if form.is_valid():
                assignment = form.save(commit=False)
                assignment.created_by = request.user
                assignment.created_at = datetime.now()
                assignment.save()
                return redirect('assignment_app:assignment')
            return render(request, 'add_assignment.html', {'form': form})
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class AddAnswer(APIView):
    permission_classes = [IsAuthenticated, IsStudentUser]

    def get(self, request, *args, **kwargs):
        assignment_id = request.GET.get('id')
        assignment = get_object_or_404(Assignment, pk=assignment_id)
        answer = Answer.objects.filter(assignment = assignment, created_by = request.user)
        answer_read_only =False
        if answer.exists():
            if answer.first().marks is not None or assignment.due_date < datetime.now().date():
                answer_read_only = True
            form = AnswerForm(instance=answer.first(), read_only=answer_read_only)
        else:
            form = AnswerForm()
        return render(request, 'add_answer.html', {'form': form, 'assignment': assignment, 'answer_read_only': answer_read_only})

    def post(self, request, *args, **kwargs):

        assignment_id = request.GET.get('id')
        assignment = get_object_or_404(Assignment, pk=assignment_id)

        form = AnswerForm(request.POST, instance=Answer())
        if form.is_valid():
            answer = form.save(commit=False)
            answer.assignment = assignment
            answer.created_by = request.user
            answer.save()
            return redirect('assignment_app:assignment')
        else:
            print(form.errors)

        return render(request, 'add_answer.html', {'form': form})


class AnswerAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsStudentUser()]
        if self.request.method == 'GET':
            return [IsStaffAdminStudentUser()]
        if self.request.method == 'PUT':
            return [IsStaffUser()]
        else:
            return super().get_permissions()
        
    def get(self, request):
        try:
            if request.user.user_details.role == 'Admin':
                answers = Answer.objects.all()
            if request.user.user_details.role == 'Student':
                answers = Answer.objects.filter(created_by = request.user)
            elif request.user.user_details.role == 'Staff':
                answers = Answer.objects.filter(assignment__created_by = request.user)
            if answers.exists():
                data = answers.values('id','answer_text','assignment__title','assignment__due_date','created_by__username','created_at','marks','remarks').order_by('-assignment__due_date')
                return render(request, "answers.html", {"answers": data, "role": request.user.user_details.role, "username": request.user.username})
                return Response({'detail': seraializer_data.data}, status=status.HTTP_200_OK)
            else:
                return render(request, "answers.html", {"answers": [], "role": request.user.user_details.role, "username": request.user.username})
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            data = request.data
            data['created_by'] = request.user.id
            # assignment_id = data.pop('assignment_id', None)
            # data['assignment'] = Assignment.objects.get(id = assignment_id)

            validate_data = AnswerSerializer(data=data, context={'request': request})
            if validate_data.is_valid():
                validate_data.save()
                return Response({'detail': 'Answer created successfully'}, status=status.HTTP_201_CREATED)
            return Response({'detail': validate_data.errors}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            answer = Answer.objects.get(id = request.data.get('id'))
            if not answer.marks:
                answer.marks = request.data.get('marks')
                answer.remarks = request.data.get('remarks')
                answer.evaluvated_by = request.user
                answer.evaluvated_at = datetime.now()
                answer.save()
                return Response({'detail': 'Marks updated successfully'}, status=status.HTTP_200_OK)
            else:
                answer.remarks = str(answer.remarks) + '<br>Marks revised, Last mark: ' + str(answer.marks) + ', Revised Mark: ' +  str(request.data.get('marks')) + ', Remarks: ' + str(request.data.get('remarks'))
                answer.marks = request.data.get('marks')
                answer.evaluvated_by = request.user
                answer.evaluvated_at = datetime.now()
                answer.save()
                return Response({'detail': 'Marks revised successfully'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)