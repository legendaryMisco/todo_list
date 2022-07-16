from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from users.models import Register
from .models import Todo
from .forms import TodoForm
from datetime import datetime
from .utils import searchForm
from django.db.models import Q
from chats.models import Message
# Create your views here.

@login_required(login_url='login')
def Lists(request):
    todo, search = searchForm(request)
    context = {'todo':todo,'search':search}
    return render(request, 'todo/todolist.html',context)


@login_required(login_url='login')
def signleLists(request,pk):
    todo = Todo.objects.get(id=pk)
    context = {'todo':todo}
    return render(request, 'todo/single-list.html',context)


@login_required(login_url='login')
def addList(request):
    profile = request.user.register
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = profile
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'todo/add_list.html', context)


@login_required(login_url='login')
def updateList(request,pk):
    action = 'update'
    profile = request.user.register
    todo = profile.todo_set.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form, 'action':action}
    return render(request, 'todo/add_list.html', context)


@login_required(login_url='login')
def deleteList(request,pk):
    profile = request.user.register
    todo = profile.todo_set.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('account')
    context = {'obj':todo}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def messageList(request):
    profile = request.user.register
    message = Message.objects.all()
    today = datetime.now()
    todo = profile.todo_set.filter(time_reminder__lte=today)
    context = {'todo':todo,'profile':profile,'chats':message}
    return render(request, 'todo/inbox.html', context)






