from product.models import Product


class DatabaseProductRepository:

    @classmethod
    def search_products(cls, request):
        products = Product.objects.filter(name__icontains=request.data['search'])
        return products

    @classmethod
    def select_product(cls, request, pk):
        product = Product.objects.filter(id=pk).first()
        return product

    @classmethod
    def select_all_products(cls):
        products = Product.objects.filter().all()
        return products
