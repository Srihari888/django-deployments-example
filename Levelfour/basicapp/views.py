from django.shortcuts import render

# Create your views here.
def index(r):
    context_dict={'text':'Mohan hello','number':100}
    return render(r,'basicapp/index.html',context_dict)

def other(r):
    return render(r,'basicapp/other.html')
def relative(r):
    return render(r,'basicapp/relative_url.html')
