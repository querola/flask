from django.shortcuts import render

# Create your views here.
def list_posts(request):
    """List existing posts."""
    return render(request, 'Base.html')