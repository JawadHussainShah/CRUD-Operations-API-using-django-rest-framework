from django.views import View
from django.views.generic.base import TemplateView,RedirectView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import StudentRegistration
from .models import User

# Create your views here.
# Add and show data
class UserDataView(TemplateView):
    template_name = 'enroll/addshow.html'
    def get_context_data(self, **kwargs):
        fmr = StudentRegistration()
        stud = User.objects.all()
        context = super().get_context_data(**kwargs)
        context = {'form':fmr, 'st':stud}
        return context

    def post(self, request):
        fmr = StudentRegistration(request.POST)
        if fmr.is_valid():
            nm = fmr.cleaned_data['name']
            em = fmr.cleaned_data['email']
            pw = fmr.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            messages.add_message(request,messages.ERROR,'Data added successfully!')
            return HttpResponseRedirect('/')

# update data
class UpdateOrEdit(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/update.html',{'form':fm})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()   
            messages.success(request, 'Data Updated Successfully!!!')
        return render(request, 'enroll/update.html',{'form':fm})

# def update_data(request,id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(instance=pi)
#     return render(request, 'enroll/update.html',{'form':fm})

# delete data
class Delte(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)