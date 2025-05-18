from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, "base.html", {"error_code": 404, "error_message": "Page Not Found"}, status=404)

def custom_500_view(request):
    return render(request, "base.html", {"error_code": 500, "error_message": "Internal Server Error"}, status=500)

def custom_403_view(request, exception):
    return render(request, "base.html", {"error_code": 403, "error_message": "Forbidden Access"}, status=403)

def custom_400_view(request, exception):
    return render(request, "base.html", {"error_code": 400, "error_message": "Bad Request"}, status=400)
