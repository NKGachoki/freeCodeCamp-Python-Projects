"""Importing functions from adjust_time module"""
import adjust_time

def add_time(start_time, duration, day=None):
    """Function that adds duration time to start time and returns results"""

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
            new_hours, new_minutes = adjust_time.adjust_hours_minutes_1(total_hours, total_minutes)   
            new_adjusted_hours, number_days = adjust_time.adjust_hours_1(new_hours)

            if new_adjusted_hours == 0:
                new_adjusted_hours += 12
                am_pm = 'AM'
            elif new_adjusted_hours >= 12:
                am_pm = 'PM'
            elif new_adjusted_hours < 12:
                am_pm = 'AM'

            if new_adjusted_hours >= 13:
                new_adjusted_hours = new_adjusted_hours - 12

            if new_minutes < 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm} ({number_days} days later)"
            elif new_minutes >= 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm} ({number_days} days later)"
            elif new_adjusted_hours == 12 and total_minutes < 10 and am_pm == 'AM':
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm} (next day)"
            elif new_adjusted_hours == 12 and total_minutes >= 10 and am_pm == 'AM':
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm} (next day)"
            elif new_minutes < 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm} (next day)"
            elif new_minutes >= 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm} (next day)"

        elif total_minutes < 60 and total_hours >= 24:
            new_adjusted_hours, number_days = adjust_time.adjust_hours_1(total_hours)

            if new_adjusted_hours == 0:
                new_adjusted_hours += 12
                am_pm = 'AM'
            elif new_adjusted_hours >= 12:
                am_pm = 'PM'
            elif new_adjusted_hours < 12:
                am_pm = 'AM'

            if new_adjusted_hours >= 13:
                new_adjusted_hours -= 12

            if total_minutes < 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm} ({number_days} days later)"
            elif total_minutes >= 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm} ({number_days} days later)"
            elif new_adjusted_hours == 12 and total_minutes < 10 and am_pm == 'AM':
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm} (next day)"
            elif new_adjusted_hours == 12 and total_minutes >= 10 and am_pm == 'AM':
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm} (next day)"
            elif total_minutes < 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm} (next day)"
            elif total_minutes >= 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm} (next day)"

        elif total_minutes >= 60 and total_hours < 24:
            new_hours, new_minutes = adjust_time.adjust_hours_minutes_1(total_hours, total_minutes)
            if new_hours == 24:
                new_adjusted_hours, number_days = adjust_time.adjust_hours_1(new_hours)
                new_adjusted_hours += 12
                am_pm = 'AM'

                if new_minutes < 10:
                    new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm} (next day)"
                elif new_minutes >= 10:
                    new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm} (next day)"
            else:
                if new_hours == 0:
                    new_hours += 12
                    am_pm = 'AM'
                elif new_hours >= 12:
                    am_pm = 'PM'
                elif new_hours < 12:
                    am_pm = 'AM'

                if new_hours >= 13:
                    new_hours -= 12

                if new_hours == 12 and new_minutes < 10 and am_pm == 'AM':
                    new_time = f"{str(new_hours)}:0{str(new_minutes)} {am_pm} (next day)"
                elif new_hours == 12 and new_minutes >= 10 and am_pm == 'AM':
                    new_time = f"{str(new_hours)}:{str(new_minutes)} {am_pm} (next day)"
                elif new_minutes < 10:
                    new_time = f"{str(new_hours)}:0{str(new_minutes)} {am_pm}"
                else:
                    new_time = f"{str(new_hours)}:{str(new_minutes)} {am_pm}"
           
        elif total_minutes < 60 and total_hours < 24:

            if total_hours == 0:
                total_hours += 12
                am_pm = 'AM'
            if total_hours >= 12:
                am_pm = 'PM'
            elif total_hours < 12:
                am_pm = 'AM'

            if total_hours >= 13:
                total_hours = total_hours - 12

            if total_hours == 12 and total_minutes < 10 and am_pm == 'AM':
                new_time = f"{str(total_hours)}:0{str(total_minutes)} {am_pm} (next day)"
            elif total_hours == 12 and total_minutes >= 10 and am_pm == 'AM':
                new_time = f"{str(total_hours)}:{str(total_minutes)} {am_pm} (next day)"
            elif total_minutes < 10:
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
            new_hours, new_minutes = adjust_time.adjust_hours_minutes_2(total_hours, total_minutes)
            new_adjusted_hours, result_day, number_days = adjust_time.adjust_hours_2(new_hours, day)

            if new_adjusted_hours == 0:
                new_adjusted_hours += 12
                am_pm = 'AM'
            elif new_adjusted_hours >= 12:
                am_pm = 'PM'
            elif new_adjusted_hours < 12:
                am_pm = 'AM'

            if new_adjusted_hours >= 13:
                new_adjusted_hours -= 12

            if new_minutes < 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm}, {result_day} ({number_days} days later)"
            elif new_minutes >= 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm}, {result_day} ({number_days} days later)"
            elif new_adjusted_hours == 12 and new_minutes < 10 and am_pm == 'AM':
                new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
            elif new_adjusted_hours == 12 and new_minutes >= 10 and am_pm == 'AM':
                new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
            elif new_minutes < 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm}, {result_day} (next day)"
            elif new_minutes >= 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm}, {result_day} (next day)"    

        elif total_minutes < 60 and total_hours >= 24:
            new_adjusted_hours, result_day, number_days = adjust_time.adjust_hours_2(total_hours, day)

            if new_adjusted_hours == 0:
                new_adjusted_hours += 12
                am_pm = 'AM'
            elif new_adjusted_hours >= 12:
                am_pm = 'PM'
            elif new_adjusted_hours < 12:
                am_pm = 'AM'

            if new_adjusted_hours >= 13:
                new_adjusted_hours -= 12

            if total_minutes < 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm}, {result_day} ({number_days} days later)"
            elif total_minutes >= 10 and number_days > 1:
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm}, {result_day} ({number_days} days later)"
            elif new_adjusted_hours == 12 and total_minutes < 10 and am_pm == 'AM':
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
            elif new_adjusted_hours == 12 and total_minutes >= 10 and am_pm == 'AM':
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
            elif total_minutes < 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:0{str(total_minutes)} {am_pm}, {result_day} (next day)"
            elif total_minutes >= 10 and number_days == 1:
                new_time = f"{str(new_adjusted_hours)}:{str(total_minutes)} {am_pm}, {result_day} (next day)"

        elif total_minutes >= 60 and total_hours < 24:
            new_hours, new_minutes = adjust_time.adjust_hours_minutes_2(total_hours, total_minutes)
            if new_hours == 24:
                new_adjusted_hours, result_day, number_days = adjust_time.adjust_hours_2(new_hours, day)
                if new_adjusted_hours == 0:
                    new_adjusted_hours += 12
                    am_pm = 'AM'

                if new_adjusted_hours == 12 and new_minutes < 10 and am_pm == 'AM':
                    new_time = f"{str(new_adjusted_hours)}:0{str(new_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
                elif new_adjusted_hours == 12 and new_minutes >= 10 and am_pm == 'AM':
                    new_time = f"{str(new_adjusted_hours)}:{str(new_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
            else:
                if new_hours == 0:
                    new_hours += 12
                    am_pm = 'AM'
                elif new_hours >= 12:
                    am_pm = 'PM'
                elif new_hours < 12:
                    am_pm = 'AM'

                if new_hours >= 13:
                    new_hours -= 12

                lower_day = day.lower()
                capitalized_day = lower_day.capitalize()

                if new_hours == 12 and new_minutes < 10 and am_pm == 'AM':
                    new_time = f"{str(new_hours)}:0{str(new_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
                elif new_hours == 12 and new_minutes >= 10 and am_pm == 'AM':
                    new_time = f"{str(new_hours)}:{str(new_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
                elif new_minutes < 10:
                    new_time = f"{str(new_hours)}:0{str(new_minutes)} {am_pm}, {capitalized_day}"
                else:
                    new_time = f"{str(new_hours)}:{str(new_minutes)} {am_pm}, {capitalized_day}"

        elif total_minutes < 60 and total_hours < 24:

            if total_hours == 0:
                total_hours += 12
                am_pm = 'AM'
            if total_hours >= 12:
                am_pm = 'PM'
            elif total_hours < 12:
                am_pm = 'AM'

            if total_hours >= 13:
                total_hours -= 12

            lower_day = day.lower()
            capitalized_day = lower_day.capitalize()

            if total_hours == 12 and total_minutes < 10 and am_pm == 'AM':
                new_time = f"{str(total_hours)}:0{str(total_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
            elif total_hours == 12 and total_minutes >= 10 and am_pm == 'AM':
                new_time = f"{str(total_hours)}:{str(total_minutes)} {am_pm}, {adjust_time.move_once(day)} (next day)"
            elif total_minutes < 10:
                new_time = f"{str(total_hours)}:0{str(total_minutes)} {am_pm} {capitalized_day}"
            else:
                new_time = f"{str(total_hours)}:{str(total_minutes)} {am_pm} {capitalized_day}"

        return new_time
