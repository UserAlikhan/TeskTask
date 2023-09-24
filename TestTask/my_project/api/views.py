from rest_framework.response import Response
from rest_framework.decorators import api_view
from testTask.models import Lesson_view, Lesson
from .serializers import LessonSerializer
import logging
from rest_framework import status
from rest_framework.views import APIView

logger = logging.getLogger(__name__)

@api_view(['GET'])
def getData(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addLesson(request):
    serializer = LessonSerializer(data=request.data)
    if serializer.is_valid():
        logger.info("DADADADADAADADA")
        serializer.save()
        return Response(serializer.data)
    else:
        logger.error(f'Serializer is not valid: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonViewListAPIView(APIView):
    def get(self, request, person_name):
        lessons_view_info = Lesson_view.objects.all()
        serialized_lessons = []
        for lesson_view in lessons_view_info:
            print()
            if str(lesson_view.lesson_id.product_id.owner.name) == person_name:
                serialized_lessons.append({
                    'Product': lesson_view.lesson_id.product_id.product_name,
                    'Lesson': lesson_view.lesson_id.name,
                    'Person_Name': lesson_view.lesson_id.product_id.owner.name,
                    'Lesson Name': lesson_view.lesson_id.name,
                    'Watched_time': lesson_view.date_time_field.strftime("%d %B %Y %H:%M"),
                    'Viewed_time': lesson_view.viewed_time,
                    'Status': lesson_view.status
                })

            else:
                logger.info('NONO!!')
        return Response(serialized_lessons)