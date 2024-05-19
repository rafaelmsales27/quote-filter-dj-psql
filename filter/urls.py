from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="filter"),
    path("form/", views.form, name="form"),
    path("<int:question_id>/", views.detail, name="detail"),
]
