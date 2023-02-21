from rest_framework.views import APIView
from core.tasks import create_report_of_sale
from rest_framework.response import Response

import time
# Create your views here.
class CreateReportToSale(APIView):

    def get(self, request):
        tb = time.time()
        create_report_of_sale.delay()
        ta = time.time()
        print(f"Tempo de Processamento:{ta-tb}")
        return Response(data={"msg":f"Relatório criado com sucesso !"},status=200)

