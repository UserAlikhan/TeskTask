import logging

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Lesson_view, Product
from .models import User

logger = logging.getLogger(__name__)
# Create your views here.
def home(request):

    all_users = User.objects.all()
    context = {
        'all_users': all_users,
    }

    return render(request, 'testTask/index.html', context)

def user_request(request, name):
    return HttpResponse('<h2>User name:' + name + '</h2>')

class LessonViewListAPIView(APIView):
    def get(self, request, person_name):
        lessons_view_info = Lesson_view.objects.all()
        serialized_lessons = []
        for lesson_view in lessons_view_info:
            if str(lesson_view.lesson_id.product_id.owner.name) == person_name:
                serialized_lessons.append({
                    'Product': lesson_view.lesson_id.product_id.product_name,
                    'Lesson': lesson_view.lesson_id.name,
                    'Person_Name': lesson_view.lesson_id.product_id.owner.name,
                    'Lesson_Name': lesson_view.lesson_id.name,
                    'Watched_time': lesson_view.date_time_field.strftime("%d %B %Y %H:%M"),
                    'Viewed_time': lesson_view.viewed_time,
                    'Status': lesson_view.status
                })

            else:
                logger.info('NONO!!')

        product_list = []

        for i in serialized_lessons:
            product_list.append(i['Product'])

        # print('PRDCTL', product_list)
        context = {
            'person_name': person_name,
            'lessons': serialized_lessons,
            'product_list': product_list
        }

        return render(request, 'testTask/products.html', context)

class ProductLessonsAPIVIEW(APIView):

    def get(self, request, person_name, product_name):
        lessons_view = Lesson_view.objects.all()
        serialized_lessons = []
        for lesson_item in lessons_view:
            if str(lesson_item.lesson_id.product_id.product_name) == product_name\
                    and str(lesson_item.lesson_id.product_id.owner.name) == person_name:
                serialized_lessons.append({
                    'Lesson_Name': lesson_item.lesson_id.name,
                    'Last_Viewed_Date': lesson_item.date_time_field.strftime("%d %B %Y"),
                    'Watched_Time': lesson_item.date_time_field.strftime("%H:%M"),
                    'Status': lesson_item.status
                })

        context = {
            'person_name': person_name,
            'lessons': serialized_lessons,
        }
        # return Response(serialized_lessons)
        return render(request, 'testTask/lessons_access.html', context)

class ProductStatisticsAPIView(APIView):

    def get(self, request):
        products = Product.objects.all()
        product_statistics = []

        for product in products:
            total_lessons_viewed = Lesson_view.objects.filter(lesson_id__product_id=product).count()
            total_time_watched = Lesson_view.objects.filter(lesson_id__product_id=product).aggregate(
                total_watched_time=Sum('viewed_time'))['total_watched_time']

            total_students = Product.objects.filter(id=product.id).values('owner__id').distinct().count()

            purchase_percentage = (total_students / User.objects.count()) * 100 if User.objects.count() > 0 else 0

            product_statistics.append({
                'product_id': product.id,
                'product_name': product.product_name,
                'total_lessons_viewed': total_lessons_viewed,
                'total_time_watched': total_time_watched,
                'total_students': total_students,
                'purchase_percentage': purchase_percentage
            })

        context = {
            'product_statistics': product_statistics
        }

        return render(request, 'testTask/statistic.html', context)
        # return Response(product_statistics)

