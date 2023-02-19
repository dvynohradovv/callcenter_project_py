from django.contrib.auth.mixins import UserPassesTestMixin

from call_center_project.models import AccountType


class UserTypeMixin(UserPassesTestMixin):
    def test_func(self):
        return (
            len(self.user_types) == 0
            or AccountType[self.request.user.type] in self.user_types
            or self.request.user.is_superuser
            or AccountType[self.request.user.type] == AccountType.Admin
        )
