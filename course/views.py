from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Course
from course.serializers import CourseSerializer


class CourseApiView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if not request.user.groups.filter(name="Student").exists():
            return Response({"message": "You are not a Student"}, status=400)

        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        if not request.user.groups.filter(name="Educator").exists():
            return Response({"message": "You are not an educator"}, status=400)

        title = request.data.get("title")
        description = request.data.get("description")
        image = request.data.get("image")

        course = Course(
            title=title, description=description, image=image, educator=request.user
        )
        course.save()

        return Response({"message": "Course Created"}, status=201)


class CourseDetailApiView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if request.user.groups.filter(name="Student").exists():
            course = Course.objects.get(id=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=200)

        elif request.user.groups.filter(name="Educator").exists():
            course = Course.objects.get(id=pk)
            if not course.educator == request.user:
                return Response(
                    {"message": "you are not the educator of this course"}, status=400
                )

            student_usernames = course.students.objects.values_list(
                "username", flat=True
            )

            return Response({"student_usernames": student_usernames}, status=200)

    def post(self, request, pk):
        if not request.user.groups.filter(name="Student").exists():
            return Response({"message": "You are not a Student"}, status=400)

        course = Course.objects.get(id=pk)
        course.students.add(request.user)

        return Response({"message": "enrolled"}, status=200)
