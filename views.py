from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm 
from django.contrib import messages 
# Create your views here.

def posts_create(Request):
	form = PostForm(Request.POST or None)
	# if Request.method == "POST":
	# 	print Request.POST.get("Content")
	# 	print Request.POST.get("Title")
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("Title")
		instance.save()
		messages.success(Request,"Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(Request,"Not Successfully created")
	context = {
		"form" : form
	}
	return render (Request,"Post_Form.html",context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.Title,
		"obj": instance,
	}
	return render(request, "post_det.html", context)



def posts_update(Request,id=None):
	obj = get_object_or_404(Post,id=id)
	form = PostForm(Request.POST or None,instance=obj)
	# if Request.method == "POST":
	# 	print Request.POST.get("Content")
	# 	print Request.POST.get("Title")
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("Title")
		instance.save() 
		messages.success(Request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context={
	"title" : obj.Title,
	"obj" : obj,
	"form": form
	}
	return render (Request,"post_Form.html",context)
def posts_list(Request):
	queryset = Post.objects.all()
	context={
	"object_List" : queryset,
	"title" : "List"
	}
	# if Request.user.is_authenticated():
	# 	context={
	# 	"title" : " User List"
	# 	}
	# else:
	# 	context={
	# 	"title" : "List"
	# 	}	
	return render (Request,"index.html",context)
	# return HttpResponse("<h1>Hello</h1>")
def posts_delete(Request):
	return HttpResponse("<h1>delete</h1>")
