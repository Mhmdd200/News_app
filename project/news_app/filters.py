from django_filters import rest_framework as filters
from news_app.models import Article
class ArticleFilter(filters.FilterSet):
    status = filters.CharFilter(field_name="status")
    view_count_lt = filters.NumberFilter(field_name="view_count", lookup_expr="lt")
    view_count_gt = filters.NumberFilter(field_name="view_count", lookup_expr="gt")
    published_date_lt = filters.DateFilter(field_name="published_date", lookup_expr='lt')
    published_date_gt = filters.DateFilter(field_name="published_date", lookup_expr="gt")
    class Meta:
        model = Article
        fields = ['status', 'view_count', 'published_date']