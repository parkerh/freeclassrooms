from penn.registrar import Registrar
from credentials import REG_USERNAME, REG_PASSWORD

r = Registrar(REG_USERNAME, REG_PASSWORD)
day_param = 'starts_on_day'
start_param = 'starts_at_or_after_hour'
end_param = 'ends_at_or_after_hour'

days_of_the_week = "MTWRFSU"

def get_used_rooms(start_time, end_time, day):
    sections_generators = [get_sections_starting_on_day(start_time, end_time, d)
            for d in days_to_search(day)]
    """sections = sections_generators[0]
    return [[i['meetings'][0]['building_code'], 
             i['meetings'][0]['room_number']]
            for i in sections ]
"""
    list_of_room_lists = [[[i['meetings'][0]['building_code'],
                            i['meetings'][0]['room_number']]
                           for i in generator if day in
                               i['meetings'][0]['meeting_days']] for generator in
                           sections_generators]
    return [item for sublist in list_of_room_lists for item in sublist]

def get_sections_starting_on_day(start_time, end_time, day):
    sections = r.search({
        day_param : day,
        start_param : start_time,
        end_param : end_time,
        #'course_id' : 'math'
        })
    return sections

def days_to_search(day):
    index = days_of_the_week.index(day)
    days = []
    while(index >= 0):
        days.append(days_of_the_week[index])
        index -= 2
    return days

