def nav_bar(request):
    nav_items = {
        'nav_items': [
            {'title': 'home', 'url': '/'},
            {'title': 'stocks', 'url': '/stocks'},
            {'title': 'result', 'url': '/results'}
        ]
    }
    return nav_items