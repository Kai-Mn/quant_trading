from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StockForm
from django_tables2 import SingleTableView
from .tables import StocksTable
from .models import Stocks

# Create your views here.
def index(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        # import function to run
        from .scripts.cerebro_runner import exec
        
        # call function
        exec()
        
        # return user to required page
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def get_stock(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = StockForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/stocks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StockForm()

    return render(request, "stocks_form.html", {"form": form})

def show_stock(request):
    return render(request, 'stocks.html')


class StocksListView(SingleTableView):
    model = Stocks
    table_class = StocksTable
    template_name = 'stocks.html'
