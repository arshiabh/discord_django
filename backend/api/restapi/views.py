from django.http import JsonResponse


def getRoutes(request):
    routes = [
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]

    return JsonResponse(getRoutes, safe=False)