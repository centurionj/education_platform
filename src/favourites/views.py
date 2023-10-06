from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect

from . models import CourseLike


@login_required
def favourite_add(request, course_id):
    CourseLike.update_or_create(user=request.user, course_id=course_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
