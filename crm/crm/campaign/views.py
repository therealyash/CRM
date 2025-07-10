from django.shortcuts import render, redirect, get_object_or_404
from .models import Campaign
from .forms import CampaignForm
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@never_cache
@login_required
def campaign_list(request):
    campaigns = Campaign.objects.all().order_by('-start_date')
    return render(request, 'campaign/campaign_list.html', {'campaigns': campaigns})


def campaign_create(request):
    form = CampaignForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Campaign created successfully!")
        return redirect('campaign_list')
    return render(request, 'campaign/campaign_form.html', {'form': form, 'title': 'Create Campaign'})


def campaign_update(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    form = CampaignForm(request.POST or None, instance=campaign)
    if form.is_valid():
        form.save()
        messages.info(request, "✏️ Campaign updated successfully!")
        return redirect('campaign_list')
    return render(request, 'campaign/campaign_form.html', {'form': form, 'title': 'Update Campaign'})

def campaign_delete(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    if request.method == 'POST':
        campaign.delete()
        messages.warning(request, "🗑️ Campaign deleted successfully!")
        return redirect('campaign_list')
    return render(request, 'campaign/campaign_confirm_delete.html', {'campaign': campaign})
