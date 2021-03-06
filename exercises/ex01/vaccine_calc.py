"""A vaccination calculator."""

__author__ = "730237793"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
Population: int = int(input("Population: "))
Doses_administered: int = int(input("Doses administered: "))
Doses_per_day: int = int(input("Doses per day: "))
Target_percent_vaccinated: int = int(input("Target percent vaccinated: "))

Additional_vaccines: float = ((2 * Population * (Target_percent_vaccinated/100)) - Doses_administered) 
Days_until_target_percent_vaccinated: float = Additional_vaccines / Doses_per_day
round(Days_until_target_percent_vaccinated)

Days: timedelta = timedelta(Days_until_target_percent_vaccinated)
today: datetime = datetime.today()
Vaccination_date: datetime = today + Days
Date: str = Vaccination_date.strftime("%B %d, %Y")

string = ("We will be {}% vaccinated in {} days which will fall on {}") .format(Target_percent_vaccinated, Days_until_target_percent_vaccinated, Date)

print(string)






