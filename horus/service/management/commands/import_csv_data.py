import csv

from django.core.management.base import BaseCommand

from horus.service.models import (  # Replace 'myapp' with the name of your Django app
    Hotel,
)


def clean(value):
    if value == "null":
        return None
    return value


def clean_image(value):
    if value == "null":
        return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwrOqvMw6ggZnvpbjKMenaPA6NLmRNo_re4mklFQHT&s"
    return value


def clean_location(value):
    if value == "null":
        return "Egypt"
    return value


def clean_language_spoken(value):
    if value == "null":
        return "Arabic"
    return value


def clean_review(value):
    if value == "null":
        return 3
    return value


class Command(BaseCommand):
    help = "Imports data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        csv_file = options["csv_file"]
        # print(__path__)
        with open(f"./horus/service/management/commands/{csv_file}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                person = Hotel(
                    name=clean(row["name"]),
                    location=clean_location(row["location"]),
                    image=clean_image(row["image-src"]),
                    description=clean(row["description"]),
                    review=clean_review(row["review rate"]),
                    cleanlinsess_review=clean_review(row["cleanliness review"]),
                    service_review=clean_review(row["service review"]),
                    value_review=clean_review(row["value review"]),
                    language_spoken=clean_language_spoken(row["LANGUAGES SPOKEN"]),
                )
                person.save()

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
