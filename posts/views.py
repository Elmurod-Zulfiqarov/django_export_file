from django.http import HttpResponse
from django.views.generic import ListView, FormView
from .models import Post
from .admin import PostResorce
from .forms import FormatForm

class PostListView(ListView, FormView):
    model = Post
    template_name = 'posts/main.html'
    form_class = FormatForm

    def post(self, request, **kwargs):
        qs = self.get_queryset()
        dataset = PostResorce().export(qs)

        format = request.POST.get('format')
        
        if format == 'xls':
            ds = dataset.xls     
        elif format == 'csv':
            ds  =dataset.csv
        else:
            ds = dataset.json
        
        response = HttpResponse(ds, content_type=f"{format}")
        response['Content-Disposition'] = f"attachment; filename=posts.{format}"
        return response

