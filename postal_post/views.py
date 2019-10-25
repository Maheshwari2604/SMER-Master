from django.shortcuts import render
from .models import Postal
from django.http import HttpResponse

# Create your views here.
def get_postal(request):
    print('hy')
    if request.method == 'POST':
        print('in post')
        user = Postal()
        #user.project = request.GET['projectname']
        user.From = request.GET['From']
        user.To = request.GET['To']
        #user.typeofdel = request.GET['typeofdel']
        user.del_pin_no = request.GET['del_pin_no']
        #user.weightrate = request.GET['weightrate']
        user.Describe_del = request.GET['Describe_del']
        user.Full_area_address = request.GET['Full_area_address']
        #user.City = request.GET['paid']
        #user.slug = request.GET['paid']
        #print(user.paid)
        user.save()
        return HttpResponse("Created new order")
        # context = {
        #     'message': 'Thanks for Submission'
        # }
        # print("done")
        #return render(request , 'dbo/projectdetail.html', context)
    
    else:
        # context = {
        #     'message': 'Enter New Project'
        # }
        # print('in else')
        #return HttpResponse("NC new order:")
        print("in else")
        pass
    
    return render(request,'postal.html')

#def (request):