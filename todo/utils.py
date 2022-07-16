from django.db.models import Q
from .models import Todo
from users.models import Register
def searchForm(request):
    search = ''
    if request.GET.get('search_query'):
        search = request.GET.get('search_query')
    profile = request.user.register
    todo = profile.todo_set.filter(
       Q(title__icontains=search) |
       Q(body__icontains=search) |
       Q(time_reminder__startswith=search)
    )
    return todo,search