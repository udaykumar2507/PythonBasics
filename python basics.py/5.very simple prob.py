#PROGRAM TO ADD,SUB,MUL,DIV TWO NUM
A=int(input("enter the num:"))
B=int(input("enter the num:"))
print("the sum is ",A+B)
print("the diff is",A-B)
print("the mul is",A*B)
print("the div is",A/B)
#PROGRAM TO CALCULATE AREA OF RECTANGLE,CIRCLE,SQUARE PERIMETER OF SQUARE,RECTANGLE ,CIRCUMFERENCE OF CIRCLE
r=int(input("enetr the num1:"))
h=int(input("enter the num2:"))
print("the area of the circle is",3.14*(r*r))
print("area of the rectangle",r*h)
print("area of the square",r**2)
print("perimeter of the square",4*r)
print("perimeter of rectangle",2*(r+h))
print("circumfernce of circle",2*3.14*r)
#electricity consuption
unit=int(input("enter the amount of electricity:"))
percen=int(input("percentage of discount"))
price=unit*5
discount=(price/100)*percen
print("discount is",discount)
print("amount of electricity ",price-discount)
#program to accept 5 subjects and their grade
mark1=int(input("enter the mark1"))
mark2=int(input("mark2"))
mark3=int(input("mark3"))
mark4=int(input("mark4"))
mark5=int(input("mark5"))
total_mark=mark1+mark2+mark3+mark4+mark5
percentage=(total_mark/500)*100
if percentage>=80:
    print("grade a")
elif percentage<80 and percentage>=60:
    print("grade b")
elif percentage<60 and percentage>=40:
    print("grade c")
else:
    print("grade f")

                