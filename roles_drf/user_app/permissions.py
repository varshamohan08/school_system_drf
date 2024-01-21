from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_details.role == 'Admin'

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_details.role == 'Staff'

class IsStudentUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_details.role == 'Student'

class IsEditorUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_details.role == 'Editor'

class IsStaffAdminStudentUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_details.role in ['Admin','Staff','Student']