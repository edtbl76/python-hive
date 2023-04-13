from time import sleep,strftime
USER_FIRST_NAME = "Ed"

calendar = {}


def welcome():
  print(f"Welcome, {USER_FIRST_NAME}.")
  print("Calendar starting...")
  sleep(1)
  print("Today is: " + strftime("%A %B %d, %Y"))
  print("The time is currently: " + strftime("%X"))
  print("What would you like to do?")


def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit")

    user_choice = user_choice.upper()

    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print("Calendar is empty")
      else:
        print(calendar)
    elif user_choice == "U":
      date = input("What date?")
      update = input("Enter the update: ")
      calendar[date] = update
      print(f"Update {update} to {date} successful")
      print(calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print(f"Invalid Date: {date}")
        try_again = input("Try Again? Y for Yes, N for No")
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print(f"Successfully added {event} on {date} to calendar")
        print(calendar)
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("Calendar is empty")
      else:
        event = input("What event?: ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print("Successfully deleted {event} on {date} from calendar.")
            print(calendar)
          else:
            print("Invalid event.")
    elif user_choice == "X":
      start = False
    else:
      print("Invalid Option")
      start = False


start_calendar()