from rest_framework.pagination import PageNumberPagination


class Paginationz(PageNumberPagination):
    page_size_query_param = 'limit'
