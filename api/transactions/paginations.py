from rest_framework.pagination import PageNumberPagination

class TransactionPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 1000