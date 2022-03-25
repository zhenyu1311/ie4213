from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import joblib
reloadModel =joblib.load('./models/predicter.pkl')
# Create your views here.

def index(request):
    temp={}
    temp['storey_range']='8 TO 12'
    temp['month']='2018-12'
    temp['flat_type']='2 ROOM'
    temp['floor_area_sqm']=44
    temp['flat_model']='Improved'
    temp['remaining_lease']='61 years 04 months'
    temp['block']='406'
    temp['street_name']='ANG MO KIO AVE 10'
    context={'temp':temp}
    return render(request,'index.html',context)

def predictHDB(request):
    print(request)
    if request.method == 'POST':
        temp={}
        temp['storey_range']=request.POST.get('storey_rangev')
        temp['month']=request.POST.get('monthv')
        temp['flat_type']=request.POST.get('flat_typev')
        temp['floor_area_sqm']=request.POST.get('floor_area_sqmv')
        temp['flat_model']=request.POST.get('flat_modelv')
        temp['remaining_lease']=request.POST.get('remaining_leasev')
        temp['block']=request.POST.get('blockv')
        temp['street_name']=request.POST.get('street_namev')
    testDtaa=pd.DataFrame({'x':temp}).transpose()
    scoreval=reloadModel.predict(testDtaa)[0]
    context={'scoreval':scoreval,'temp':temp}
    return render(request,'index.html',context)
  