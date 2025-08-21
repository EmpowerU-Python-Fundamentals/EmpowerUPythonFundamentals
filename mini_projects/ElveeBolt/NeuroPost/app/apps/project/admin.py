from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Project, ProjectPlan, ProjectPlanPost


class ProjectAdmin(ModelAdmin):
    list_display = ("title", "channel")


class ProjectPlanAdmin(ModelAdmin):
    list_display = ("title", "project", "is_gpt")


class ProjectPlanPostAdmin(ModelAdmin):
    list_display = (
        "title",
        "plan",
        "is_approved",
        "is_draft",
        "is_published",
        "publish_at",
        "created_at",
    )
    readonly_fields = ("is_published",)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPlan, ProjectPlanAdmin)
admin.site.register(ProjectPlanPost, ProjectPlanPostAdmin)
