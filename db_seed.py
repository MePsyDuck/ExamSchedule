import random

from django_seed import Seed
from faker import Faker

from MainApp.models import Schedule

count = 2000

seeder = Seed.seeder()

courses = ['AE', 'AU', 'CE', 'ME', 'CS', 'EC', 'EE', 'IT', 'EN', 'MA', 'PH', 'CH', 'MG', 'GE', 'LL']

seeder.add_entity(Schedule, count, {
    'vtu_id': lambda x: 'VTU' + str(random.randint(6000, 6999)),
    'tts_id': lambda x: 'TTS' + str(random.randint(2000, 2199)),
    'sub_id': lambda x: str(random.randint(1, 8)) + '15' + str(random.randint(0, 8)) +
                        random.choice(courses) + str(random.randint(100, 999)),
    'room_id': lambda x: random.randint(1000, 9999),
    'date': lambda x: Faker().date_between(start_date='today', end_date='+30d')
})

seeder.execute()
