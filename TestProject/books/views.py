# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from django.shortcuts import render_to_response
from django.http import *
from TestProject.books.models import *
import datetime


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors })
    
publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list.html',
    'template_object_name': 'publisher',
    'extra_context': {'book_list': Book.objects.all()}
}

book_info = {
    'queryset': Book.objects.order_by('-publication_date'),
    'template_name': 'book_list.html',
    'template_object_name': 'book',
}

def books_by_publisher(request, name):

    # Look up the publisher (and raise a 404 if it can't be found).
    publisher = get_object_or_404(Publisher, name__iexact=name)

    # Use the object_list view for the heavy lifting.
    return list_detail.object_list(
        request,
        queryset = Book.objects.filter(publisher=publisher),
        template_name = 'books_by_publisher.html',
        template_object_name = 'book',
        extra_context = {'publisher': publisher}
    )

def author_detail(request, author_id):
    # Delegate to the generic view and get an HttpResponse.
    response = list_detail.object_detail(
        request,
        queryset = Author.objects.all(),
        template_name = 'author_list.html',
        template_object_name = 'author',
        object_id = author_id,
    )

    # Record the last accessed date. We do this *after* the call
    # to object_detail(), not before it, so that this won't be called
    # unless the Author actually exists. (If the author doesn't exist,
    # object_detail() will raise Http404, and we won't reach this point.)
    now = datetime.datetime.now()
    #Author.objects.filter(id=author_id).update(last_accessed=now)
    return response