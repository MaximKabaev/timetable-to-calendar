from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import time

further_maths = {
    'name':'fm',
    'full_lesson': 'Further Maths',
    'short_teacher1':'N',
    'teacher1':'- Mr Nickol',
    'short_teacher2':'L',
    'teacher2':'- Mrs Leach'
}

maths = {
    'name':'m',
    'full_lesson': 'Maths',
    'short_teacher1':'N',
    'teacher1':'- Mr Nickol',
    'short_teacher2':'J',
    'teacher2':'- Mrs Johnson'
}

physics = {
    'name':'p',
    'full_lesson': 'Physics',
    'short_teacher1':'C',
    'teacher1':'- Mr Collman',
    'short_teacher2':'D',
    'teacher2':'- Mrs Dix'
}

computing = {
    'name':'c',
    'full_lesson': 'Computer Science',
    'short_teacher1':'B',
    'teacher1':'- Mr Bradshaw',
    'short_teacher2':'G',
    'teacher2':'- Mrs Githaiga'
}

free = {
    'name':'f',
    'full_lesson': 'Free Period',
    'short_teacher1':'',
    'teacher1':'',
    'short_teacher2':'',
    'teacher2':''
}

games = {
    'name':'g',
    'full_lesson': 'Games',
    'short_teacher1':'',
    'teacher1':'',
    'short_teacher2':'',
    'teacher2':''
}

eal = {
    'name':'e',
    'full_lesson': 'EAL',
    'short_teacher1':'',
    'teacher1':'',
    'short_teacher2':'',
    'teacher2':''
}

a2b = {
    'name':'a',
    'full_lesson': 'A2B',
    'short_teacher1':'',
    'teacher1':'',
    'short_teacher2':'',
    'teacher2':''
}

available_lessons = [further_maths, maths, computing, physics, free, games, eal, a2b]


def decrypt_events():
    user_lessons = input('Enter lessons for the current week from monday. (:) at the end of a dayand (-) at the end of the week (ex: fmN mN fmN fmN cB cG:fM...): ')
    # print(user_lessons)
    weeks = user_lessons.split('-')
    week_index = 0
    for n in weeks:
        week_index+=1
        week = n.split(':')
        index = 0
        for i in week:
            day = i.split()
            index+=1
            lessonNum = 0
            # print(day)
            for lesson in day:
                lessonNum+=1
                time.sleep(1)
                for i in available_lessons:
                    if lesson[0] == i['name']:
                        lesson_type = i
                    elif len(lesson) == 3:
                        lesson_type = further_maths

                if lesson_type['short_teacher1'] == lesson[len(lesson)-1]:
                    create_event(week_index, lessonNum, index, lesson_type, 1)
                else:
                    create_event(week_index, lessonNum, index, lesson_type, 2)
    


def create_event(week_index, lessonNum, index, lesson, teacher_num):
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    # service.calendars().clear(calendarId=CALENDARID).execute()


    d = datetime.now()
    d = d.replace(hour=0, minute=0, second=0)
    day = d - timedelta(days = d.weekday()) + timedelta(days=(index-1)) + timedelta(weeks=(week_index-1))
    
    # day = datetime.combine(day, time.min)
    if lessonNum <=2:
        start = (day + timedelta(hours=(7+lessonNum), minutes=50))
    elif lessonNum <= 4:
        start = (day + timedelta(hours=(8+lessonNum), minutes=10))
    else:
        start = (day + timedelta(hours=(9+lessonNum)))

    end = (start + timedelta(hours=1)).isoformat()
    start = start.isoformat()

    print(f'CREATING week: {week_index}, day: {index}, lesson: {lessonNum}')
    # print(day)
    # print(start)
    # print(end)

    event_result = service.events().insert(calendarId=CALENDARID,
        body={
            "summary": str(lesson['full_lesson']) + ' ' + str(lesson['teacher'+str(teacher_num)]),
            "description": 'lesson',
            "start": {"dateTime": start, "timeZone": 'Europe/London'},
            "end": {"dateTime": end, "timeZone": 'Europe/London'},
            'recurrence': [
                "RRULE:FREQ=WEEKLY;INTERVAL=2",
            ],
        }
    ).execute()

    print("EVENT CREATED")
    # print("id: ", event_result['id'])
    # print("summary: ", event_result['summary'])
    # print("starts at: ", event_result['start']['dateTime'])
    # print("ends at: ", event_result['end']['dateTime'])

CALENDARID = input("Input your calndar id: ")
decrypt_events()
