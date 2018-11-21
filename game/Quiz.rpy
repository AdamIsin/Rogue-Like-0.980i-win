label Rogue_Strip_Study:
    $ Count = 0
    $ Count2 = 1
    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # The entire list of objects. . .
    $ renpy.random.shuffle(QuizOrder)  # . . .shuffled randomly. . .    
    
    ch_r "Alright, [R_Petname], I'll make this simple. I'll ask you a quiz question, get it right, I take something off. . ."
    ch_r "Get three wrong, and we're done for the night. Good luck."
    while Count2:        
        "Question [Count2],"
        call Quiz_Question_Rogue
        $ Count2 += 1
        if _return:
            call Rogue_Strip_Study_Right
        else:
            $ Count += 1
            call Rogue_Strip_Study_Wrong        
    return
            
label Rogue_Strip_Study_Right:
    if R_Hose:  # Will she lose the hose?
            $ Line = R_Hose           
            $ R_Hose = 0
            "She slowly removes her [Line]. . ."
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 3)
            return    
        
    if R_Over: #will she lose the top?
        if R_SeenChest or (R_Chest and ApprovalCheck("Rogue", 300)) or ApprovalCheck("Rogue", 850):
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 25, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
            $ Line = R_Over           
            $ R_Over = 0
            "She pulls her [Line] off and throws it aside."      
            
        else:
            ch_r "You know, I don't really think I'm ready for this, sorry [R_Petname]. I shouldn't have led you on."
            $ Count2 = 0
        return   
        
    if R_Legs:   #will she lose the pants/skirt?
        if (R_SeenPanties and R_SeenPussy) or (R_Panties and (ApprovalCheck("Rogue", 700) or R_SeenPanties)) or ApprovalCheck("Rogue", 950):  
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 5)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
            $ Line = R_Legs           
            $ R_Legs = 0
            if Line == "skirt":
                "She unzips her skirt and slides it off."
            else:
                "She unzips her jeans and slides them down her legs." 
            if R_Panties:
                if not R_SeenPanties:   
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)  
                    $ R_SeenPanties = 1
            else:
                #R seen pussy
                $ R_Blush = 1
                "You notice that she apparently isn't wearing any panties, and she flushes a bit."
                
        else:
            ch_r "You know, I don't really think I'm ready for this, sorry [R_Petname]. I shouldn't have led you on."
            $ Count2 = 0
        return     
    
    if R_Chest: # Will she go topless?
        if ApprovalCheck("Rogue", 900) or (R_SeenChest and ApprovalCheck("Rogue", 600)):
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 1)
            $ Line = R_Chest           
            $ R_Chest = 0
            "She pulls her [Line] over her head and tosses it aside."  
            if not R_SeenChest:   
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 3)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)  
                call Rogue_First_Topless(1)
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 15)
        else:
             ch_r "I know a deal's a deal, but I'd like to keep my top on, ok [R_Petname]? Sorry about that."
             $ Count2 = 0
        return  
            
    if R_Panties: # Will she go bottomless?
        if ApprovalCheck("Rogue", 950) or (R_SeenPussy and ApprovalCheck("Rogue", 600)):    
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 70, 10)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 2)    
            $ Line = R_Panties           
            $ R_Panties = 0
            "She slides her [Line] off, leaving her pussy bare."    
            if not R_SeenPussy:
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 4)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 4)
                call Rogue_First_Bottomless(1)
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 75, 20)
        else:
             ch_r "Look, this has gone a bit far, [R_Petname]. I'd like to call it a night."
             $ Count2 = 0
        return  
            
    ch_r "Well, that's another right answer, but I don't have a stitch left to take off. . ."     
    $ Count2 = 0
    $ Tempmod = 50
    call Rogue_SexMenu    
    ch_r "Well I sure enjoyed that."
    return
    
label Rogue_Strip_Study_Wrong:
    if Count == 1:
        ch_r "Bzzt, too bad, [R_Petname]."
    elif Count == 2:
        ch_r "Oh, you're really not good at this. Come on, you've only got one more shot."
    elif Count > 2:
        ch_r "And you are out of here! Sorry, [R_Petname], thanks for playing, you're done."
        $ Count2 = 0
        
    return
    
label Quiz_Question_Rogue:    
    if QuizOrder[Count2] == 1:
        menu:
            ch_r "Who was the first person who I used my powers on?"
            "A. Colby":
                return 0
            "B. Renly":
                return 0
            "C. Remy":
                return 0
            "D. Cody":
                return 1
    if QuizOrder[Count2] == 2:
        menu:
            ch_r "Where did I live before moving to Xaviers?"
            "A. Lousiana":
                return 0
            "B. Mississippi":
                return 1
            "C. Connecticut":
                return 0
            "D. Tennessee":
                return 0
    if QuizOrder[Count2] == 3:
        menu:
            ch_r "What was the first power I. . . borrowed?"
            "A. Mystique's shape shifting":
                return 0
            "B. Shadowcat's phasing":
                return 0
            "C. Nightcrawler's teleport":
                return 1
            "D. Cyclops's eyebeams":
                return 0
    if QuizOrder[Count2] == 4:
        menu:
            ch_r "What mutant raised me as my parent before my powers manifested."
            "A. Magneto":
                return 0
            "B. Mystique":
                return 1
            "C. Xavier":
                return 0
            "D. Belasco":
                return 0
    if QuizOrder[Count2] == 5:
        menu:
            ch_r "I eventually joined the X-Men after Mystique attacked me, where?"
            "A. At school":
                return 0
            "B. At the beach":
                return 0
            "C. In the mountains":
                return 1
            "D. In the bayou":
                return 0
    if QuizOrder[Count2] == 6:
        menu:
            ch_r "When Magneto was selecting the fittest mutants for Asteroid M, I was captured after beating which member of the Brotherhood?"
            "A. Blob":
                return 0
            "B. Avalanche":
                return 0
            "C. Toad":
                "That's right, [R_Petname], I slammed that frog tongue in a car door"
                "Better not make me angry."
                return 1
            "D. Quicksilver":
                return 0
                
    #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1


#////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////

label Kitty_Strip_Study:
    $ Count = 0
    $ Count2 = 1
    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # The entire list of objects. . .
    $ renpy.random.shuffle(QuizOrder)  # . . .shuffled randomly. . .   
    call KittyFace("perplexed", 2)
    ch_k "Ok, so[K_like]if you get a question right. . . I'll take off a piece of clothing. . ."
    ch_k "But you only get three tries." 
    call KittyFace("sly", 1)
    while Count2:        
        "Question [Count2],"
        call Quiz_Question_Kitty
        $ Count2 += 1
        if _return:
            call Kitty_Strip_Study_Right
        else:
            $ Count += 1
            call Kitty_Strip_Study_Wrong        
    return
            
label Kitty_Strip_Study_Right:
    if K_Hose:  # Will she lose the hose?   
            $ Line = K_Hose           
            $ K_Hose = 0
            "She slowly removes her [Line]. . ."
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 3)
            return    
        
    if K_Over: #will she lose the top?
        if K_SeenChest or (K_Chest and ApprovalCheck("Kitty", 300)) or ApprovalCheck("Kitty", 850):
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 25, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)        
            $ Line = K_Over             
            $ K_Over = 0
            "She lets her [Line] drop to the floor."     
            
        else:  
            call KittyFace("perplexed", 2)
            ch_k "Sorry,I don't mean to be a tease, but I just can't handle this yet."  
            call KittyFace("bemused", 1)
            $ Count2 = 0
        return   
        
    if K_Legs:   #will she lose the pants/skirt?
        if (K_SeenPanties and K_SeenPussy) or (K_Panties and (ApprovalCheck("Kitty", 700) or K_SeenPanties)) or ApprovalCheck("Kitty", 950):  
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 5)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)     
            $ Line = K_Legs           
            $ K_Legs = 0 
            "She lets her [Line] pool at her feet."    
            if K_Panties:
                if not K_SeenPanties:   
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)  
                    $ K_SeenPanties = 1
            else:
                #R seen pussy
                $ K_Blush = 2
                "You notice that she apparently isn't wearing any panties, and she flushes a bit."
                $ K_Blush = 1
                
        else:
            ch_k "Sorry, I don't mean to be a tease, but I just can't handle this yet." 
            $ Count2 = 0
        return     
    
    if K_Chest: # Will she go topless?
        if ApprovalCheck("Kitty", 900) or (K_SeenChest and ApprovalCheck("Kitty", 600)):
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 1)     
            $ Line = K_Chest                         
            $ K_Chest = 0  
            "She lets her [Line] drop into a pile at her feet."    
            if not K_SeenChest:   
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 3)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)  
                call Kitty_First_Topless(1)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 15)
        else:
             ch_k "So. . . I know this is a bit late to mention it, but I'd like to keep my top on?"
             $ Count2 = 0
        return  
            
    if K_Panties: # Will she go bottomless?
        if ApprovalCheck("Kitty", 950) or (K_SeenPussy and ApprovalCheck("Kitty", 600)):    
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 70, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 2)    
            $ Line = K_Panties                        
            $ K_Panties = 0    
            "She shrugs and her [Line] drop to the floor, leaving her pussy bare."  
            if not K_SeenPussy:
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 4)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 4)
                call Kitty_First_Bottomless(1)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 75, 20)
        else:
            call KittyFace("perplexed", 2)
            ch_k "Wow, I. . . I'm not really ready for this sort of thing, I'm sorry!"
            call KittyFace("perplexed", 1)
            $ Count2 = 0
        return  
            
    call KittyFace("sly", 1)
    ch_k "So. . . you got that one right. . ."
    $ K_Eyes = "down"
    ch_k ". . . but I'm not[K_like]wearing anything else. . ."     
    call KittyFace("sly", 1)
    $ Count2 = 0
    $ Tempmod = 50
    call Kitty_SexMenu    
    ch_k "I think I learned a few things there. . ."
    return
    
label Kitty_Strip_Study_Wrong:
    call KittyFace("sly", 1)
    if Count == 1:
        ch_k "Nope."
    elif Count == 2:
        ch_k "{i}So{/i} close. One more try."
    elif Count > 2:
        ch_k "Aw, too bad, so sad. Maybe next time."
        $ Count2 = 0
        
    return

label Quiz_Question_Kitty:    
    if QuizOrder[Count2] == 1:
        menu:
            ch_k "Ok, do you[K_like]know where I come from? What's my home town?"
            "A. Chicago, Illinois": 
                return 0 
            "B. Deerfield, Illinois": 
                return 1 
            "C. New York City, New York":        
                return 0 
            "D. St. Louis, Missouri": 
                return 0 
    if QuizOrder[Count2] == 2:          
        menu: 
            ch_k "What's my mutant power called?"
            "A. Disappearing": 
                return 0 
            "B. Ghosting": 
                return 0 
            "C. Phasing": 
                return 1 
            "D. Shifting": 
                return 0 
    if QuizOrder[Count2] == 3: 
        ch_k "So. . . don't laugh, but I have this stuffed animal I sleep with[K_like]every night."
        menu:
            ch_k "Know his name?"
            "A. Draco": 
                return 0 
            "B. Flipper": 
                return 0 
            "C. Lockheed": 
                return 1 
            "D. N'gari": 
                return 0 
                    
    if QuizOrder[Count2] == 4: 
        ch_k "Okay. Did you know that Dr. McCoy takes a handful of students on a private tutoring retreat?"
        menu:                
            ch_k "Know where he takes them?"
            "A. The Great Redwood Forest, California": 
                return 1 
            "B. Mount McKinley, Alaska": 
                return 0 
            "C. Mount Rushmore, South Dakota": 
                return 0 
            "D. Yellowstone National Park, Wyoming": 
                return 0 
    if QuizOrder[Count2] == 5: 
        ch_k "One of the worst threats we have to worry about as mutants are the giant robots called Sentinels."
        menu:
            ch_k "Do you know who built them?"
            "A. Arcade": 
                return 0 
            "B. Bolivar Trask": 
                return 1 
            "C. Magneto": 
                return 0 
            "D. Unus the Untouchable": 
                return 0 
    if QuizOrder[Count2] == 6: 
        ch_k "Y'know, we didn't always have classes here at the Institute." 
        ch_k "For a while, all the students here went to a local public school." 
        menu:
            ch_k "Know which one?" 
            "A. Bayville High School": 
                return 1 
            "B. King Memorial High School":
                return 0 
            "C. Riverside High School": 
                return 0 
            "D. Seth Paine High School": 
                return 0 
    if QuizOrder[Count2] == 7: 
        menu:
            ch_k "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
            "A. Jean Grey": 
                return 0 
            "B. Lance Alvers": 
                return 1 
            "C. Mystique": 
                return 0 
            "D. Professor Xavier": 
                return 0 
    if QuizOrder[Count2] == 8: 
        ch_k "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation." 
        ch_k "Even though it was a lot of fun, we ended up disbanding after that." 
        menu:
            ch_k "Anyway, know what the name we chose for the group was?"
            "A. The Bayville Avengers": 
                return 0 
            "B. The Bayville Brawlers": 
                return 0 
            "C. The Bayville Harpies": 
                return 0 
            "D. The Bayville Sirens": 
                return 1 
    if QuizOrder[Count2] == 9: 
        menu:
            ch_k "Okay[K_like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
            "A. A hot shower": 
                return 0 
            "B. Methyl Ethyl Ketone": 
                return 0 
            "C. Isolation": 
                return 1 
            "D. Tomato Juice": 
                return 0 
    if QuizOrder[Count2] == 10: 
        ch_k "When I'm using my powers, I'm not[K_like]{i}totally{/i} invulnerable."
        menu:
            ch_k "Who has powers that can still affect me?"
            "A. Blob": 
                return 0 
            "B. Magneto": 
                return 0 
            "C. Quicksilver": 
                return 0 
            "D. Scarlet Witch": 
                return 1

 #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1
    
#label Quiz:
#    $ Count = 0                                         #This is the number of times you've gotten a wrong answer. 
#    $ Count2 = 1                                        #this is the position in the quis so far. 
#    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # The entire list of objects. . .
#    $ renpy.random.shuffle(QuizOrder)                   # . . .shuffled randomly. . .    This is optional, and if you want to skip randomization then you can just increment a counter instead of this.
    
#    while Count2:                                       #This cycles so long as Count2 is greater than zero
#        "Question [Count2],"
#        call Quiz_Question
#        $ Count2 += 1                                   #This increments to the next question in the list after ti asks each one
#        if _return:                                     #the _return variable is whatever the Quiz Questions lable returns.
#            "You got it right!"
#            $ Score += 1                                #This tallies the right answers as you make them
#        else:
#            "Bzzt, Wrong answer"
#            $ Count += 1
#        if Count2 >= 14: #set this to one under the total number of questions
#            "You're done. Your score is [Score] out of 15."            
#            $ Count2 = 0           
#        elif Count > 2:                                 #this kicks you out if you get three wrong, remove that if you don't want it. 
#            "Too bad, you're done"
#            $ Count2 = 0                                #This breaks the cycle and returns the player to where he started the quiz. 
#    return
    
#label Quiz_Question:
#    if QuizOrder[Count2] == 1:                          #This asks the first question, set each following question to a number.
#        menu:
#            "Question"
#            "A. ":
#                return 1                                #the correct answer sends a 1, the incorrect answers send back a zero. 
#            "B. ":
#                return 0
#            "C. ":
#                return 0
#            "D. ":
#                return 0


#////////////////////////////////////////////////////////////////////////////////////

label Emma_Strip_Study:
    $ Count = 0
    $ Count2 = 1
    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # The entire list of objects. . .
    $ renpy.random.shuffle(QuizOrder)  # . . .shuffled randomly. . .   
    call EmmaFace("bemused")
    ch_e "I take the education process very seriously."    
    call EmmaFace("bemused", Eyes="side")
    ch_e "So you get a question right. . . "
    ch_e ". . ."
    call EmmaFace("sly")
    ch_e "I'll take off a piece of clothing. . ."
    ch_e "But you only get three tries." 
    while Count2:        
        "Question [Count2],"
        call Quiz_Question_Emma
        $ Count2 += 1
        if _return:
            call Emma_Strip_Study_Right
        else:
            $ Count += 1
            call Emma_Strip_Study_Wrong        
    return
            
label Emma_Strip_Study_Right:
    if E_Hose:  # Will she lose the hose?        
            $ Line = E_Hose           
            $ E_Hose = 0
            "She slowly removes her [Line]. . ."
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 3)
            return    
        
    if E_Over: #will she lose the top?
        if E_SeenChest or (E_Chest and ApprovalCheck("Emma", 300)) or ApprovalCheck("Emma", 750):
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 25, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)         
            $ Line = E_Over        
            $ E_Over = 0
            "She shrugs off her [Line] and lets it fall to the floor."    
            
        else:  
            call EmmaFace("sly", 1)
            ch_e "Sorry, I don't mean to be a tease, but I doubt you can handle this yet."  
            call EmmaFace("bemused", 1)
            $ Count2 = 0
        return   
        
    if E_Legs:   #will she lose the pants/skirt?
        if (E_SeenPanties and E_SeenPussy) or (E_Panties and (ApprovalCheck("Emma", 700) or E_SeenPanties)) or ApprovalCheck("Emma", 950):  
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)        
            $ Line = E_Legs    
            $ E_Legs = 0 
            "She strips off her [Line] and drops them at her feet."  
            if E_Panties:
                if not E_SeenPanties:   
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)  
                    $ E_SeenPanties = 1
            else:
                #R seen pussy
                call EmmaFace("sly", 1)
                "You notice that she apparently isn't wearing any panties."
                $ E_Blush = 0
                
        else:
            call EmmaFace("sly", 1)
            ch_e "Sorry, I don't mean to be a tease, but I doubt you can handle this yet." 
            $ Count2 = 0
        return     
    
    if E_Chest: # Will she go topless?
        if ApprovalCheck("Emma", 800) or (E_SeenChest and ApprovalCheck("Emma", 500)):
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 1)        
            $ Line = E_Chest               
            $ E_Chest = 0  
            "She pulls off her [Line] and drops it at her feet."     
            if not E_SeenChest:   
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 3)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)  
                call Emma_First_Topless(1)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 15)
        else:
            call EmmaFace("perplexed", 1)
            ch_e "Hmm. . . better than I thought." 
            call EmmaFace("sly", 1)
            ch_e "But I doubt you're ready for this yet."
            $ Count2 = 0
        return  
            
    if E_Panties: # Will she go bottomless?
        if ApprovalCheck("Emma", 950) or (E_SeenPussy and ApprovalCheck("Emma", 600)):    
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 2)            
            $ Line = E_Panties            
            $ E_Panties = 0   
            "She tugs off her [Line] and drops them to the floor, leaving her pussy bare." 
            if not E_SeenPussy:
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 4)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 4)
                call Emma_First_Bottomless(1)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 75, 20)
        else:
            call EmmaFace("perplexed", 1)
            ch_e "Hmm. . . better than I thought." 
            call EmmaFace("sly", 1)
            ch_e "But I doubt you're ready for this yet."
            $ Count2 = 0
        return  
            
    call EmmaFace("sly", 1)
    ch_e "Hmm. . . another correct answer. . ."
    $ E_Eyes = "down"
    ch_e ". . . but I don't have anything else to remove. . ."     
    call EmmaFace("sly", 1)
    $ Count2 = 0
    $ Tempmod = 50
    call Emma_SexMenu    
    ch_e "I hope you picked up a few things. . ."
    return
    
label Emma_Strip_Study_Wrong:
    call EmmaFace("sly", 1)
    if Count == 1:
        ch_e "Unfortunately. . . no."
    elif Count == 2:
        ch_e "I'm afraid not, one more try."
    elif Count > 2:
        ch_e "Pity, I expected better of you."
        $ Count2 = 0
    return

label Quiz_Question_Emma:    
    if QuizOrder[Count2] == 1:
        menu:
            ch_e "So, do you know "
            "A. Manchester, England": 
                return 0 
            "B. New York City, New York":        
                return 0 
            "C. Boston, Massachusetts": 
                return 1 
            "D. London, England": 
                return 0 
    if QuizOrder[Count2] == 2:          
        menu: 
            ch_e "What's my mutant power?"
            "A. Telekinesis": 
                return 0 
            "B. Ice Powers": 
                return 0 
            "C. Telepathy": 
                return 1 
            "D. Baking": 
                return 0 
    if QuizOrder[Count2] == 3: 
        ch_e "I was once a leader in a. . . social club."
        menu:
            ch_e "What was the name of that club?"
            "A. Akatsuki": 
                return 0 
            "B. The Pride": 
                return 0 
            "C. The Hellfire Club": 
                return 1 
            "D. The Sinister Six": 
                return 0 
                    
    if QuizOrder[Count2] == 4: 
        ch_e "I was once a leader in a. . . social club."
        menu:                
            ch_e "What was my title in that organization?"
            "A. The Black Queen": 
                return 0 
            "B. The White Queen": 
                return 1 
            "C. The Red Queen": 
                return 0 
            "D. Princess Powerful": 
                return 0 
    if QuizOrder[Count2] == 5: 
        ch_e "I have some clones wandering around. . . somewhere."
        menu:
            ch_e "What are they called?"
            "A. Kagebunshin": 
                return 0 
            "B. The Stepford Cuckoos": 
                return 1 
            "C. Jamie Maddrox": 
                return 0 
            "D. The Spice Girls": 
                return 0 
    if QuizOrder[Count2] == 6: 
        menu:
            ch_e "What is it called when a mutant develops a new ability, unrelated to their original one?" 
            "A. Secondary Mutation": 
                return 1 
            "B. Level-Up":
                return 0 
            "C. Digivolution": 
                return 0 
            "D. Super-Mutant": 
                return 0 
    if QuizOrder[Count2] == 7: 
        ch_e "I used to teach on an island nation of all mutants."
        menu:
            ch_e "What was it called?"
            "A. Australia": 
                return 0 
            "B. Genosha": 
                return 1 
            "C. Martinique": 
                return 0 
            "D. Whole Cake Island": 
                return 0 
    if QuizOrder[Count2] == 8: 
        menu:
            ch_e "When we first met, how did I trim my pubic hair?" 
            "A. Left natural": 
                return 0 
            "B. Shaved into an \"X\"": 
                return 0 
            "C. I don't know":    
                call EmmaFace("sadside", 1)
                if not E_SeenPussy:
                    ch_e "Boo, I thought you might at least take a guess. . ." 
                else:                    
                    ch_e "Clearly you weren't paying enough attention."
                call EmmaFace("normal")
                return 0 
            "D. Waxed clean":    
                call EmmaFace("sly", 1)
                ch_e "Someone was paying attention. . ."    
                return 1 
    if QuizOrder[Count2] == 9: 
        menu:
            ch_e "Name one of my horrible sisters."
            "A. Drucilla": 
                return 0 
            "B. Elsa": 
                return 0 
            "C. Adrienne": 
                return 1 
            "D. Cordelia": 
                return 1 
    if QuizOrder[Count2] == 10: 
        menu:
            ch_e "My previous teaching experience was at which Ivy League school?"
            "A. Deerfield Community College": 
                return 0 
            "B. Princeton": 
                return 0 
            "C. Empire State University": 
                return 0 
            "D. The Massachusetts Academy": 
                return 1

 #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1
    
#label Quiz:
#    $ Count = 0                                         #This is the number of times you've gotten a wrong answer. 
#    $ Count2 = 1                                        #this is the position in the quis so far. 
#    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # The entire list of objects. . .
#    $ renpy.random.shuffle(QuizOrder)                   # . . .shuffled randomly. . .    This is optional, and if you want to skip randomization then you can just increment a counter instead of this.
    
#    while Count2:                                       #This cycles so long as Count2 is greater than zero
#        "Question [Count2],"
#        call Quiz_Question
#        $ Count2 += 1                                   #This increments to the next question in the list after ti asks each one
#        if _return:                                     #the _return variable is whatever the Quiz Questions lable returns.
#            "You got it right!"
#            $ Score += 1                                #This tallies the right answers as you make them
#        else:
#            "Bzzt, Wrong answer"
#            $ Count += 1
#        if Count2 >= 14: #set this to one under the total number of questions
#            "You're done. Your score is [Score] out of 15."            
#            $ Count2 = 0           
#        elif Count > 2:                                 #this kicks you out if you get three wrong, remove that if you don't want it. 
#            "Too bad, you're done"
#            $ Count2 = 0                                #This breaks the cycle and returns the player to where he started the quiz. 
#    return
    
#label Quiz_Question:
#    if QuizOrder[Count2] == 1:                          #This asks the first question, set each following question to a number.
#        menu:
#            "Question"
#            "A. ":
#                return 1                                #the correct answer sends a 1, the incorrect answers send back a zero. 
#            "B. ":
#                return 0
#            "C. ":
#                return 0
#            "D. ":
#                return 0
          