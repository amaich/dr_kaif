from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.decorators.http import require_POST

from .models import Client
from .forms import ClientForm, VisitForm


class ClientListView(ListView):
    model = Client
    template_name = 'clients/clients_list.html'
    context_object_name = 'clients'


class ClientCreateView(CreateView):
    form_class = ClientForm
    template_name = 'clients/client_create.html'
    success_url = reverse_lazy('clients:client_list')


def client_detail(request, client_id):
    client = get_object_or_404(Client,
                               id=client_id)
    visits = client.visits.all().order_by('visit_date')
    form = VisitForm()
    context = {'client': client, 'visits': visits, 'form': form}
    return render(request,
                  'clients/client_detail.html',
                  context=context)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_update.html'
    context_object_name = 'client'

    def get_success_url(self):
        return reverse('clients:client_detail', kwargs={'pk': self.object.id})


def client_delete(self, request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return HttpResponseRedirect(reverse('clients:clients_list'))


class ClientSearchView(ListView):
    model = Client
    template_name = 'clients/client_search.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.filter(fullname__icontains=self.request.GET.get('name'))

    def get_context_data(self, **kwargs):
        context = super(ClientSearchView, self).get_context_data(**kwargs)
        context['find_name'] = self.request.GET.get('name')
        return context


@require_POST
def visit_create(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    visit = None
    form = VisitForm(data=request.POST)
    if form.is_valid():
        visit = form.save(commit=False)
        visit.client = client
        visit.save()
        return HttpResponseRedirect(reverse('clients:client_detail', kwargs={'client_id': client_id}))
    else:
        print(form.errors)
        return HttpResponse(f'{form.errors}\n{type(form.errors)}')
