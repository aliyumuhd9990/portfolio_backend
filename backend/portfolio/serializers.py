from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Project
        fields = [
            "id", "title", "slug", "category", "completion_date", "tools", "summary",
            "problem", "approach", "insights", "outcome", "featured", "image",
            "image_url", "project_url", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "slug", "image_url", "created_at", "updated_at"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if not obj.image:
            return ""
        url = obj.image.url
        return request.build_absolute_uri(url) if request else url

    def validate_tools(self, value):
        if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
            raise serializers.ValidationError("Tools must be a list of text values.")
        return [x.strip() for x in value if x.strip()]

    def validate_insights(self, value):
        if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
            raise serializers.ValidationError("Insights must be a list of text values.")
        return [x.strip() for x in value if x.strip()]
