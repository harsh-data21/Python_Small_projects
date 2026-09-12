"""
Day 9/75
jokes

"""
import pyjokes

joke = pyjokes.get_joke()

print("Joke of the Moment:")
print(joke)

print("HERE ARE FEW MORE: ")
count = 1

while count <= 5:
   print(str(count) + ". " + pyjokes.get_joke())
   count = count + 1
   
print()
print("BONUS CHUK NORRIS JOKE:")
print(pyjokes.get_joke(category="chuck"))