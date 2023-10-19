a=input("ENTER YOUR NAME:")
print("HELLO",a,"I AM THE PROGRAMMAR, LET'S PLAY A GAME . ")
print("I WILL ASK YOU 5 QUESTIONS AND YOU HAVE TO ANSWER IT.")
print("BUT IF YOU WILL TELL THE WRONG ANSWER THE GAME WILL BE OVER.")
print("AT LAST I WILL TELL YOU YOUR'S SCORE THAT HOW MUCH YOU HAVE DONE CORRECT AND WHEN YOU TELL THE WRONG ANSWER")
print("(PLEASE WRITE THE ANSWERS IN SMALL LETTERS)")
print("SO LET'S BEGIN")
while True:
 b, c=int(input("2+3=")), (1)
 if b==5:
     print("WELL DONE")
 else:
     print("GAME OVER")
     print("YOUR SCORE IS ZERO OUT OF 5")
     break
 d, e=input("WHAT IS THE COLOUR OF GRAPES?(PLEASE WRITE IN SMALL LETTERS)"), (1)
 if d==("green"):
     print("WOW")
 else:
     print("GAME OVER")
     print("YOUR SCORE IS", e, "OUT OF 5")
     break
 f, g=input("WHAT IS THE COLOUR OF SKY?"), (1)
 if f==("blue"):
      print("NICE")
 else:
     print("GAME OVER")
     print("YOUR SCORE IS ", c+e, "OUT OF 5")
     break
 h, i=input("WHAT IS THE COLOUR OF TEETH?"), (1)
 if h==("white"):
     print("AMAZING")
 else:
     print("GAME OVER")
     print("YOUR SCORE IS ", c+e+g, "OUT OF 5")
     break
 j, k=int(input("IN WHICH YEAR OUR COUNTRY GOT IT'S INDEPENDENCE?")), (1)
 if j==1947:
     print ("WOW YOU HAVE DONE EVERY QUESTIONS RIGHT AND")
     print("YOUR SCORE IS", c+e+g+i+k, "OUT OF 5")
     break
 else:
     print("GAME OVER")
     print("YOUR SCORE IS ", c+e+g+i)
     break
