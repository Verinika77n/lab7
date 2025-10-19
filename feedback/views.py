from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from .forms import FeedbackForm
from .models import Feedback

def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо! Отзыв отправлен.')
            return redirect('feedback-create')  # PRG
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

class FeedbackList(ListView):
    model = Feedback
    template_name = 'feedback/feedback_list.html'
    
    paginate_by = 5
