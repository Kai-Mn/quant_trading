from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse  
from .forms import StockForm, SimulationForm
from django_tables2 import SingleTableView
from django.views.generic import TemplateView, CreateView
from .tables import StocksTable, ResultsTable, CompaniesTable
from .models import Stocks, Images, Results, Companies, Simulations
from .scripts.cerebro_runner import exec
from .scripts.utils import model_to_csv
from .strategies.example_strategy import TestStrategy 
from django.conf import settings
from django.urls import reverse
import csv
import os
import zipfile
import io


    
# Create your views here.
def index(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SimulationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            simulation = form.save()
            fig = exec(TestStrategy,form.data['company'])
            name = "{}_{}.png".format(simulation.strategy,simulation.id) 
            path = settings.MEDIA_ROOT + name
            fig.savefig(path, format="png")
            img = Images()
            img.image.name = name
            img.save()
            result = Results(simulation=simulation, image=img)
            result.save() 
            
            return redirect(reverse('result_detail', kwargs={'result_id':result.id}))

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

class CompaniesListView(SingleTableView):
    model = Companies
    table_class = CompaniesTable
    template_name = 'companies.html'

    def post(self, request, *args, **kwargs):
        ids = list(map(lambda x: int(x), request.POST.getlist("id")))
        # Folder name in ZIP archive which will contain the files
        zip_subdir = "stock_data"
        zip_filename = "%s.zip" % zip_subdir
        # Open StringIO to grab in-memory ZIP contents
        s = io.BytesIO()
        # The zip compressor
        zf = zipfile.ZipFile(s, "w")
        # Loop trough ids and write the date into zip
        for id in ids:
            stock = Stocks.objects.filter(type = id)
            csv_file = model_to_csv(stock,['date','adj_close'])
            stock_name = Companies.objects.get(id = id).name
            file_name = "{0}.csv".format(stock_name)
            zip_path = os.path.join(zip_subdir, file_name)
            # Add file, at correct path
            zf.writestr(zip_path,csv_file.getvalue())

        # Must close zip for all contents to be written
        zf.close()

        # Grab ZIP file from in-memory, make response with correct MIME-type
        response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
        # ..and correct content-disposition
        response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

        return response

class ResultsListView(SingleTableView):
    model = Results
    table_class = ResultsTable
    template_name = 'results.html'

class ResultDetailView(TemplateView):
    template_name = 'result_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_url'] = Results.objects.get(id = kwargs['result_id']).image.image.url
        print(kwargs)
        return context
