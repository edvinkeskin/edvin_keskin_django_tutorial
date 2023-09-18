from django.contrib import admin
from django.http import JsonResponse
import json
from .models import Customer, Organization, Office, Employee


def export_as_json_organization(modeladmin, request, queryset):
    # Use prefetch_related to fetch the related offices efficiently
    queryset = queryset.prefetch_related('offices')

    data = []
    for organization in queryset:
        organization_data = {
            'id': organization.id,
            'name': organization.name,
            'address': organization.address,
            'city': organization.city,
            'province': organization.province,
            'postal_code': organization.postal_code,
            'country': organization.country,
            'phone_no': organization.phone_no,
            'offices': [office.name for office in organization.offices.all()]  # Include offices in the data
        }
        data.append(organization_data)

    # Create a JSON response
    response_data = json.dumps(data, indent=2)
    response = JsonResponse(json.loads(response_data), safe=False)
    response['Content-Disposition'] = 'attachment; filename="data.json"'
    return response


export_as_json_organization.short_description = "Export selected items as JSON"


class YourModelAdmin(admin.ModelAdmin):
    actions = [export_as_json_organization]


admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Office)
admin.site.register(Organization, YourModelAdmin)
