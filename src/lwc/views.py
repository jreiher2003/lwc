from django.shortcuts import render
from joins.forms import EmailForm, JoinForm

def home(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        # new_join.save()
    context = {"form":form}
    return render(request, "home.html", context)



# def home(request):
#     form = EmailForm(request.POST or None)
#     if form.is_valid():
#         email = form.cleaned_data['email']
#         new_join, created = Join.objects.get_or_create(email=email)
#     context = {"form":form}
#     return render(request, "home.html", context)