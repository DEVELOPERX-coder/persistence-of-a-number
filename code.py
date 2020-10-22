# THIS CODE WILL FIND FIRST NUMBER WITH DEFINE PERSISTENCE

num=0
TD=0
while TD<X:  # THE VALUE OF X = PERSISTENCE  THAT YOU WANNA FIND
    print("THE NUMBER IS:",num)
    number=map(int, str(num))
    a=1
    for x in number:
        a=a*x
    digit=map(int, str(a))
    print(a)
    total_time=1
    td=0
    while len(digit)!=1:
        g=1
        td=-1
        for i in digit:
            td=td+1
            g=g*i
        digit = map(int, str(g))
        print(g)
    print("TIMES DIVIDE", total_time+td)
    TD=total_time+td
    num=num+1

# SOME OF THE FIRST NUMBER OF SOME SPECIFIC PERSISTENCE  ARE
#NUM=0 , TD=0
#NUM=10 , TD=1
#NUM=25 , TD=2
#NUM=269 , TD=3
#NUM=2789 , TD=4
#NUM=27999 , TD=5
#NUM=289999 , TD=6
#NUM= , TD=7
#NUM= , TD=8
#NUM= , TD=9
#NUM= , TD=10
#NUM=277777788888899 , TD=11
#NUM= , TD=12