from django.urls import path
from .views import (
    admin,
    admin_client_transactions_view,

    manage_users,
    delete_user,

    add_account,
    update_account,
    manage_accounts,
    delete_account,

    add_client,
    update_client,
    manage_clients,
    delete_client,

    add_consultant,
    update_consultant,
    manage_consultants,
    delete_consultant,

    add_card,
    update_card,
    manage_cards,
    delete_card,
    update_admin_profile,
    )
urlpatterns = [

    path('home/',admin,name='adminpage'),

    path('manage-users/',manage_users,name='manage-users'),
    path('delete-user/<int:id>/',delete_user,name='delete-user'),

    path('add-client/',add_client,name='admin-add-client'),
    path('admin-manage-clients/',manage_clients,name='admin-manage-clients'),
    path('update-client/<int:id>/',update_client,name='admin-update-client'),
    path('delete-client/<int:id>/',delete_client,name='admin-delete-client'),

    path('add-consultant/',add_consultant,name='admin-add-consultant'),
    path('manage-consultants/',manage_consultants,name='admin-manage-consultants'),
    path('update-consultant/<int:id>/',update_consultant,name='admin-update-consultant'),
    path('delete-consultant/<int:id>/',delete_consultant,name='admin-delete-consultant'),

    path('add-account/',add_account,name='admin-add-account'),
    path('manage-accounts/',manage_accounts,name='admin-manage-accounts'),
    path('update-account/<int:id>/',update_account,name='admin-update-account'),
    path('delete-account/<int:id>/',delete_account,name='admin-delete-account'),

    path('add-card/',add_card,name='admin-add-card'),
    path('manage-cards/',manage_cards,name='admin-manage-cards'),
    path('update-card/<int:id>/',update_card,name='admin-update-card'),
    path('delete-card/<int:id>/',delete_card,name='admin-delete-card'),

    path('client-account/<int:id>/',admin_client_transactions_view,name='admin-client-account'),
    path('update-admin-profile/<int:id>/',update_admin_profile,name='update-admin-profile'),


]
