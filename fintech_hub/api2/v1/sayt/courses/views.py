from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api2.v1.sayt.courses.services import courses_format, courses_pag, get_one_courses
from apps.courses.models.courses import CourseModel
from .serializer import CourseSerializer


class CoursesView(GenericAPIView):
    serializer_class = CourseSerializer

    def get_object(self, pk):
        try:
            root = CourseModel.objects.get(pk=pk)
        except:
            raise NotFound(f'{pk}-chi iddagi malumot topilmadi')
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = get_one_courses(self.get_object(pk))
        else:
            result = courses_pag(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(requests.data)

        return Response(courses_format(data))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        data = requests.data
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        if "image1" in requests.data:
            serializer.image1 = requests.data.get('image1')
        data = serializer.save()

        return Response(courses_format(data))

    def delete(self, requests, pk, *args, **kwargs):
        root = CourseModel.objects.get(pk=pk)
        root.delete()
        return Response({"Success": "Course malumotlari muoffaqiyatli o'chirildi"})