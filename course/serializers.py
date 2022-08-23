from rest_framework import serializers

from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    date_posted = serializers.SerializerMethodField(required=False)
    educator_username = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "image",
            "date_posted",
            "educator_username",
        ]

    def get_date_posted(self, obj):
        return obj.created.strftime("%d %B, %Y")

    def get_educator_username(self, obj):
        return obj.educator.username
