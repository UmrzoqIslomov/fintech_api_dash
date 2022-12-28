from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api2.v1.sayt.partners.services import partners_format, partners_pag, get_one_partners
from apps.partners.models.partners import PartnersModel
from .serializer import PartnersSerializer


class PartnersView(GenericAPIView):
    serializer_class = PartnersSerializer

    def get_object(self, pk):
        try:
            root = PartnersModel.objects.get(pk=pk)
        except:
            raise NotFound(f'{pk}-chi iddagi malumot topilmadi')
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = get_one_partners(self.get_object(pk))
        else:
            result = partners_pag(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(requests.data)

        return Response(partners_format(data))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        data = requests.data
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        if "image1" in requests.data:
            serializer.image1 = requests.data.get('image1')
        data = serializer.save()

        return Response(partners_format(data))

    def delete(self, requests, pk, *args, **kwargs):
        root = PartnersModel.objects.get(pk=pk)
        root.delete()
        return Response({"Success": "Partners malumotlari muoffaqiyatli o'chirildi"})