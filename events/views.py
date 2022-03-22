from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalFormView,
    BSModalReadView,
    BSModalUpdateView,
)

from events.models import Event, Error, Comment
from events.forms import EventForm, CommentForm, EventUpdateForm

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Index(generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event_home.html'   

@method_decorator(login_required, name='dispatch')
class EventCreateView(BSModalCreateView):
    template_name = 'event_create.html'
    form_class = EventForm
    success_message = 'Thành công: Một sự kiện đã được tạo!'
    success_url = reverse_lazy('event-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(BSModalUpdateView):
    model = Event
    template_name = 'event_update.html'
    form_class = EventUpdateForm
    success_message = 'Thành công: Sự kiện đã được cập nhật!'
    success_url = reverse_lazy('event-home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_comment = Comment.objects.filter(event_comment=self.get_object()).order_by('-create_on')
        context['comments'] = event_comment
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'), staff=self.request.user, event_comment=self.get_object())
        if new_comment.content:
            new_comment.save()
        return super(EventUpdateView, self).post(request, **kwargs)

    def form_valid(self, form):
        if form.instance.date_close:
            form.instance.status = 'close'
        elif form.instance.date_complete:
            form.instance.status = 'complete'
        else:
            form.instance.status = 'process'
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EventDeleteView(BSModalDeleteView):
    model = Event
    template_name = 'event_delete.html'
    success_message = 'Thành công: Sự kiện đã được xóa hoàn toàn!'
    success_url = reverse_lazy('event-home')

