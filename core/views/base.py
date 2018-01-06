from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


class BaseListView(ListView):
    pass

class BaseDetailView(DetailView):
    pass

class BaseCreateView(CreateView):
    pass

class BaseUpdateView(UpdateView):
    pass

class BaseDeleteView(DeleteView):
    pass
