from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_view(request):
	return render(request, 'gringotts/base.html')


def transfer(request):
	if request.GET:
		x = request.GET['id']
		render(request, 'http://api.reimaginebanking.com/accounts/%s/transfers?key=73773e58efaba48db97f6f32c3f89f51'%(x) )

	return render(request, 'gringotts/base.html')
		


