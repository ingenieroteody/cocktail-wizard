from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('signup/', views.user_signup),
    path('myaccount/<int:id>/', views.my_account),
    path('cocktails/', views.list_cocktails),
    path('cocktail/<int:id>/', views.view_cocktail),
    path('cocktail/<int:id>/confirm_delete/', views.confirm_delete_cocktail),
    path('cocktail/<int:id>/delete/', views.delete_cocktail),
]
