from django.http import HttpResponse
import datetime

def default(request):
    return HttpResponse("""
        <h1>Landing page</h1>
""")

def test(request):
    print("Test function")
    return HttpResponse("<h1>Test function</h1>")

def aboutus(request):
    print("Aboutus function")
    return HttpResponse("""
                        <div>
                            <h1>This is an aboutus page</h1>
                            <p>
                            This is a page that can be used 
                            to display aboutus and view 
                            more details
                            </p>
                        </div>""")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)