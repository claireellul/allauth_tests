from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):

    return render_to_response("larb/index.html",
                              RequestContext(request))

# test if we can redirect to another page rather than the index.html
def test(request):

    return render_to_response("larb/test.html",
                              RequestContext(request))