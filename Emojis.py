while True:
    number_of_guys=int(input("Cuantos chicos quieres en el emoji: "))
    if number_of_guys>255:
        continue
    elif number_of_guys<1:
        continue
    else:
        break
comp_guys={"complete_guy":"(-_-)", "side_guy_right":"_-)", "partial_guy_right":"-_-)", "final_guy_right":"-)", "side_guy_left":"(-_", "partial_guy_left":"(-_-", "final_guy_left":"(-"}
mob=''
if number_of_guys==1:
    mob+=comp_guys["complete_guy"]
if number_of_guys%2==0:
    if number_of_guys>7:
        mob+=comp_guys["final_guy_left"]
        cont=(number_of_guys//2)-1
        while cont>0:
            if cont%3==0:
                mob+=comp_guys["partial_guy_left"]
            elif cont%2==0:
                mob+=comp_guys["side_guy_left"]
            elif cont%1==0:
                mob+=comp_guys["side_guy_left"]
            cont-=1
        mob+=comp_guys["complete_guy"]
        rest=number_of_guys-((number_of_guys//2)+2)
        while rest>0:
            mob+=comp_guys["side_guy_right"]
            rest-=1
        mob+=comp_guys["final_guy_right"]
    else:
        cont=number_of_guys//2
        while cont>0:
            if cont%3==0:
                mob+=comp_guys["partial_guy_left"]
            elif cont%2==0:
                mob+=comp_guys["side_guy_left"]
            elif cont%1==0:
                mob+=comp_guys["side_guy_left"]
            cont-=1
        mob+=comp_guys["complete_guy"]
        rest=number_of_guys-((number_of_guys//2)+1)
        while rest>0:
            mob+=comp_guys["side_guy_right"]
            rest-=1
if number_of_guys%2!=0:
    if number_of_guys>7:
        mob+=comp_guys["final_guy_left"]
        cont=(number_of_guys//2)-1
        while cont>0:
            if cont%3==0:
                mob+=comp_guys["partial_guy_left"]
            elif cont%2==0:
                mob+=comp_guys["side_guy_left"]
            elif cont%1==0:
                mob+=comp_guys["side_guy_left"]
            cont-=1
        mob+=comp_guys["complete_guy"]
        rest=number_of_guys-((number_of_guys//2)+2)
        while rest>0:
            mob+=comp_guys["side_guy_right"]
            rest-=1
        mob+=comp_guys["final_guy_right"]
    else:
        cont=number_of_guys//2
        while cont>0:   
            if cont%3==0:
                mob+=comp_guys["partial_guy_left"]
            elif cont%2==0:
                mob+=comp_guys["side_guy_left"]
            elif cont%1==0:
                mob+=comp_guys["side_guy_left"]
            cont-=1
        mob+=comp_guys["complete_guy"]
        rest=number_of_guys-((number_of_guys//2)+1)
        while rest>0:
            mob+=comp_guys["side_guy_right"]
            rest-=1
print(mob)
