from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def compoff(request):
    days=45
    if request.method == "GET":
            return render(request,"compoff_calculation.html")
    else:
        input_date=request.POST['inputdate']
        print("##########################################################", type(input_date))

        compoff_expiry_date= datetime.strptime(input_date,"%Y-%m-%d") + timedelta(days)
        print("##########################################################")
        print( datetime.strftime(compoff_expiry_date,"%Y-%m-%d"))

        return render(request,"compoff_calculation.html" ,{"holiday":input_date,"compoff":datetime.strftime(compoff_expiry_date,"%Y-%m-%d")})
        