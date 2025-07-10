from django.shortcuts import render, redirect, get_object_or_404
from .models import Automation
from .forms import AutomationForm
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@never_cache
@login_required
def automation_list(request):
    automations = Automation.objects.all()
    return render(request, 'automation/automation_list.html', {'automations': automations})



def automation_create(request):
    form = AutomationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Automation created successfully!")
        return redirect('automation_list')
    return render(request, 'automation/automation_form.html', {'form': form, 'title': 'Create Automation'})


def automation_update(request, pk):
    automation = get_object_or_404(Automation, pk=pk)
    form = AutomationForm(request.POST or None, instance=automation)
    if form.is_valid():
        form.save()
        messages.info(request, "✏️ Campaign updated successfully!")
        return redirect('automation_list')
    return render(request, 'automation/automation_form.html', {'form': form, 'title': 'Update Automation'})

def automation_delete(request, pk):
    automation = get_object_or_404(Automation, pk=pk)
    if request.method == 'POST':
        automation.delete()
        messages.warning(request, "🗑️ Campaign deleted successfully!")
        return redirect('automation_list')
    return render(request, 'automation/automation_confirm_delete.html', {'automation': automation})
