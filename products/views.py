from django.core.checks import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.db.models import Q
# from .forms import AddReviewForm
from .models import Waters, Review, CategoryWaters


class WaterListView(ListView):
    model = Waters
    template_name = 'water/water_list.html'


# class WaterListView(View):
#     def get(self, request):
#         water = Waters.objects.all().order_by('-id')
#         return render(request, 'water/water_list.html', {'water': water})


class WaterListView(View):
    def get(self, request):
        water = Waters.objects.all().order_by('-id')
        water_author = Waters.objects.all()
        search_post = request.GET.get('search')
        if search_post:
            water = Waters.objects.filter(
                Q(name__icontains=search_post)
                # Q(price_incontains=search_post)
            )
            if not water:
                messages.warning(request, 'No results found')
                return render(request, 'water/water_list.html', {'water': water})

        return render(request, 'water/water_list.html', {'water_author': water_author})


class WaterDetailView(View):
    def get(self, request, pk):
        water = Waters.objects.get(pk=pk)
        rewiews = Review.objects.filter(water=pk)
        category_waters = Waters.objects.filter(category=water.category.pk)
        # print(category_waters)
        context = {
            'water': water,
            'reviews': rewiews,
            'category_water': category_waters
        }
        return render(request,'water/water_detail.html', context=context)


class WaterCreateView(CreateView):
    model = Waters
    template_name = 'water/water_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:water_list')


class WaterDeleteView(DeleteView):
    model = Waters
    template_name = 'water/water_delete.html'
    success_url = reverse_lazy('products:water_list')


# class AddReviewView(LoginRequiredMixin, View):
#     def get(self, request, pk):
#         add_review_form = AddReviewForm()
#         return render(request, 'water/water_detail.html', {'add_review_form': add_review_form})
#

class CategoriesListView(View):
    def get(self, request):
        categorys = CategoryWaters.objects.all()
        return render(request, 'products.html',{'categorys': categorys})

