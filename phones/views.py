from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    sorting = request.GET.get('sort')
    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    if sorting:
        context_val = Phone.objects.all().order_by(SORT_MAP[sorting])
    else:
        context_val = Phone.objects.all()
    return render(request, 'catalog.html', {'phones': context_val})


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug).first()}
    return render(request, template, context)
