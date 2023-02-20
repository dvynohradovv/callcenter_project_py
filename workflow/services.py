from django.db.models import Q
from django.shortcuts import get_object_or_404

from call_center_project.models import CallLog, User


class CallLogService:
    def find_all(self, user: User):
        query = self.get_owner_query(user)

        return CallLog.objects.filter(query).order_by("-start_time")

    def find_by_id(self, user: User, id: int):
        query = self.get_owner_query(user)
        query &= Q(id=id)

        return get_object_or_404(CallLog, query)

    def get_owner_query(self, user: User):
        query = Q()

        if user.is_operator:
            query &= Q(operator=user) & Q(operator__isdisabled=False)

        if user.is_tenant_company_owner:
            query &= Q(tenant_company_phone_number__tenant_company=user.tenant_company)

        return query
