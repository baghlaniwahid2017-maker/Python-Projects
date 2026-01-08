# Day 8: Loop سلسله
# Loop (While)
#x = 1 (در این فرمول که X+=1 بعد از پرنت بیاید شمار از همان قمیت اکس شروع میشود)
#while x < 10:
#    print(x)
#    x+=1
#x = 1 (در این فرمول که X+=1 پیش از پرنت بیاید شمار از همان قمیت اکس شروع میشود)
#x = 1
#while x < 10:
#    x+=1
#    print(x)
# اگر بخایم بجای یک عدد دو عدد یا سه عد بالای اکس جمع شود
#x = 1
#while x < 10:
#    print(x)
#    x+=2
# اگر بخایم به صورت جفت  بیاید

#x = 1
#while x <10:
#    if x % 2==0:
#        print(x)
#    x+=1

# اگر بخایم به صورت  طاق بیاید

#x = 1
#while x <10:
#    if x % 2!=0:
#        print(x)
#    x+=1

# اگر از عدد کلان به خورد بخایم پرنت کنیم 

#x = 15
#while x > 1:
   
#    print(x)
#    x-=1

#x = 15
#while x > 1:
#    if x % 2 !=0:
#        print(x)
#    x-=1

# Loops (for) practice


# (Loop Continute)
#x = 15
#while x > 1:
#    if x ==5:
#        continue 
#    print(x)
#    x-=1
# (loop Break)
#x = 15
#while x > 1:
#    if x ==10:
#        break
#   print(x)
#   x-=1

# (loop for)

#for x in range (15):
#   if x == 6:
#       continue
#   print(x)

#for x in range (20):
#    if (x == 4) or (x == 6):
#        continue 
#    print(x)


#for x in range (2,30,2):
#   if (x == 4) or (x == 6):
#        continue 
#    print(x)

for x in range(2,40):
    if (x == 5) or (x == 2):
        continue
    print(x)
