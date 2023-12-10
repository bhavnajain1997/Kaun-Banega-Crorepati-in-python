import random
username = input("Enter Your Name: ").strip()
print(f"Hello {username}, All the Best ")
question = ["Who is the Father of our Nation?","Giddha is the folk dance of?","Who was the first Prime Minister of India?","Who invented Computer?","India lies in which continent?"]
selectrandomques = random.choice(question)
print(f"Question:-  {selectrandomques}")

answer = ["Mahatma Gandhi","Punjab","Dr. Rajender Prasad","Charles Babbage","Asia"]

if(selectrandomques == "Who is the Father of our Nation?"):
  a = "(A) Jawaharlal Nehru"
  b = "(B) Mahatma Gandhi"
  c = "(C) Dr. Rajender Prasad"
  d = "(D) Sheikh Mujibur Rahman"
  print(a,b,c,d)
  userans = int(input("Enter Correct ans: "))
  if(userans == 2):
   print("Mahatma Gandhi is the father of our nation")
  else:
   print("please fill correct answer")
elif(selectrandomques == "Giddha is the folk dance of?"):
  a = "(A) Delhi"
  b = "(B) Gujarat"
  c = "(C) Punjab"
  d = "(D) Kerla"
  print(a,b,c,d)

  userans = int(input("Please select one option 1,2,3,4: "))
  if(userans == 3):
   print("Giddha is the folk dance of Punjab")
  else:
   print("please fill correct answer")
   
elif(selectrandomques == "Who was the first Prime Minister of India?"):
  a = "(A) Dr. Rajender Prasad"
  b = "(B) Indira Gandhi"
  c = "(C) Rajiv Gandhi"
  d = "(D) Lal Bahadur Shastri"
  print(a,b,c,d)
  userans = int(input("Please select one option 1,2,3,4: "))
  if(userans == 1):
      print("Dr. Rajender Prasad is the first prime minister of India")
  else:
      print("please fill correct answer")

elif(selectrandomques == "Who invented Computer?"):
  a = "(A) William Shakespeare"
  b = "(B) Charles Babbage"
  c = "(C) Charles Rudolph Walgreen"
  d = "(D) Albert Einstein"
  print(a,b,c,d)
  userans = int(input("Please select one option 1,2,3,4: "))
  if(userans == 2):
    print("Charles Babbage is invented Computer")
  else:
    print("please fill correct answer")

elif(selectrandomques == "India lies in which continent?"):
  a = "(A) Europe"
  b = "(B) Africa"
  c = "(C) Asia"
  d = "(D) South America"
  print(a,b,c,d)
  userans = int(input("Please select one option 1,2,3,4: "))
  if(userans == 3):
    print("India lies in Asia Contineufwrnt")
  else:
    print("please fill correct answer")

else:
  print("Good luck")

