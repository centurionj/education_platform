from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.list import ListView

from .models import CourseLike


class FavouriteListView(ListView):
    """Вывод вишлиста в дашборде"""
    model = CourseLike
    template_name = 'favourites/favourites.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super(FavouriteListView, self).get_queryset()
        user_id = self.kwargs.get('user_id')
        return queryset.filter(user=user_id)


@login_required
def add_or_delete(request, course_id):
    CourseLike.objects.delete_or_create(user=request.user, course_id=course_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
