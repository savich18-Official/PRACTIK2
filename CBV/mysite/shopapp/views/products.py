from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from shop.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(archived=False)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'discount']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'discount']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductArchiveView(View):
    template_name = 'products/product_confirm_archive.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.archived = True
        product.save()
        return redirect('product_list')
