from crontab import CronTab
import os
import pathlib
from argparse import ArgumentParser

# Get path to this directory
def get_current_dir():
    return str(pathlib.Path(__file__).parent.absolute())

def set_cron(args, job):
    
    # Use default values if no flags are provided
    if not (args.minutes or args.hours or args.dateofmonth):
        args.minutes = 30
        args.hours = 1

    # Converting overflow of minutes & hours
    args.hours += args.minutes // 60
    args.dateofmonth += args.hours // 23

    # Limiting minutes & hours
    args.minutes %= 60
    args.hours %= 24


    # Day gap, if provided
    if args.dateofmonth: job.day.every(args.dateofmonth)

    # Hour gap, if provided
    job.hour.every(args.hours) if args.hours else job.hour.on(0) 

    # Minute gap if provided
    job.minute.every(args.minutes) if args.minutes else job.minute.on(0) 


if __name__ == "__main__":

    # Add arguments
    parser = ArgumentParser()
    
    parser.add_argument("-min", dest="minutes",
                        help="Set minutes after which wallpaper updates", required=False, 
                        type=int , metavar="[1-59]", default=0)

    parser.add_argument("-hr", dest="hours",
                        help="Set hours after which wallpaper updates", required=False, 
                        type=int , metavar="[0-23]", default=0)

    parser.add_argument("-dom", dest="dateofmonth",
                        help="Set the day of the month for wallpaper update", required=False, 
                        type=int , metavar="[1-31]", default=0)
    
    # Parse arguments
    args = parser.parse_args()

    # Create cron
    cron = CronTab(user=True)

    # Add cron job to run update_background.py
    job  = cron.new(command='/usr/bin/python3 ' + get_current_dir() + "/bin/update_background.py")

    # Set up the cron job
    set_cron(args, job)

    # Add to the crontab
    cron.write()

