from django.http import HttpResponseRedirect
from .models import Bb, Rubric
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy, reverse

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs, 'rubrics': rubrics})

def by_rubric (request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    # bbs = Bb.objects.get(pk=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    first_rubric = Rubric.objects.first()
    bbz = first_rubric.entries.all()
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric, 'bbz': bbz}

    return render(request,'bboard/by_rubric.html', context)
class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics']= Rubric.objects.all()
        return context

def add(request):
    bbf = BbForm
    context = {'form': bbf}
    return render(request, 'bboard/create.html', context)
def add_save(request):
    bbf = BbForm(request.POST)
    if bbf.is_valid():
        bbf.save()
        return HttpResponseRedirect (reverse('by_rubric', kwargs={'rubric_id' : bbf.cleaned_data['rubric'].pk}))
    else:
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)


