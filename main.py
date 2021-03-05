# Author: Jens Putzeys
# Date: 27-10-2020 (DD-MM-YYYY); last edit: 05-03-2021

import gkeepapi
from quivr import quivr_main
from gkeep import gkeep_main

# Retrieve courses of this week from Quivr.com
courses_dict = quivr_main() # Dictionary

# Place courses in one list
courses = []
for day in courses_dict:
    courses.extend(courses_dict[day])

gkeep_main(courses)