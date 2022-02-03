from django.urls import path


from api import views

urlpatterns =[
    path('transactions/',views.TransactionList.as_view()),
    path('transactions/<int:pk>/',views.TransactionDetail.as_view())
]