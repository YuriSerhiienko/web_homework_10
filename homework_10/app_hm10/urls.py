from django.urls import path
from . import views

app_name = "app_hm10"

urlpatterns = [
    path("", views.main, name="main"),
    path("add_author/", views.add_author, name="add_author"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path("quotes/", views.quote_list, name="quote_list"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("tags/<int:tag_id>/", views.tag_detail, name="tag_detail"),
]
