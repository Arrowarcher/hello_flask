from . import views
from ...utils import resource_path

# blueprint_urlpatterns = []

urlpatterns = [
    resource_path(views.AuthorAPI, "/authors/<author_id>", endpoint="author"),
    resource_path(views.AuthorListAPI, "/authors", endpoint="authorList")
]
