from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum

from .forms import DriverCreationForm, DriverUpdateForm, CarCreateForm
from .models import Driver, Car, Manufacturer

PAGINATED_BY = 3
DAYS = 30
PERCENT = 0.35
DAYS_MIN = 70
DAYS_MAX = 100
AWARD_MIN = 1.2
AWARD_MIDDLE = 1.3
AWARD_MAX = 1.45


@login_required
def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    paginate_by = PAGINATED_BY


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = PAGINATED_BY
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = PAGINATED_BY
    context_object_name = "driver_list"


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


class DriverCreateView(LoginRequiredMixin, generic.CreateView):
    model = Driver
    form_class = DriverCreationForm
    success_url = reverse_lazy("taxi:driver-list")


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    form_class = CarCreateForm
    success_url = reverse_lazy("taxi:car-list")


class DriverDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Driver
    success_url = reverse_lazy("taxi:driver-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class CarUpdateView(generic.UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class DriverUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Driver
    form_class = DriverUpdateForm
    template_name = "taxi/driver_license_update.html"
    success_url = reverse_lazy("taxi:car-list")


class Search(generic.ListView):
    paginate_by = 3

    def get_queryset(self):
        return Manufacturer.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context


def get_salary(request, pk):
    if Driver.objects.filter(trip__license_number=pk).exists():
        queryset = Driver.objects.filter(trip__created_at__gte=timezone.now() - timedelta(days=DAYS))
        if queryset:
            rides_per_month = queryset.annotate(num_rides=Count("trip")).get(id=pk).num_rides
            money_per_month = queryset.annotate(num_money=Sum("trip__price")).get(id=pk).num_money
            salary = money_per_month * PERCENT
            if rides_per_month > DAYS_MIN:
                salary *= AWARD_MIN
            if DAYS_MIN <= rides_per_month < DAYS_MAX:
                salary *= AWARD_MIDDLE
            if rides_per_month >= DAYS_MAX:
                salary *= AWARD_MAX
        else:
            salary = 0
    else:
        salary = 0
    context = {
        "driver": Driver.objects.get(id=pk),
        "salary": salary
    }
    return render(request, "taxi/driver_salary.html", context=context)
