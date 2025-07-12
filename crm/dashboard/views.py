from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncDate
from datetime import timedelta
from collections import OrderedDict

from lead.models import Lead
from campaign.models import Campaign
from automation.models import Automation
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

@never_cache
@login_required
def dashboard_view(request):
    total_leads = Lead.objects.count()
    leads_by_status = Lead.objects.values('status').annotate(count=Count('id'))
    total_campaigns = Campaign.objects.count()
    total_automations = Automation.objects.count()

    recent_leads = Lead.objects.order_by('-id')[:5]
    recent_campaigns = Campaign.objects.order_by('-id')[:5]

    # Lead growth data (past 7 days)
    today = timezone.now().date()
    last_week = today - timedelta(days=6)
    lead_growth = (
        Lead.objects.filter(created_at__date__gte=last_week)
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    growth_data = OrderedDict((str(last_week + timedelta(days=i)), 0) for i in range(7))
    for item in lead_growth:
        growth_data[str(item['date'])] = item['count']

    return render(request, 'dashboard/dashboard.html', {
        'total_leads': total_leads,
        'leads_by_status': leads_by_status,
        'total_campaigns': total_campaigns,
        'total_automations': total_automations,
        'recent_leads': recent_leads,
        'recent_campaigns': recent_campaigns,
        'growth_labels': list(growth_data.keys()),
        'growth_counts': list(growth_data.values()),
    })
