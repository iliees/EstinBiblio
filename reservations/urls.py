from django.urls import path
from .views import reserve_book, ReservationListView, ReservationDetailView

urlpatterns = [
    path('books/<int:book_id>/reserve/', reserve_book),
    path('reservations/', ReservationListView.as_view(), name='reservation_list'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
]
