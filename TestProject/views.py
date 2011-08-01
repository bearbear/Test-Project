from django.http import *
import datetime

def hello(request):
    return HttpResponse("<h1>Hello, &lt;i&gt;World&lt;/i&gt;!</h1>")

def current_datetime(request):
    t = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" %t
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

