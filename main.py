from random import randint as rand

print("""    
     #        #####     ##       #        ##        ##          ######         ######         ######   ############    #####        #######                                                                          
    #  #     ##         ##      #  #      ## ##     ##        ##      ##      #      ##     ##              ##        #      #      #      #                                                                               
   #    #    ##         ##     #    #     ##  ##    ##        #        ##   #        ##   ##               ##       #        #     #       #                                                                                            
  #######      ###      ##    # ## ###    ##    ##  ##        ##        #   #        ##   ##               ##       #        #     # #####                                                                           
 #        #       ##    ##   #        #   ##     ## ##        ##       ##    #     ##      ##              ##        #      #      #      #                                                  
#         #   #####     ##   #        #   ##        ##          #######        #####         #######        ##          #####       #       #                                                                 
                       

""")
print("The game where you are diagnosed with the status of Asian, Bsian, Csian, or Failure.")
print("Disclaimer: any emotional damage associated with the game's responses are not the developer's responsibility")
print("\n")



questions = ["What was your highest math score in percentages?\n", "What was your highest physics score\n", 
 "What was your highest chemistry score\n",  "What was your highest biology score?\n", "How many instruments do you play and to what level?\n", 
 "What are you hobbies\n", "How many PHDs do you have\n", "Do you own a multi-billion dollar business?\n"]

responsesG = ["ok, that okay", "interesting", "that is a good average score", "good", "that's not a fail", "ok, good-e la", "good job"]
responsesB = ["That's a fail", "You're a failure", "That would be highly effective at creating emotional damage for failures like you", "So stupid", "dumb"]


for i in range(len(questions)-1):
    print(questions[i])

    response = input()

    if "100" in response or "ARCT" in response or "all of them" in response or "doctor" in response or "neurosurgeon" in response or "lawyer" in response:
        print(responsesG[rand(0, len(responsesG)-1)])
    else:
        print(responsesB[rand(0, len(responsesB)-1)])
print(questions[7])
response = input()
if "i own apple inc." in response:
    print("Your final diagnoses: you are not a failure")
else:
    print("You are a failure because your business is not the biggest in the world")
