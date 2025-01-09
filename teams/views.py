from django.http import JsonResponse

# Exemplo de view para a lista de times
def teams_view(request):
    data = {
        "teams": [
            {"name": "Brasil", "titles": 5},
            {"name": "Alemanha", "titles": 4},
            {"name": "Itália", "titles": 4},
        ]
    }
    return JsonResponse(data)
