import sqlite3
import json
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Custom startup command to load data from JSON"

    def add_arguments(self, parser):
        parser.add_argument("json_path", type=str, help="Path to the json containing prefix data")

    def handle(self, *args, **kwargs):
        try:
            with open(kwargs["json_path"], "r") as json_file:
                data = json.load(json_file)
            
            

            connection = sqlite3.connect("db.sqlite3")
            cursor = connection.cursor()

        except:
            raise CommandError("Initialization Failed")
