from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Set
from .forms import SetForm


class SetListView(generic.ListView):
    model = Set
    template_name = 'index.html'
    paginate_by = 6


def set_list(request):
    set_list = Set.objects.all()

    return render(request, 'set_list.html', {
                      'set_list': set_list})


class update_set(View):
    
    def get(self, request, id, *args, **kwargs):
        
        set = get_object_or_404(Set, id=id)
        form = SetForm(request.POST or None, instance=set)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/set_list?submitted=True')


        return render(request, 'update_set.html', {'set': set, 'form': form},)


class show_set(View):
    
    def get(self, request, id, *args, **kwargs):
        
        set = get_object_or_404(Set, id=id)
    
        return render(request, 'show_set.html', {'title': set.title,
                                            'theme': set.theme,
                                            'featured_image': set.featured_image,
                                            'done': set.done,
                                            'description': set.description},)


def search(request):
    """ search function  """
    if request.method == "POST":
        searched = request.POST('searched')
        sets = Set.objects.filter(name__contains=searched)

        return render(request, 'search.html', {'searched': searched, 
                      'sets': sets})
    else: 
        return render[request, 'search.html', {}]


def add_set(request):
    submitted = False
    if request.method == "POST":
        form = SetForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_set?submitted=True')
    else:
        form = SetForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_set.html', {'form': form, 
                'submitted': submitted})

    