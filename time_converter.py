#  Create a time management system that converts between different time formats. Your program should:

# Define a function hours_to_minutes(hours) that converts hours to minutes
def hours_to_minutes(hours):
    return hours*60
# Define a function minutes_to_seconds(minutes) that converts minutes to seconds
def minutes_to_seconds(minutes):
    return minutes*60

# Define a function total_seconds(hours, minutes, seconds) that calculates total seconds
def total_seconds(hours,minutes,seconds):
    return hours*3600+minutes*60+seconds

# Define a function format_time(total_minutes) that:
# Takes total minutes as input
# Returns a formatted string “X hours and Y minutes”
def format_time(total_minutes):
    total_minutes=int(input())
    hours=total_minutes//60
    left_minutes=total_minutes%60
    
# Example: 135 minutes returns “2 hours and 15 minutes”
    return hours,'hours',left_minutes,'minutes'

# Define a function can_fit_task(available_hours, task_hours, task_minutes) that:
# Returns True if a task can fit within available time
# Convert everything to minutes for comparison
def can_fit_task(available_hours, task_hours, task_minutes):
    available_minutes=hours_to_minutes(available_hours)
    task_total_minutes=hours_to_minutes(task_hours)+task_minutes
    return task_total_minutes<available_minutes

# Define a function schedule_summary(task_name, hours, minutes) that prints:
def schedule_summary(task_name,hours,minutes):
    # Task name and duration
    # Total time in minutes
    # Total time in seconds
    # No return value (action function)
    print(f'{task_name} takes {hours} hours {minutes} minutes. {total_seconds((hours,minutes))}')
# Task name and duration
# Total time in minutes
# Total time in seconds
# No return value (action function)
# Test your system:
# Convert 2.5 hours to minutes
print(f" 2.5 hours in minutes is{hours_to_minutes(2.5)}")
# Calculate total seconds for 1 hour, 45 minutes, 30 seconds
print(f"Total seconds: {total_seconds((1,45,30))}")
# Format 200 minutes into hours and minutes
print(f'200 minutes formatted: {format_time((200))}')
# Check if a 3 hour 20 minute task fits in 3.5 hours available
print(f"If it fits available time: {can_fit_task((3.5,3,20))}")
# Create schedule summaries for:
# “Study”: 2 hours 30 minutes
# “Exercise”: 0 hours 45 minutes
print(schedule_summary("Study",2,30))
print(schedule_summary("Exercise",0,45))