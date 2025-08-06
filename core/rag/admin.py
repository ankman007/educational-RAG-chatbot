from django.contrib import admin
from .models import Course, Enrollment, Document, DocumentChunk
from .form import DocumentForm

class EducatorAdminMixin:
    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.groups.filter(name__in=['Educator', 'Admin']).exists()

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.groups.filter(name__in=['Educator', 'Admin']).exists()

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.groups.filter(name__in=['Educator', 'Admin']).exists()

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.groups.filter(name__in=['Educator', 'Admin']).exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.groups.filter(name='Admin').exists()


@admin.register(Course)
class CourseAdmin(EducatorAdminMixin, admin.ModelAdmin):
    list_display = ("name", "code", "created_at")


@admin.register(Document)
class DocumentAdmin(EducatorAdminMixin, admin.ModelAdmin):
    form = DocumentForm

    list_display = ("title", "course", "uploaded_by", "uploaded_at")

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.groups.filter(name__in=['Educator', 'Admin']).exists()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Educator').exists() and not request.user.is_superuser:
            return qs.filter(uploaded_by=request.user)
        return qs


@admin.register(Enrollment)
class EnrollmentAdmin(EducatorAdminMixin, admin.ModelAdmin):
    list_display = ("user", "course", "enrolled_at")


@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):
    list_display = ("chunk_id", "document")

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.groups.filter(name='Admin').exists()
