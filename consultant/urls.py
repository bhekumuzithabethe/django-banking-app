from django.urls import path
from .views import (
    consultant,
    consultant_client_transactions_view,

    add_account,
    update_account,
    manage_accounts,
    delete_account,

    add_client,
    update_client,
    manage_clients,
    delete_client,

    add_card,
    update_card,
    manage_cards,
    delete_card,
    update_profile,
    )
urlpatterns = [

    path('home/',consultant,name='consultant'),

    path('add-client/',add_client,name='add-client'),
    path('manage-clients/',manage_clients,name='manage-clients'),
    path('update-client/<int:id>/',update_client,name='update-client'),
    path('delete-client/<int:id>/',delete_client,name='delete-client'),

    path('add-account/',add_account,name='add-account'),
    path('manage-accounts/',manage_accounts,name='manage-accounts'),
    path('update-account/<int:id>/',update_account,name='update-account'),
    path('delete-account/<int:id>/',delete_account,name='delete-account'),

    path('add-card/',add_card,name='add-card'),
    path('manage-cards/',manage_cards,name='manage-cards'),
    path('update-card/<int:id>/',update_card,name='update-card'),
    path('delete-card/<int:id>/',delete_card,name='delete-card'),

    path('client-account/<int:id>/',consultant_client_transactions_view,name='client-account'),
    path('update-consultant-profile/<int:id>/',update_profile,name='update-consultant-profile'),


]
