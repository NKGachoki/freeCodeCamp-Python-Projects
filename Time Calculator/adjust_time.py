"""Importing Circular Linked List class and methods"""
from circular_linked_list import CircularLinkedList

def adjust_hours_minutes_1(hours,minutes):
    """Function to adjust hours + minutes during 1st instance of "add_time" function call"""
    while minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
        if minutes >= 60:
            adjust_hours_minutes_1(hours, minutes)
        else:
            break
    return hours, minutes

def adjust_hours_1(hours):
    """Function to adjust hours + number of days during 1st instance of "add_time" function call"""
    no_of_days = 0
    while hours >= 24:
        hours = hours - 24
        no_of_days = no_of_days + 1

    return hours, no_of_days

def adjust_hours_minutes_2(hours,minutes):
    """Function to adjust hours + minutes during 2nd instance of "add_time" function call"""
    while minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
        if minutes >= 60:
            adjust_hours_minutes_2(hours, minutes)
        else:
            break
    return hours, minutes

def adjust_hours_2(hours, day):
    """Function to adjust hours + number of days during 2nd instance of add_time function call"""
    lower_day = day.lower()
    count = 0
    week = CircularLinkedList()
    days_of_week = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    for day_of_week in days_of_week:
        week.insert(day_of_week)

    while hours >= 24:
        hours = hours - 24
        count = count + 1

    result_day = week.iterate(lower_day, count)
    capitalized_day = result_day.capitalize()

    return hours, capitalized_day, count

def move_once(day):
    """Function to move to next node in a circular linked list"""
    lower_day = day.lower()
    count = 1
    week = CircularLinkedList()
    days_of_week = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    for day_of_week in days_of_week:
        week.insert(day_of_week)

    result_day = week.iterate(lower_day, count)
    capitalized_day = result_day.capitalize()

    return capitalized_day
