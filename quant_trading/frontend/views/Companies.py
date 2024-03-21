
class TableView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = Simple.objects.all()
    template_name = "simple_list.html"