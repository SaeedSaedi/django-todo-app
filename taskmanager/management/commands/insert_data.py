from django.core.management.base import BaseCommand
from faker import Faker
from taskmanager.models import Task
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Insert fake tasks with 'Complete' status into the database"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        # Create a user
        user = User.objects.create_user(
            username=self.fake.email(), password="Test@123456"
        )
        user.first_name = self.fake.first_name()
        user.last_name = self.fake.last_name()
        user.save()

        self.stdout.write(self.style.SUCCESS(f"Created user: {user.email}"))

        # Create tasks in "Complete" status
        for _ in range(5):  # Create 5 tasks
            Task.objects.create(
                user=user,
                title=self.fake.sentence(nb_words=5),  # Generate a fake title
                status=2,  # 2 corresponds to "Done" status
                created_at=timezone.now(),
                updated_at=timezone.now(),
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully created 5 tasks in 'Complete' status")
        )
