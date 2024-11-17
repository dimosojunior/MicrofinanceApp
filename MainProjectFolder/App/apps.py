from django.apps import AppConfig
from django.utils.autoreload import restart_with_reloader
import threading


class AppConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'App'

	#-------------FOR JOBS.py------------
	# def ready(self):
	# 	from jobs import updater
	# 	updater.start()

	#--------------FOR Kumbusho La Uatamiaji.py-----------
	# def ready(self):
	# 	from .Kumbusho_La_Uatamiaji_schedule import Kumbusho_La_Uatamiaji_start_scheduler

	# 	def Kumbusho_La_Uatamiaji_start_scheduler_thread():
	# 	    Kumbusho_La_Uatamiaji_start_scheduler()

	# 	thread = threading.Thread(target=Kumbusho_La_Uatamiaji_start_scheduler_thread)
	# 	thread.daemon = True  # Daemonize thread to exit when the main program exits
	# 	thread.start()


	#--------------FOR Chanjo.py-----------
	# def ready(self):
	# 	from .chanjo_schedule import chanjo_scheduler

	# 	def chanjo_scheduler_thread():
	# 	    chanjo_scheduler()

	# 	thread = threading.Thread(target=chanjo_scheduler_thread)
	# 	thread.daemon = True  # Daemonize thread to exit when the main program exits
	# 	thread.start()

	#------------For test1.py-----------
	# def ready(self):
	# 	from .kusafisha_banda import start_scheduler

	# 	def start_scheduler_thread():
	# 	    start_scheduler()

	# 	thread = threading.Thread(target=start_scheduler_thread)
	# 	thread.daemon = True  # Daemonize thread to exit when the main program exits
	# 	thread.start()