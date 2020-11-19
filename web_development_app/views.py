from django.shortcuts import render

# Create your views here.
def learn_html(request):
	return render(request, 'learn_html.html')

def nnetwork_html(request):
	return render(request, 'nnetwork.html')

def blog_html(request):
	return render(request, 'blog.html')

def learn_css(request):
	return render(request, 'learn_css.html')

def view_css(request):
	return render(request, 'style_copy.txt')

def sample_webpage(request):
	return render(request, 'sample_webpage.html')
