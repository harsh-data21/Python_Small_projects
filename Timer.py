"""
Day 7/75
Timer

"""
import time

seconds = int(input("ENTER SECONDS !!!:"))

while seconds>=0:

   mins, secs = divmod(seconds, 60)

   print(f"/r{mins:02d}:{secs:02d}", end = " ")

   time.sleep(1)

   seconds -= 1

print( " /n TIME UP !!!")