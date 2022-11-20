from django.contrib import admin

from call_center_project.models import (Address, CallerPerson, CallLog, Office,
                                        OperatorToWorkPlace, Software,
                                        SoftwareVersion, TenantCompany,
                                        TenantCompanyPhoneNumber, User,
                                        WorkPlace)

# Register your models here.
admin.site.register(Address)
admin.site.register(Office)
admin.site.register(Software)
admin.site.register(SoftwareVersion)
admin.site.register(WorkPlace)
admin.site.register(TenantCompany)
admin.site.register(TenantCompanyPhoneNumber)
admin.site.register(CallerPerson)
admin.site.register(User)
admin.site.register(OperatorToWorkPlace)
admin.site.register(CallLog)
