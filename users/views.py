from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.template.response import TemplateResponse

from .forms import AddUserForm
from .models import Users

# Create your views here.

class AllUsers(View):
    def get(self, request):
        users = Users.objects.all()
        context = {"users": users}
        return render(request, "all_users.html", context)


class AddUser(View):
    def get(self, request):
        form = AddUserForm()
        context = {
            'form': form,
        }
        return TemplateResponse(request, "add_user_form.html", context)

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_users')
        context = {
            'form': form,
        }
        print(form.errors)
        return render(request, "add_user_form.html", context)
    

class DeleteUser(View):
    def get(self, request, user_id):
        user = get_object_or_404(Users, id=user_id)
        user.delete()
        return redirect("all_users")
    

class EditUser(View):
    def get(self, request, user_id):
        user = Users.objects.get(id=user_id)
        form = AddUserForm(instance=user)
        context = {
            'form': form,
            "user": user,
        }
        return TemplateResponse(request, "edit_user_form.html", context)

    def post(self, request, user_id):
        user = Users.objects.get(id=user_id)
        form = AddUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all_users')
        context = {
            'form': form,
            "user": user,
        }
        print(form.errors)
        return render(request, "edit_user_form.html", context)