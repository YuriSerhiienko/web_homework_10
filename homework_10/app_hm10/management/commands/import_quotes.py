from django.core.management.base import BaseCommand
import json
from app_hm10.models import Quote, Author, Tag

class Command(BaseCommand):
    help = "Import quotes data from quotes.json"

    def handle(self, *args, **options):
        with open('quotes.json', 'r', encoding="utf-8") as file:
            quotes_data = json.load(file)

        for quote_data in quotes_data:
            author, created = Author.objects.get_or_create(fullname=quote_data['author'])

            quote = Quote.objects.create(
                text=quote_data['quote'],
                author=author
            )

            tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in quote_data['tags']]
            quote.tags.set(tags)

        self.stdout.write(self.style.SUCCESS("Quotes data imported successfully."))
