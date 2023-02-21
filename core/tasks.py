from openpyxl import Workbook
from core.models import Sale
from celery import shared_task


@shared_task(
        bind=True,
        max_retries=5,
        default_retry_delay=30)
def create_report_of_sale(self):
    try:
        wb = Workbook()
        ws = wb.active
        ws.append(["ID", "Criado Em", "Total","Vendedor","Roupas", "Quantidade de Roupas"])
        
        sales = Sale.objects.prefetch_related("items")
        
        for sale in sales:
            date = sale.created_at.strftime('%Y-%m-%d')
            items = []
            for item in sale.items.all():
                items.append(item.clothe.name)
            
            ws.append([sale.pk,date,sale.total, sale.saller.name, str(items), len(items)])

        wb.save("sample.xlsx")
    except:
        raise self.retry()
