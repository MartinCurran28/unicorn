[![Build Status](https://travis-ci.org/MartinCurran28/bedbug.svg?branch=master)](https://travis-ci.org/MartinCurran28/bedbug)

def debug_detail(request, pk):
    debug = get_object_or_404(Debug, pk=pk)
    debug.views += 1
    debug.save()
    return render(request, "debug_details.html", {'debug': debug})    
    
 url(r'^(?P<pk>\d+)/$', debug_detail, name='debug_detail'),    
 
 
Like button functionality credit -  https://stackoverflow.com/questions/36014336/django-like-button-dosent-increment-and-redirect-me-to-the-same-page