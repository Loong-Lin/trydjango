from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import ProductForm, RawProductForm
from .models import Product


def product_create_view(request):
    """
    用表单来创建Product
    """
    initial_data = {
        'title': " my title",
        'description': "The product is very well."
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data)  # instance = obj
    if form.is_valid():
        form.save()
        form = ProductForm()  # 表单保存后清空表单

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_update_view(request):
    pass


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request, why???
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def product_list(request):
    """
    list all products
    """
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "products/product_list.html", context)


def product_detail_view(request, id):
    # 展现产品的详细详细
    # product_obj = get_object_or_404(Product, id=id)
    try:
        product_obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    context = {"object": product_obj}
    return render(request, "products/product_detail.html", context)




"""
def product_create_view(request):
    #  用表单来创建Product
    form = ProductForm(requst.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # 表单保存后清空表单

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
"""