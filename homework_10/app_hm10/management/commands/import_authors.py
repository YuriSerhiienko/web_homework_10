from django.core.management.base import BaseCommand
import json
from app_hm10.models import Author

class Command(BaseCommand):
    help = "Import authors data from authors.json"

    def handle(self, *args, **options):
        with open('authors.json', 'r', encoding="utf-8") as file:
            authors_data = json.load(file)

        for author_data in authors_data:
            Author.objects.create(
                fullname=author_data['fullname'],
                born_date=author_data['born_date'],
                born_location=author_data['born_location'],
                description=author_data['description']
            )

        self.stdout.write(self.style.SUCCESS("Authors data imported successfully."))
