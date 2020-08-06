
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('update/<int:id>',views.updateTodo,name="update"),
    path('delete/<int:id>',views.deleteTodo,name="delete"),

]