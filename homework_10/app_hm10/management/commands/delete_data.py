from django.core.management.base import BaseCommand
from app_hm10.models import Tag, Author, Quote


class Command(BaseCommand):
    help = "Delete all data"

    def handle(self, *args, **options):
        Tag.objects.all().delete()
        Author.objects.all().delete()
        Quote.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("All data has been deleted."))


# python manage.py --help
# python manage.py delete_data
