# Formatting dates and time in Python

# This file demonstrates how to format date and time values using 
# the datetime module along with f-strings.
# Date and time formatting is commonly used in logs, reports, user interfaces, and 
# real-world applications.


from datetime import datetime

now=datetime.now()

print(f"Today is {now:%Y-%m-%d}")
print(f"Time is {now:%H-%M-%S}")

# explanation:
# %Y -> Year (4 digits)
# %m -> Month (01-12)
# %d -> Day (01-31)
# %H -> Hour (00-23)
# %M -> Minute (00-59)
# %S -> Second (00-59)
