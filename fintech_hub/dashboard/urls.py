from django.urls import path
from .views import *
from dashboard.courses import views as c_views
from dashboard.teachers import views as t_views
from dashboard.fact import views as f_views
from dashboard.partner import views as part_views
from dashboard.about_us import views as about_views
from dashboard.registiratsiya import views as reg_views
from dashboard.comment import views as com_views
from dashboard.contact import views as con_view

urlpatterns = [
    path("", index, name='dashboardHome'),
    path("teacher/", t_views.teacher_list, name='dash_tables'),
    path("teacher/edit/<int:pk>/", t_views.edit_teacher, name='dash_teacher_edit'),
    path("teacher/add/", t_views.add_teacher, name='dash_teacher_add'),
    path("teacher/delete/<int:pk>", t_views.delete_teacher, name='dash_teacher_delete'),
    path('teacher/delete/<int:dlt>/', t_views.delete_teacher, name="dash_teacher_delete"),

    path("courses/", c_views.courses_lists, name='dash_courses'),
    path("courses/add/", c_views.add, name='dash_courses_add'),
    path("courses/detail/<int:pk>/", c_views.courses_lists, name='dash_courses_detail'),
    path("courses/edit/<int:pk>/", c_views.edit, name='dash_courses_edit'),
    path("courses/delete/<int:pk>", c_views.delete_courses, name='dash_courses_delete'),
    path('courses/delete/<int:dlt>/', c_views.delete_courses, name="dash_courses_delete"),

    path("fact/", f_views.fact_list, name='dash_facts_list'),
    path("fact/add", f_views.add, name='dash_fact_add'),
    path("fact/edit/<int:pk>/", f_views.edit_fact, name='dash_fact_edit'),
    path("fact/delete/<int:pk>", f_views.delete_fact, name='dash_fact_delete'),
    path('fact/delete/<int:dlt>/', f_views.delete_fact, name="dash_fact_delete"),

    path("partner", part_views.partner_list, name="dash_partner_list"),
    path("partner/add", part_views.partner_add, name="dash_partner_list_add"),
    path("partner/edit/<int:pk>/", part_views.part_edit, name="dash_partner_list_edit"),
    path("partner/delete/<int:pk>", part_views.part_delete, name='dash_partner_delete'),
    path('partner/delete/<int:dlt>/', part_views.part_delete, name="dash_partner_delete"),

    path("about_us", about_views.about_us, name="dash_about_us"),
    path("about_us/form", about_views.about_form, name="dash_about_us_form"),
    path("about_us/edit/<int:pk>/", about_views.about_edit, name="dash_about_us_edit"),
    path("about_us/delete/<int:pk>", about_views.delete_about, name='dash_about_us_delete'),
    path('about_us/delete/<int:dlt>/', about_views.delete_about, name="dash_about_us_delete"),

    path("register/register", reg_views.register, name="dash_register_reg"),
    path("register/add", reg_views.register_add, name="dash_register_add"),
    path("register/edit/<int:pk>/", reg_views.register_edit, name="dash_register_edit"),
    path("register/", register, name="dash_register"),
    path("register/delete/<int:pk>", reg_views.delete_register, name='dash_register_delete'),
    path('register/delete/<int:dlt>/', reg_views.delete_register, name="dash_register_delete"),

    path('comment/', com_views.comment, name='dash_comment'),
    path('comment/add/', com_views.commend_add, name='dash_comment_add'),
    path('comment/edit/<int:pk>/', com_views.commend_edit, name='dash_comment_edit'),
    path("comment/delete/<int:pk>", com_views.delete_about, name='dash_comment_delete'),
    path('comment/delete/<int:dlt>/', com_views.delete_about, name="dash_comment_delete"),

    path('contact/', con_view.contact_handler, name='dash_contact'),
    path('contact/add', con_view.contact_add, name='dash_contact_add'),
    path('contact/edit/<int:pk>/', con_view.edit, name='dash_contact_edit'),
    path("contact/delete/<int:pk>", con_view.delete_contact, name='dash_contact_delete'),
    path('contact/delete/<int:dlt>/', con_view.delete_contact, name="dash_contact_delete"),

    path('login/', dash_login, name='dash_login'),
    path('login/logout', dash_logout, name='dash_logout'),
    path('account/', account, name='dash_account'),
    path('passwordChange', changePassword, name='dash_password_change')

]
