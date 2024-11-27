from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Group


def view_detail_group(request):
    groups_list = Group.objects.all()
    paginator = Paginator(groups_list, 10)
    page_number = request.GET.get('page')
    groups = paginator.get_page(page_number)
    context = {
        "groups": groups
    }
    return render(request, 'groups/detail_groups.html', context=context)
    return render(request, 'groups/detail_groups.html', {'groups': groups})
