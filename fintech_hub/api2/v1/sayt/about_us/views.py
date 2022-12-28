from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from api2.v1.sayt.about_us.services import about_format, about_pag, get_one_about
from apps.about_us.models.about_us import AboutUsModel
from .serializer import AboutSerializer


class AboutView(GenericAPIView):
    serializer_class = AboutSerializer

    def get_object(self, pk):
        try:
            root = AboutUsModel.objects.get(pk=pk)
        except:
            raise NotFound(f'{pk}-chi iddagi malumot topilmadi')
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = get_one_about(self.get_object(pk))
        else:
            result = about_pag(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(requests.data)

        return Response(about_format(data))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        data = requests.data
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        if "image1" in requests.data:
            serializer.image1 = requests.data.get('image1')
        if "image2" in requests.data:
            serializer.image2 = requests.data.get('image2')
        data = serializer.save()

        return Response(about_format(data))

    def delete(self, requests, pk, *args, **kwargs):
        root = AboutUsModel.objects.get(pk=pk)
        root.delete()
        return Response({"Success": f"{root.title} muoffaqiyatli o'chirildi"})
