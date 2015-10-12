from django.core.management.base import BaseCommand
from django.db import IntegrityError
from gwaith import get_rates

from gwaithdemo.models import Rate


class Command(BaseCommand):
    help = "Downloads the rates and saves them into DB. In output " \
           "'.' marks progress, one db object saved; " \
           "'s' denotes an already existing object, skipped."

    def add_arguments(self, parser):
        parser.add_argument(
            'currency', nargs='*', type=str, default=None,
            help='limits downloading to optional space delimited list of '
                 'ISO-4217 currency codes, uppercase, omit to get all'
        )

    def handle(self, *args, **options):
        for currency, rates in get_rates(only=options['currency']):
            for date, rate in rates.items():
                try:
                    Rate.objects.create(
                        date=date, rate=rate, currency=currency
                    )
                    self.stdout.write('.', ending='')
                except IntegrityError:
                    self.stdout.write('s', ending='')
                self.stdout.flush()
