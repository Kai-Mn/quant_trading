from django.conf import settings


def nav_bar(request):
    settings.MEDIA_ROOT
    nav_items = {
        'nav_items': [
            {'title': 'home', 'url': '/'},
            {'title': 'stocks', 'url': '/stocks'},
            {'title': 'companies', 'url': '/companies'},
            {'title': 'result', 'url': '/results'},
            {'title': 'get_stock', 'url': '/get_stock'}

        ]
    }
    return nav_items