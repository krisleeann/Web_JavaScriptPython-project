from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("listing", views.listing, name="listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("register", views.register, name="register"),
    path("listing_inactive", views.listing_inactive, name="listing_inactive"),
    path("create_event", views.create_event, name="create_event"),
    path("events", views.events, name="events"),
    path("events/<int:event_id>", views.events, name="events"),
    path("category/<str:category>", views.category, name="category")
]
