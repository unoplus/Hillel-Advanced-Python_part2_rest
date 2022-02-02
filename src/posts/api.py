from django.http import JsonResponse


def posts(request):
    data = {
        "posts": [
            {"id": 1, "title": "Post1", "content": "some content", "author": "admin"},
            {"id": 2, "title": "Post2", "content": "some content", "author": "anonimus"},
        ]
    }
    return JsonResponse(data)
