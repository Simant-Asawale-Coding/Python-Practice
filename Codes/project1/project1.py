action=-1
points=0

    

"""player class is below"""
class player():
    def __init__(self,player_name):
        self.player_name=player_name
        self.arrow=0
        self.points=0
        
    def display_options(self):
        a=input("would you like to start? enter(y/n)")
        if(a==('Y' or 'y')):
            r11.check_wumpus()
        else:
            return 0





"""room class is below"""

class room:
    def __init__(self,room_number,pit,stench,breeze,arrow,glitter,visited,adjacent_rooms_list,wumpus,treasure):
        self.room_number=room_number
        self.pit=pit
        self.stench=stench
        self.breeze=breeze
        self.arrow=arrow
        self.glitter=glitter
        self.visited=visited
        self.adjacent_rooms_list=adjacent_rooms_list
        self.wumpus=wumpus
        self.treasure=treasure
        self.perception = (f"\nstench: {self.stench}\n"
                          f"breeze: {self.breeze}\n"
                          f"glitter: {self.glitter}\n"
                          f"arrow: {self.arrow}\n")


    def check_wumpus(self):
        global action
        global points
        action=action+1
        points=points-1
        if self.wumpus==1:
            print("\noh no!, u are in the room of WUMPUS!!")
            if user.arrow==1:
                print("\nYou have an arrow that can kill the WUMPUS, so we are using it to save you! ")
                self.wumpus=0
                points=points-10
                self.check_pit()
            else:
                print("\nYou didn't have an arrow, YOU GOT KILLED\n GAME OVER")
                points=-1000
                print("\n Final score:",points)
                return 0
        else:
            self.check_pit()
            

    def check_pit(self):
                global points
                global action
                if self.pit==1:
                    print("\nYou fell into a PIT!!!, YOU GOT KILLED\n GAME OVER")
                    points=points-500
                    print("\n Final score:",points)
                    return 0
                else:
                    self.check_treasure()

    def check_treasure(self):
            global points
            global action
            if self.treasure==1:
                print("\nCongratulations!!! YOU FOUND THE TREASURE!!")
                points=points+1000
                print("\n Final score:",points)
                return 0
            else:
                self.display_perception()

                    

    def display_perception(self):

        print("\nPerception in the room is:\n","visited earlier:",self.visited,"\n","stench:",self.stench," \n","breeze= ",self.breeze," \n","glitter= ",self.glitter," \n","arrow= ",self.arrow,"\n")
        self.visited='yes'
        self.update_map()


    
    def update_map(self):
        self.visited=1
        global action
        map_file=open("map.txt", 'a')    # Open the file in append mode
        map_file.write(f"\naction number:" + str(action) + "\nroom number:"+ self.room_number +"\nPerceptions:"+ self.perception +"adjacent rooms list:\n")
        for item in self.adjacent_rooms_list:
            map_file.write(item+"\n")

        map_file.close()
        self.adjacent_rooms()


    def adjacent_rooms(self):
        print("\nthe adjacent rooms are: " ,self.adjacent_rooms_list)
        self.arrow_option()

    def arrow_option(self):
        if self.arrow==1:
            arrow_input=input("\narrow is presnt in this room, do u want to pick it up?..(Y/N)")
            if arrow_input==('Y' or 'y'):
                user.arrow=1
                self.arrow=0
                self.actions()
            elif arrow_input==('N' or 'n'):
                user.arrow=0
                self.actions()
            else:
                print("please enter a valid input!")
                self.arrow_option()
        else:
            self.actions()


    def actions(self):
        actions_input=input("\nchoose an action: \n"+"1:go to room (enter 1)\n2:view map (enter 2)\n3:quit (enter 3) ===")
        if actions_input =='1':
            

            for i in self.adjacent_rooms_list:
                print(i)

            room_name=input("enter room number from above: ")
            room_object=rooms_dictionary[room_name]
            if room_name in self.adjacent_rooms_list:
                room_object.check_wumpus()

            else:
                print("please enter a valid room number!!")
                self.actions()

        elif actions_input=='2':
            with open('map.txt','r') as map:
                s=map.read()
                print(s)
                self.actions()
        
        elif actions_input=='3':
            print("thank you for playing")
            return 0
        
        else:
            print("invalid input!, please enter correct option")
            self.actions()

#room objects creation
"""
        self.room_number:room_number
        self.pit=pit
        self.stench=stench
        self.breeze=breeze
        self.arrow=arrow
        self.glitter=glitter
        self.visited=visited
        self.adjacent_rooms_list=adjacent_rooms
        self.wumpus=wumpus
        self.treasure=treasure
        """




"""starting menu"""




if __name__=='__main__':

    
    r11=room(
    room_number='r11'
    ,pit=0
    ,stench='none'
    ,breeze='none'
    ,arrow=0
    ,glitter='none'
    ,visited="no"
    ,adjacent_rooms_list=['r12','r21']
    ,wumpus=0
    ,treasure=0)

    r12=room(
    room_number='r12'
    ,pit=0
    ,stench='none'
    ,breeze='yes'
    ,arrow=0
    ,glitter='none'
    ,visited="no"
    ,adjacent_rooms_list=['r11','r13','r22']
    ,wumpus=0
    ,treasure=0)

    r13=room(
    room_number='r13'
    ,pit=1
    ,stench='none'
    ,breeze='no'
    ,arrow=0
    ,glitter='none'
    ,visited="no"
    ,adjacent_rooms_list=['r12','r14','r23']
    ,wumpus=0
    ,treasure=0)

    r14=room(
    room_number='r14'
    ,pit=0
    ,stench='none'
    ,breeze='yes'
    ,arrow=0
    ,glitter='none'
    ,visited="no"
    ,adjacent_rooms_list=['r13','r24']
    ,wumpus=0
    ,treasure=0)

    r21=room(
    room_number='r21'
    ,pit=0
    ,stench='yes'
    ,breeze='no'
    ,arrow=0
    ,glitter='none'
    ,visited="no"
    ,adjacent_rooms_list=['r11','r22','r31']
    ,wumpus=0
    ,treasure=0)


    r22=room(
    room_number='r22'
    ,pit=0
    ,stench='no'
    ,breeze='no'
    ,arrow=1
    ,glitter='yes'
    ,visited="no"
    ,adjacent_rooms_list=['r12','r21','r23','r32']
    ,wumpus=0
    ,treasure=0)

    r23=room(
    room_number='r23'
    ,pit=0
    ,stench='no'
    ,breeze='yes'
    ,arrow=0
    ,glitter='no'
    ,visited="no"
    ,adjacent_rooms_list=['r13','r22','r24','r33']
    ,wumpus=0
    ,treasure=0)

    r24=room(
    room_number='r24'
    ,pit=0
    ,stench='no'
    ,breeze='no'
    ,arrow=0
    ,glitter='no'
    ,visited="no"
    ,adjacent_rooms_list=['r14','r23','r34']
    ,wumpus=0
    ,treasure=0)

    r31=room(
    room_number='r31'
    ,pit=0
    ,stench='no'
    ,breeze='no'
    ,arrow=0
    ,glitter='yes'
    ,visited="no"
    ,adjacent_rooms_list=['r21','r32','r41']
    ,wumpus=1
    ,treasure=0)

    r32=room(
    room_number='r32'
    ,pit=0
    ,stench='yes'
    ,breeze='yes'
    ,arrow=0
    ,glitter='yes'
    ,visited="no"
    ,adjacent_rooms_list=['r22','r31','r33','r42']
    ,wumpus=0
    ,treasure=1)

    r33=room(
    room_number='r33'
    ,pit=1
    ,stench='no'
    ,breeze='no'
    ,arrow=0
    ,glitter='yes'
    ,visited="no"
    ,adjacent_rooms_list=['r23','r32','r34','r43']
    ,wumpus=0
    ,treasure=0)

    r34=room(
    room_number='r34'
    ,pit=0
    ,stench='no'
    ,breeze='yes'
    ,arrow=0
    ,glitter='no'
    ,visited="no"
    ,adjacent_rooms_list=['r24','r33','r44']
    ,wumpus=0
    ,treasure=0)

    r41=room(
    room_number='r41'
    ,pit=0
    ,stench='yes'
    ,breeze='no'
    ,arrow=0
    ,glitter='no'
    ,visited="no"
    ,adjacent_rooms_list=['r31','r42']
    ,wumpus=0
    ,treasure=0)

    r42=room(
    room_number='r42'
    ,pit=0
    ,stench='no'
    ,breeze='no'
    ,arrow=0
    ,glitter='yes'
    ,visited="no"
    ,adjacent_rooms_list=['r32','r41','r43']
    ,wumpus=0
    ,treasure=0)

    r43=room(
    room_number='r43'
    ,pit=0
    ,stench='no'
    ,breeze='breeze'
    ,arrow=0
    ,glitter='no'
    ,visited="no"
    ,adjacent_rooms_list=['r33','r42','r44']
    ,wumpus=0
    ,treasure=0)

    r44=room(
    room_number='r44'
    ,pit=1
    ,stench='no'
    ,breeze='no'
    ,arrow=0
    ,glitter='no'
    ,visited="no"
    ,adjacent_rooms_list=['r34','r43']
    ,wumpus=0
    ,treasure=0)

    rooms_dictionary = {
    'r11': r11,
    'r12': r12,
    'r13': r13,
    'r14': r14,
    'r21': r21,
    'r22': r22,
    'r23': r23,
    'r24': r24,
    'r31': r31,
    'r32': r32,
    'r33': r33,
    'r34': r34,
    'r41': r41,
    'r42': r42,
    'r43': r43,
    'r44': r44
}
    print("Hello and welcome to WUMPUS world game\n The rules are simple:\ 1: The game contains a 4x4 grid of roomsn\n2: One of the room contains a treasure, the rooms adjacent to the treasure contain glitter in them so look out for the glitter!\n3: Also one of the room has a Monster named WUMPUS, if u enter his room u can either kill him if u have an arrow with u or u get killed and the game is over\n 4: The rooms around the WUMPUS contain a strong stench, so be aware\n 4:One room also contains an arrow that can be picked up if wanted. However if u use that arrow ur score will reduce by -10 points.\n 5: there are multiple rooms containing a pit which can result in immediate fall and death, however the rooms adjacent to the pit contains a strong breeze, so keep a lookout for it as well\n6: Finally if u win u get +1000 points and if u lose u get -1000 points\n7: You will start from room r11\n ALL THE BEST!!")
    user=player(player_name="player1")
    with open("map.txt",'w') as map_file:
        map_file.write("These are the rooms u visited\n")
    r11.check_wumpus()








        
     