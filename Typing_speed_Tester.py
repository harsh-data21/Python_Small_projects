"""
Day 1/75
Typing_speed_Tester

"""
import time

print("⚡Typing Speed Test⚡\n")

input("Press Enter to Start ⤵️...")

start = time.time()

text = input("🧾type anything...\n")

end = time.time()

time_taken = end - start

words = len(text.split())

wpm = (words / time_taken) * 60

accuracy = 100

print("\n RESULT") 

print(f" ⏱️ Time: {time_taken:.2f}s")

print(f" ⚡ Speed: {wpm:.0f} wpm")

print(f" 🎯 Accuracy: {accuracy:.0f}%")