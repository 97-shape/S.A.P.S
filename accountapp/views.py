from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.list import MultipleObjectMixin

from accountapp.customForm import CustomUserCreationForm
from accountapp.decorators import account_ownership_required
from database.models import UserData, Device

from django.shortcuts import render

has_ownershp = [account_ownership_required, login_required]

# Create your views here

class AccountCreateView(CreateView):
    model = UserData
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = UserData
    context_object_name = 'target_user'
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        object_list = Device.objects.all()
        context = super().get_context_data(object_list=object_list, **kwargs)
        # print(context)
        return context

@method_decorator(has_ownershp, 'get')
@method_decorator(has_ownershp, 'post')
class AccountUpdateView(UpdateView):
    model = UserData
    context_object_name = 'target_user'
    template_name = "update.html"
    success_url = reverse_lazy('dashboardapp:main')
    fields = ['name', 'phone_number', 'email']

    def get_context_data(self, **kwargs):
        object_list = Device.objects.all()
        context = super().get_context_data(object_list=object_list, **kwargs)
        # print(context)
        return context

@method_decorator(has_ownershp, 'get')
@method_decorator(has_ownershp, 'post')
class AccountDeleteView(DeleteView):
    model = UserData
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'delete.html'