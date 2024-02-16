# Import here
from . import models
from datetime import datetime, date, timedelta
from django.db.models import Sum, Avg, Count


def young_employees(job: str):
    return models.Employee.objects.filter(age__lt=30, job=job)


def cheap_products():
    average_price = models.Product.objects.all().aggregate(Avg('price'))['price__avg']
    products_below_avg = models.Product.objects.filter(price__lt=average_price).order_by('price').values_list('name', flat=True)

    return list(products_below_avg)


def products_sold_by_companies():
    return models.Company.objects.annotate(sold=Sum('product__sold')).values_list('name', 'sold')



def sum_of_income(start_date: str, end_date: str):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    total_revenue = models.Order.objects.filter(time__range=(start_date, end_date)).aggregate(total=Sum('price'))['total']
    return total_revenue or 0


def good_customers():
    one_month_ago = date.today() - timedelta(days=30)
    return models.Customer.objects.filter(
                                    level='G',
                                    # order__time__gte=one_month_ago
                                ).annotate(
                                    purchases_count=Count('order')
                                ).filter(
                                    purchases_count__gt=10
                                ).values_list('name', 'phone', named=True)


def nonprofitable_companies():
    return models.Company.objects.annotate(
                            low_sold_products_count=Count(
                                'product',
                                filter=models.Product.objects.filter(sold__lt=100)
                            )
                        ).filter(
                            low_sold_products_count__gte=4
                        ).values_list('name', flat=True)
