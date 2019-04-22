def debug_detail(request, pk):
    debug = get_object_or_404(Debug, pk=pk)
    debug.views += 1
    debug.save()
    return render(request, "debug_details.html", {'debug': debug})    
    
 url(r'^(?P<pk>\d+)/$', debug_detail, name='debug_detail'),    