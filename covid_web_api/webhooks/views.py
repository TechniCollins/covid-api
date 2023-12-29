from django.urls import path, include
from webhooks.models import Case
from rest_framework import serializers, viewsets

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ["date", "state", "tcin", "tcfn", "cured", "death"]

class CaseViewSet(viewsets.ModelViewSet):
    # Override get_queryset method
    def get_queryset(self):
        field_name = self.request.query_params.get('field_name', 'death')
        query = self.request.query_params.get('query', 'gt')
        value = self.request.query_params.get('value', 148500)

        # Formulate query from URL query parameters
        filters = {
            f"{field_name}__{query}" : value
        }

        queryset = Case.objects.filter(**filters)
        # Example queries
        # Select where death count is greater than 100 -> death__gt=100
        # Other handy queries -> gte, lt, lte

        # Select data within a specified date range
        # start_date = datetime.date(2022, 12, 12)
        # end_date = datetime.date(2023, 12, 12)
        # Case.objects.filter(date__range=(start_date, end_date))

        # Dynamic queries: https://stackoverflow.com/a/310785
        return queryset


    serializer_class = ClientSerializer
