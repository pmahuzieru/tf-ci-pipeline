from django.http import JsonResponse

def ping(request):
    return JsonResponse({'ping': 'pong', "message": "hola"})