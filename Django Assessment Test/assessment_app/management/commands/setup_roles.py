from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create user roles and assign permissions'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        roles_permissions = {
            'interviewer': ['can_schedule_interview'],
            'admin': ['can_schedule_interview', 'can_view_all_interviews', 'can_manage_users']
        }

        for role, perms in roles_permissions.items():
            group, created = Group.objects.get_or_create(name=role)
            for perm in perms:
                permission, created = Permission.objects.get_or_create(codename=perm, name=f'Can {perm}', content_type=ContentType.objects.get_for_model(User))
                group.permissions.add(permission)
                self.stdout.write(f'Assigned {perm} to {role}')

        self.stdout.write(self.style.SUCCESS('Successfully created roles and assigned permissions'))