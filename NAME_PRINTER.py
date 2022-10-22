
print("NICKNAME PRINTER")
input("PRESS ANY KEY TO CONTINUE!")
print("GOOD DAY! MY NAME IS CHRISTIAN KEVIN P. DE VEGA AND MY NICKNAME IS")


#the printed nickname is sliced diagonaly into 5 section
#each line of code (from line 13 to 17) corresponds to each of the sliced 5 sections


for y_axis in range(5):
 for x_axis in range(14):
        if (y_axis==0 and x_axis!=1 and x_axis!=2 and x_axis!=4 and x_axis!=8 and x_axis!=13)\
         or (y_axis==1 and x_axis!=1 and x_axis!=3 and x_axis!=4 and x_axis!=6 and x_axis!=7 and x_axis!=8 and x_axis!=10 and x_axis!=11 and x_axis!=12 and x_axis!=14)\
         or (y_axis==2 and x_axis!=2 and x_axis!=3 and x_axis!=4 and x_axis!=8 and x_axis!=13 and x_axis!=14)\
         or (y_axis==3 and x_axis!=1 and x_axis!=3 and x_axis!=4 and x_axis!=6 and x_axis!=7 and x_axis!=8 and x_axis!=10 and x_axis!=11 and x_axis!=12 and x_axis!=14)\
         or (y_axis==4 and x_axis!=1 and x_axis!=2 and x_axis!=4 and x_axis!=8 and x_axis!=13):       
            print("*",end="")
        else:
            print(end=" ")
 print()

print("IT COMES FROM MY SECOND NAME KEVIN, NOW YOU KNOW!")
