from django.db.models import Q
from django.shortcuts import get_object_or_404

from call_center_project.models import CallLog, User


class CallLogService:
    def find_all(self, user: User):
        return CallLog.objects.filter(*self.get_conditions(user)).order_by(
            "-start_time"
        )

    def find_by_id(self, user: User, id: int):
        conditions = self.get_conditions(user)
        conditions.append(Q(id=id))

        return get_object_or_404(CallLog, *conditions)

    def get_conditions(self, user: User):
        if user.is_operator:
            conditions = [Q(operator=user)]
        else:
            conditions = [
                Q(tenant_company_phone_number__tenant_company=user.tenant_company),
            ]

        return conditions
