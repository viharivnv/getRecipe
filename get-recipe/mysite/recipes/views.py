from django.shortcuts import render
import requests
# Create your views here.


def search(request):
    temp={}
    if request.method=='POST':
        type=request.POST.get('search')
        val=request.POST.get('Val')
        url = 'https://www.themealdb.com/api/json/v1/1/search.php?s={}'.format(val)
        temp = requests.get(url)
        try:
            temp=temp.json()
            temp=temp['meals'][0]
        except:
            data=[
                {
                'message':'Recipe not found. Please Try any other'
                }
            ]
            context = {
                'data': data
            }
            return render(request, 'recipes/search.html')

    else:
        return render(request, 'recipes/search.html')

    data=[
        temp
    ]
    context={
        'data':data
    }

    return render(request, 'recipes/results.html',context)
