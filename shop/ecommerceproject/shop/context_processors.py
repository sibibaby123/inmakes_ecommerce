from .models import Category, Product


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)


def pod_links(request):
    lists = Product.objects.all()
    return dict(lists=lists)
