from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead
from .forms import LeadForm
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@never_cache
@login_required
def lead_list(request):
    leads = Lead.objects.all().order_by('-created_at')
    return render(request, 'lead/lead_list.html', {'leads': leads})

def lead_create(request):
    form = LeadForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Lead created successfully!")
        return redirect('lead_list')
    return render(request, 'lead/lead_form.html', {'form': form, 'title': 'Create Lead'})


def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        messages.info(request, "✏️ Lead updated successfully!")
        return redirect('lead_list')
    return render(request, 'lead/lead_form.html', {'form': form, 'title': 'Update Lead'})

def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        messages.warning(request, "🗑️ Lead deleted successfully!")
        return redirect('lead_list')
    return render(request, 'lead/lead_confirm_delete.html', {'lead': lead})
