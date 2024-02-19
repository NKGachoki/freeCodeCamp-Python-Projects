from circular_linked_list import CircularLinkedList

# Main function to add time and return added time in HH:MM XM format + no of days + resulting day of week(optional).
# Function accepts 2 arguments of start time + duration in HH:MM XM format, 3rd argument is optional (all arguments must be strings).
def add_time(start_time, duration, day=None):

    # 1st instance of function call where 'day' argument is None
    if day is None:
        time, am_pm = start_time.split()
        hours, minutes = time.split(':')
        if am_pm == 'PM':
            hours = int(hours) + 12
        d_hours, d_minutes = duration.split(':')
        total_hours = int(hours) + int(d_hours)
        total_minutes = int(minutes) + int(d_minutes)
        if total_minutes >= 60 and total_hours >= 24:
            new_hours, new_minutes = adjust_hours_minutes_1(total_hours, total_minutes)   
            new_adjusted_hours, number_days = adjust_hours_1(new_hours)
            if new_adjusted_hours >= 12:
                am_pm = 'PM'
            else:
                am_pm = 'AM'

            if new_adjusted_hours >= 13:
                new_adjusted_hours = new_adjusted_hours - 12

            if new_minutes < 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm} ({number_days} days later)"
            elif new_minutes >= 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm} ({number_days} days later)"
            elif new_minutes < 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm} (next day)"
            elif new_minutes >= 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm} (next day)"

        elif total_minutes < 60 and total_hours >= 24:
            new_adjusted_hours, number_days = adjust_hours_1(total_hours)
            if new_adjusted_hours >= 12:
                am_pm = 'PM'
            else:
                am_pm = 'AM'

            if new_adjusted_hours >= 13:
                new_adjusted_hours = new_adjusted_hours - 12

            if total_minutes < 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm} ({number_days} days later)"
            elif total_minutes >= 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm} ({number_days} days later)"
            elif total_minutes < 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm} (next day)"
            elif total_minutes >= 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm} (next day)"
                
        elif total_minutes >= 60 and total_hours < 24:
            new_hours, new_minutes = adjust_hours_minutes_1(total_hours, total_minutes)
            if new_hours >= 12:
                am_pm = 'PM'
            else:
                am_pm = 'AM'

            if new_hours >= 13:
                new_hours = new_hours - 12

            if new_minutes < 10:
                new_time = f"{str(new_hours)}:0{str(new_minutes)} {am_pm}"
            else:
                new_time = f"{str(new_hours)}:{str(new_minutes)} {am_pm}"

        else:
            if total_hours >= 12:
                am_pm = 'PM'
            else:
                am_pm = 'AM'

            if total_hours >= 13:
                total_hours = total_hours - 12

            if total_minutes < 10:
                new_time = f"{str(total_hours)}:0{str(total_minutes)} {am_pm}"
            else:
                new_time = f"{str(total_hours)}:{str(total_minutes)} {am_pm}"
    
        return new_time

    # 2nd instance of function call where 'day' argument is not None
    elif day is not None:
        time, am_pm = start_time.split()
        hours, minutes = time.split(':')
        if am_pm == 'PM':
            hours = int(hours) + 12
        d_hours, d_minutes = duration.split(':')
        total_hours = int(hours) + int(d_hours)
        total_minutes = int(minutes) + int(d_minutes)
        if total_minutes >= 60 and total_hours >= 24:
            new_hours, new_minutes = adjust_hours_minutes_2(total_hours, total_minutes)   
            new_adjusted_hours, result_day, number_days = adjust_hours_2(new_hours, day)
            if new_adjusted_hours >= 12:
                am_pm = 'PM'
            else:
                am_pm = 'AM'

            if new_adjusted_hours >= 13:
                new_adjusted_hours = new_adjusted_hours - 12

            if new_minutes < 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm} {result_day} ({number_days} days later)"
            elif new_minutes >= 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm} {result_day} ({number_days} days later)"
            elif new_minutes < 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm} {result_day} (next day)"
            elif new_minutes >= 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm} {result_day} (next day)"    

        elif total_minutes < 60 and total_hours >= 24:
            new_adjusted_hours, result_day, number_days = adjust_hours_2(total_hours, day)
            if new_adjusted_hours >= 12:
                am_pm = 'PM'
            else:
                am_pm = 'AM'

            if new_adjusted_hours >= 13:
                new_adjusted_hours = new_adjusted_hours - 12

            if total_minutes < 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm} {result_day} ({number_days} days later)"
            elif total_minutes >= 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm} {result_day} ({number_days} days later)"
            elif total_minutes < 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm} {result_day} (next day)"
            elif total_minutes >= 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm} {result_day} (next day)"
                

        elif total_minutes >= 60 and total_hours < 24:
            new_hours, new_minutes = adjust_hours_minutes_2(total_hours, total_minutes)
            if new_hours >= 12:
                am_pm = 'PM'
            else:
                am_pm = 'AM'

            if new_hours >= 13:
                new_hours = new_hours - 12

            lower_day = day.lower()
            capitalized_day = lower_day.capitalize()

            if new_minutes < 10:
                new_time = f"{str(new_hours)}:0{str(new_minutes)} {am_pm} {capitalized_day}"
            else:
                new_time = f"{str(new_hours)}:{str(new_minutes)} {am_pm} {capitalized_day}"

        else:
            if total_hours >= 12:
                am_pm = 'PM'
            else:
                am_pm = 'AM'

            if total_hours >= 13:
                total_hours = total_hours - 12

            lower_day = day.lower()
            capitalized_day = lower_day.capitalize()

            if total_minutes < 10:
                new_time = f"{str(total_hours)}:0{str(total_minutes)} {am_pm} {capitalized_day}"
            else:
                new_time = f"{str(total_hours)}:{str(total_minutes)} {am_pm} {capitalized_day}"
    
        return new_time

# Helper function to adjust hours + minutes during 1st instance of main function call.
# Function returns adjusted hours + minutes.
def adjust_hours_minutes_1(hours,minutes):
            while minutes >= 60:
                minutes = minutes - 60
                hours = hours + 1
                if minutes >= 60:
                    adjust_hours_minutes_1(hours, minutes)
                else:
                    break
            return hours, minutes

# Helper function to adjust hours + number of days during 1st instance of main function call.
# Function returns adjusted hours + number of days passed, if any. 
def adjust_hours_1(hours):
    no_of_days = 0
    while hours >= 24:
        hours = hours - 24
        no_of_days = no_of_days + 1

    if hours == 0:
        return hours + 12, no_of_days
    else:
        return hours, no_of_days

# Helper function to adjust hours + minutes during 2nd instance of main function call.
# Function returns adjusted hours + minutes.
def adjust_hours_minutes_2(hours,minutes):
    while minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
        if minutes >= 60:
            adjust_hours_minutes_2(hours, minutes)
        else:
            break
    return hours, minutes

# Helper function to adjust hours + number of days during 2nd instance of main function call.
# Function returns adjusted hours + resulting day of week + number of days passed, if any.
def adjust_hours_2(hours, day):
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
            
    if hours == 0:
        return hours + 12, capitalized_day, count
    else:
        return hours, capitalized_day, count