from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api2.v1.sayt.contact.services import contact_format, contact_pag, get_one_contact
from apps.contact.models.contact import ContactModel
from .serializer import ContactSerializer


class ContactView(GenericAPIView):
    serializer_class = ContactSerializer

    def get_object(self, pk):
        try:
            root = ContactModel.objects.get(pk=pk)
        except:
            raise NotFound(f'{pk}-chi iddagi malumot topilmadi')
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = get_one_contact(self.get_object(pk))
        else:
            result = contact_pag(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(requests.data)

        return Response(contact_format(data))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        data = requests.data
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response(contact_format(data))

    def delete(self, requests, pk, *args, **kwargs):
        root = ContactModel.objects.get(pk=pk)
        root.delete()
        return Response({"Success": "Contact malumotlari muoffaqiyatli o'chirildi"})
