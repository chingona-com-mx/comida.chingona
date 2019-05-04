
# Django
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.core.management import call_command

# Utils
import time

class Command(BaseCommand):
    help = 'Intenta hacer y aplicar las migraciones hasta que la base de datos esté lista para recibir conexiones.'
    def handle(self, *args, **options):
        self.stdout.write('Aplicando migraciones...')
        con_db = None
        while not con_db:
            try:
                call_command('makemigrations')
                call_command('migrate')
                con_db = True
                self.stdout.write(self.style.SUCCESS('Las migraciones se hicieron y aplicaron correctamente!!'))
            except OperationalError:
                self.stdout.write('La base de datos no está lista, esperando un segundo...')
                time.sleep(1)
