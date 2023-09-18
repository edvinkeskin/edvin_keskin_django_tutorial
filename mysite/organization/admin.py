from django.contrib import admin
from django.http import JsonResponse
import json
from .models import Customer, Organization, Office, Employee


from django.http import JsonResponse
import json


def export_as_json_organization(modeladmin, request, queryset):
    # Use prefetch_related to fetch the related offices and their employees efficiently
    queryset = queryset.prefetch_related('offices__employees')

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
            'offices': [
                {
                    'name': office.name,
                    'address': office.address,
                    'city': office.city,
                    'province': office.province,
                    'postal_code': office.postal_code,
                    'country': office.country,
                    'phone_no': office.phone_no,
                    'employees': [
                        {
                            'name': employee.user.username,
                            'Email': employee.user.email,
                            'address': employee.address,
                            'city': employee.city,
                            'province': employee.province,
                            'postal_code': employee.postal_code,
                            'country': employee.country,
                            'phone_no': employee.phone_no,
                        }
                        for employee in office.employees.all()
                    ]
                }
                for office in organization.offices.all()
            ]
        }
        data.append(organization_data)

    # Create a JSON response
    response_data = json.dumps(data, indent=2)
    response = JsonResponse(json.loads(response_data), safe=False)
    response['Content-Disposition'] = 'attachment; filename="organization_data.json"'
    return response


export_as_json_organization.short_description = "Export selected organizations as JSON"


class YourModelAdmin(admin.ModelAdmin):
    actions = [export_as_json_organization]


admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Office)
admin.site.register(Organization, YourModelAdmin)
