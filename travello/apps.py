from django.apps import AppConfig


class TravelloConfig(AppConfig):
	name = 'travello'
	def ready(self):
		import travello.signals
