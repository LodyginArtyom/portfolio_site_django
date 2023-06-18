
from django.views.generic import ListView
from .models import Projects


class MovieView(ListView):

    model = Projects
    queryset = Projects.objects.filter(draft=False)
    template_name = "model/index.html"







