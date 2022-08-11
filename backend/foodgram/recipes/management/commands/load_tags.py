from django.core.management import BaseCommand

from recipes.models import Tag

tags = [
    {'name': 'Завтрак', 'color': '#E26C2D', 'slug': 'breakfast'},
    {'name': 'Обед', 'color': '#49B64E', 'slug': 'dinner'},
    {'name': 'Ужин', 'color': '#8775D2', 'slug': 'supper'}
]


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Tag.objects.bulk_create(Tag(**tag) for tag in tags)
        self.stdout.write(self.style.SUCCESS('Теги загружены!'))
