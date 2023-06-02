from django.shortcuts import render

# Create your views here.

from .models import Repair
from .forms import RepairModelForm


def index(request):
    return render(request, "index.html")


def repairs(request):
    form = RepairModelForm()
    if request.method == "POST":
        form = RepairModelForm(request.POST, request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.save()
    context = {
        "repairs": Repair.objects.filter(user=request.user, car__type="Sedan"),
        "form": form
    }
    return render(request, "repair.html", context=context)
