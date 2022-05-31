from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates house rules"

    """ def add_arguments(self, parser):

        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        ) """

    def handle(self, *args, **options):

        rules = [
            "No smoking",
            "No parties or events",
            "No pets/Pets allowed",
            "No unregistered guests",
            "No food or drink in bedrooms",
            "No loud noise after 11 PM",
        ]
        for r in rules:
            HouseRule.objects.create(name=r)

        self.stdout.write(self.style.SUCCESS(f"{len(rules)} House Rules created!"))
