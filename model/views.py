
from django.views.generic import ListView
from .models import Projects, Language, Libraries


class MovieView(ListView):

    model = Projects
    queryset = Projects.objects.filter(draft=False)
    template_name = "model/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['languages'] = Language.objects.all()
        context['libraries'] = Libraries.objects.all()
        return context







