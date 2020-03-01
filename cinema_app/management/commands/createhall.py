from account_app.models import User
from cinema_app.models import Hall,City,Theater,Seat,HallType
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

import inquirer
class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('hall_name', type=str, help='Indicates the name of hall to be created')
        parser.add_argument('row', type=int, help='Indicates the number of rows to be created')
        parser.add_argument('col', type=int, help='Indicates the number of columns to be created')

    def handle(self, *args, **kwargs):
        hall_name = kwargs['hall_name']
        row = kwargs['row']
        col = kwargs['col']

        cities = City.objects.all()
        if len(cities)==0:
            return f'The country of Azerbaijan has not any city in database yet.'
        print(len(cities))
        choose_city = [
          inquirer.List('city',
                        message="Which city ?",
                        choices=[city for city in cities]
                    ),
        ]
        city = inquirer.prompt(choose_city)
        print(city['city'])
        theaters=Theater.objects.filter(city=city['city'])
        if len(theaters)==0:
            city=city['city']
            return f'{city} has not any theater yet'
        print(theaters)
        print(len(theaters))


        choose_theater = [
          inquirer.List('theater',
                        message=f" Which Theater in {city['city']} ?",
                        choices=[theater for theater in theaters]
                    ),
        ]

        theater = inquirer.prompt(choose_theater)

        city = City.objects.get(name=city['city'])
        print('city',city.created_at)
        theater = Theater.objects.get(city = city,name = theater['theater'])

        print( theater)
        hall_types = HallType.objects.all()
        choose_hall_type = [
          inquirer.List('hall_type',
                        message=f" What is the hall type of the {hall_name} ?:",
                        choices=[hall_type for hall_type in hall_types]
                    ),
        ]

        hall_type = inquirer.prompt(choose_hall_type)
        print(hall_type['hall_type'])

        new_hall = Hall(name = hall_name,theater = theater,type=hall_type['hall_type'])
        new_hall.save()
        seats = []
        number =0
        is_active = False
        for i in range(1,row+1):
            for j in range(1,col+1):
                inp = input(f'row:{i} col:{j} is active ? y or any: ')
                number+=1
                if inp =='y' or inp=='Y':
                    is_active=True
                    seats.append({'row':i,'column':j,'number':number,'is_active':is_active})

        [new_hall.seats.add(Seat.objects.create(row=i['row'],column=i['column'],number=i['number'])) for i in seats]
