from django.urls import path
from api2.v1.sayt.about_us.views import AboutView
from api2.v1.sayt.contact.views import ContactView
from api2.v1.sayt.courses.views import CoursesView
from api2.v1.sayt.partners.views import PartnersView
from api2.v1.sayt.teachers.views import TeachersView

urlpatterns = [
    path('sayt/about_us/', AboutView.as_view(), name="api_about_list"),
    path('sayt/about_us/<int:pk>/', AboutView.as_view(), name="api_about_one"),

    path('sayt/contact/', ContactView.as_view(), name="api_contact_one"),
    path('sayt/contact/<int:pk>/', ContactView.as_view(), name="api_contact_one"),

    path('sayt/courses/', CoursesView.as_view(), name="api_about_list"),
    path('sayt/courses/<int:pk>/', CoursesView.as_view(), name="api_about_one"),

    path('sayt/partners/', PartnersView.as_view(), name="api_partners_list"),
    path('sayt/partners/<int:pk>/', PartnersView.as_view(), name="api_partners_one"),

    path('sayt/teacher/', TeachersView.as_view(), name="api_teacher_list"),
    path('sayt/teacher/<int:pk>/', TeachersView.as_view(), name="api_teacher_one"),

]
