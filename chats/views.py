from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from users.models import Register
from django.contrib import messages
from .forms import DmForm

# Create your views here.

@login_required(login_url='login')
def directMessage(request,pk):
    profile = request.user.register
    form = DmForm()
    receiver = Register.objects.get(id=pk)
    if request.method == 'POST':
        form = DmForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = profile
            message.receiver_id = receiver
            form.save()
            messages.success(request, 'message sent successfully')
            return redirect('find-friends')
    context = {'form':form}
    return render(request, 'chats/direct_message.html',context)


