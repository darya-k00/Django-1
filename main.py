import os
from dotenv import load_dotenv
load_dotenv()
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard 

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    for passcard in passcards:
        active_passcards = Passcard.objects.filter(is_active=True)  
    print(f"Всего пропусков: {Passcard.objects.count()}")
    print(f"Активных пропусков: {len(active_passcards)}")
