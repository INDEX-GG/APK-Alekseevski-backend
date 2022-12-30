from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from apps.vacancies.serializers import VacancySerializer, ApplicationVacancySerializer
from apps.vacancies.models import Vacancy
from apps.vacancies.utils import Util


class VacancyAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all().order_by('-pk')
    serializer_class = VacancySerializer


class ApplicationVacancyAPIView(generics.CreateAPIView):
    serializer_class = ApplicationVacancySerializer
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        created = Util.send_mail(data)
        if created:
            return Response({'result': True}, status=status.HTTP_200_OK)
        else:
            return Response({'result': False, 'email': ['Ошибка отправления']}, status=status.HTTP_404_NOT_FOUND)
