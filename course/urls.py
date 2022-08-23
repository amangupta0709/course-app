from django.urls import include, path

from course.views import CourseApiView, CourseDetailApiView

urlpatterns = [
    path("", CourseApiView.as_view(), name="course-list"),
    path("<int:pk>/", CourseDetailApiView.as_view(), name="course-list"),
]
