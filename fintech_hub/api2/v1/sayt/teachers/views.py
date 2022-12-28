from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api2.v1.sayt.teachers.services import teachers_format, get_one_teachers, teachers_pag
from apps.teachers.models.teachers import TeacherModel
from .serializer import TeacherSerializer


class TeachersView(GenericAPIView):
    serializer_class = TeacherSerializer

    def get_object(self, pk):
        try:
            root = TeacherModel.objects.get(pk=pk)
        except:
            raise NotFound(f'{pk}-chi iddagi malumot topilmadi')
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = get_one_teachers(self.get_object(pk))
        else:
            result = teachers_pag(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(requests.data)

        return Response(teachers_format(data))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        data = requests.data
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        if "image" in requests.data:
            serializer.image1 = requests.data.get('image1')
        data = serializer.save()

        return Response(teachers_format(data))

    def delete(self, requests, pk, *args, **kwargs):
        root = TeacherModel.objects.get(pk=pk)
        root.delete()
        return Response({"Success": f"{root.teacher} malumotlari muoffaqiyatli o'chirildi"})