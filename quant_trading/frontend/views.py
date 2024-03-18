from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StockForm, SimulationForm
from django_tables2 import SingleTableView
from .tables import StocksTable
from .models import Stocks, Images, Results
from .scripts.cerebro_runner import exec
from .scripts.stocks_from_xlsx import check_if_listed, fetch_and_write_stocks
from .strategies.example_strategy import TestStrategy 
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SimulationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL
            # call function
            
            # check_if_listed('Short_reports_data.xlsx')
            # fetch_and_write_stocks('stocks_with_listings.xlsx')

            #TODO get strategy from formy
            simulation = form.save()
            fig = exec(TestStrategy)
            name = "{}_{}.png".format(simulation.strategy,simulation.id) 
            path = settings.MEDIA_ROOT + name
            fig.savefig(path, format="png")
            img = Images()
            img.image.name = name
            img.save()
            result = Results(simulation=simulation, image=img)
            result.save() 

            return render(request,'results/result.html',{'result_data': result})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimulationForm()
    return render(request, "simulation_form.html", {"form": form})
    

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
