﻿# Rogue_SexMenu //////////////////////////////////////////////////////////////////////
label Rogue_SexAct(Act = 0):
    call Shift_Focus("Rogue")
    if Act == "SkipTo":
        $ renpy.pop_call() #causes it to skip past the Trigger Swap
        $ renpy.pop_call() #causes it to skip past the cycle you were in before
        $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
        call SkipTo("Rogue")
    elif Act == "masturbate":         
        call RM_Prep
        if not Situation:
            return     
    elif Act == "lesbian":         
        call R_Les_Prep
        if not Situation:
            return   
    elif Act == "morningwood":
        # This action is called for by the label Rogue_Morning and returns to there
        $ R_RecentActions.append("blow")           
        $ R_DailyActions.append("blow")                          
        $ R_DailyActions.append("morningwood")         
        call Rogue_MorningWood
        if Situation == "blow": #If you selected to continue the BJ, then it calls the BJ actions
            $ Situation = 0
            call RBJ_Prep
        if not Situation:
            return
    elif Act == "kissing":        
        call R_KissPrep
        if not Situation:
            return   
    elif Act == "breasts":        
        call R_Fondle_Breasts
        if not Situation:
            return  
    elif Act == "blow":        
        call RBJ_Prep
        if not Situation:
            return  
    elif Act == "hand":        
        call RHJ_Prep
        if not Situation:
            return   
    elif Act == "sex":        
        call R_SexPrep
        if not Situation:
            return   

label Rogue_SexMenu: 
    call Shift_Focus("Rogue")
    $ Trigger = 0    
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Situation = 0
    call Rogue_Hide    
    $ Rogue_Arms = 1    
    call Set_The_Scene(1,0,0,0,1)
    
    if not P_Semen:
        "You're a little out of juice at the moment, you might want to wait a bit." 
    if P_Focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not R_Action:
        "Rogue's looking a bit tired out, maybe let her rest a bit."
    
    if "caught" in R_RecentActions or "angry" in R_RecentActions:  
        ch_r "I don't want to deal with you right now."
        call RogueOutfit        
        call DrainWord("Rogue","caught",1,0)
        return
        
    if Round < 5:
        ch_r "We've been at it for a while now, let's take a breather."   
        return
        
    menu Rogue_SMenu:  
        ch_r "So what would you like to do?"
        "Do you want to make out?":
                    if R_Action:
                        call R_Makeout
                    else:
                        ch_r "Sorry, [R_Petname], but I'm a bit worn out."  
                
        "Could I touch you?":
                if R_Action:
                    $ R_Mouth = "smile"                    
                    menu:
                        ch_r "Well where exactly were you interested in touching, [R_Petname]?"                        
                        "Could I give you a massage?":
                                call R_Massage                        
                        "Your breasts?":
                                call R_Fondle_Breasts
                        "Your thighs?":
                                call R_Fondle_Thighs
                        "Your pussy?":
                                call R_Fondle_Pussy
                        "Your Ass?":
                                call R_Fondle_Ass
                        "Never mind [[something else]":
                                jump Rogue_SMenu
                else:
                    ch_r "That sounds lovely, [R_Petname], but I'm a bit worn out."
                
        "Could you take care of something for me? [[Your dick, you mean your dick]":        
                if P_Semen and R_Action:                
                    menu:
                        ch_r "What did you have in mind, [R_Petname]?"
                        "Could you give me a handjob?":
                            call R_Handjob
                        "Could you give me a titjob?":
                            call R_Titjob         
                        "Could you suck my cock?":
                            call R_Blowjob 
                        "Could use your feet?":
                            call R_Footjob 
                        "Never mind [[something else]":
                            jump Rogue_SMenu
                elif not R_Action:
                        ch_r "Sorry [R_Petname], I'm a bit worn out."
                else:
                        "You really don't have it in you, maybe take a break." 
        
        "Could you put on a show for me?":
                    menu:
                        ch_r "What sort of show were you expecting?"
                        "Dance for me?":
                                if R_Action:
                                    $ Count = 1
                                    call R_Strip            
                                else:
                                    ch_r "Sorry [R_Petname], I'm a bit worn out."
                                
                        "Could you undress for me?": 
                                    call R_Undress  
                                            
                        "You've got a little something. . . [[clean-up]" if R_Spunk:
                                    ch_r "Oh?"
                                    call Rogue_Cleanup("ask") 
                                    
                        "Could I watch you get yourself off? [[masturbate]":
                                if R_Action:
                                    call R_Masturbate           
                                else:
                                    ch_r "Sorry [R_Petname], I'm a bit worn out."
                        
                        "Maybe make out with Kitty?" if K_Loc == bg_current:
                                call R_LesScene
                        "Maybe make out with Emma?" if E_Loc == bg_current:
                                call R_LesScene
                        
                        "Never mind [[something else]":
                            jump Rogue_SMenu
                    
        "Could we maybe?. . . [[fuck]":
                if R_Action:
                        menu:
                            "What did you want to do?"
                            "Turn around, I've got something in mind. . .":
                                    if P_Semen:
                                        call R_Doggy_H    
                                    else:
                                        "The spirit is apparently willing, but the flesh is spongy and bruised."        
                            "Fuck your pussy.":   
                                    if P_Semen:                     
                                        call R_Doggy_P   
                                    else:
                                        "The spirit is apparently willing, but the flesh is spongy and bruised."         
                            "Fuck your ass.":    
                                    if P_Semen:                    
                                        call R_Doggy_A      
                                    else:
                                        "The spirit is apparently willing, but the flesh is spongy and bruised."   
                            "How about some toys? [[Pussy]":        
                                    call R_Dildo_Pussy     
                            "How about some toys? [[Anal]":                        
                                    call R_Dildo_Ass   
                            "Never mind [[something else]":
                                jump Rogue_SMenu        
                else:
                        ch_r "Sorry [R_Petname], I'm a bit worn out."
        
        "Hey, do you want in on this? [[Threesome]" if not Partner:
                    menu:          
                        "Do you want to join us Kitty?" if K_Loc == bg_current:
                                if Partner == "Kitty":
                                    #if she's already involved
                                    ch_k "Lol, what are you even talking about?"
                                else: 
                                    call Kitty_Noticed("Rogue",1)
                                    if K_Loc == bg_current:
                                        ch_k "I could[K_like]give it a try. . ."
                                        
                        "Do you want to join us Emma?" if E_Loc == bg_current:
                                if Partner == "Emma":
                                    #if she's already involved
                                    ch_e "Have I not been keeping up?"
                                else: 
                                    call Emma_Noticed("Rogue",1)
                                    if E_Loc == bg_current:
                                        ch_e "So what did you have in mind for us. . ."
                                        
                        "Switch lead girl." if Partner:
                                if Partner == "Kitty":
                                    jump Kitty_SexMenu
                                if Partner == "Emma":
                                    jump Emma_SexMenu
                                    
                        "Never mind [[something else]":
                            pass
                    jump Rogue_SMenu
                                
        "Cheat Menu" if config.developer:                                                   #Remove            
                call Rogue_Cheat_Menu
            
        "Never mind. [[End]":            
                    if R_Lust >= 50 or R_Addict >= 50:
                        call RogueFace("sad")
                        if R_Action and R_SEXP >= 15 and Round > 20:
                                if "round2" not in R_RecentActions:  
                                    ch_r "Are you sure, [R_Petname]? I could really use some company."                
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
                                elif R_Addict >= 50:                        
                                    ch_r "I still need a little. . . contact." 
                                else:
                                    ch_r "Don't leave my hang'in, [R_Petname]."                          
                                menu:
                                    extend ""
                                    "Yeah, I'm done for now." if P_Semen and "round2" not in R_RecentActions:                 
                                        if "unsatisfied" in R_RecentActions and not R_OCount:                                
                                            call RogueFace("angry")
                                            $ R_Eyes = "side" 
                                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2)
                                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -4)
                                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)
                                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
                                            ch_r "Way to leave a girl in the lurch. . ."
                                        else:                               
                                            call RogueFace("bemused", 1)
                                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)   
                                            ch_r "Well, you did at least do your part. . ."  
                                    "I gave it a shot." if "round2" in R_RecentActions:                 
                                        if "unsatisfied" in R_RecentActions and not R_OCount:                                
                                            call RogueFace("angry")
                                            $ R_Eyes = "side"                                 
                                            ch_r "Way to leave a girl in the lurch. . ."
                                        else:                               
                                            call RogueFace("bemused", 1) 
                                            ch_r "Well, fair enough. . ."  
                                    "Hey, I did my part." if R_OCount > 2:      
                                        call RogueFace("sly", 1) 
                                        ch_r "I guess you did at that. . ."  
                                    "I'm tapped out for the moment, let's try again later." if not P_Semen:
                                        call RogueFace("normal")                        
                                        ch_r "Huh, can't be helped, I s'pose."
                                    "Ok, we can try something else." if MultiAction and "round2" not in R_RecentActions:
                                        call RogueFace("smile")
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1) 
                                        ch_r "Mmmm. . ."                            
                                        $ R_RecentActions.append("round2")                      
                                        $ R_DailyActions.append("round2") 
                                        jump Rogue_SexMenu
                                    "Again? Ok, fine." if MultiAction and "round2" in R_RecentActions:
                                        call RogueFace("sly")
                                        ch_r "Yeah, again. . ."           
                                        jump Rogue_SexMenu  
                                #End "if Rogue is still up for more"
                        else:  
                                call RogueFace("bemused", 1)
                                ch_r "I guess I'm a bit tuckered out too, [R_Petname]. I guess we can take a breather."                
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)    
                        call RogueFace
                    else:
                        ch_r "Huh? Ok."
                    
                    call Sex_Over
                    return
    if R_Loc != bg_current:
                call Set_The_Scene
                $ Trigger = 0    
                $ Trigger2 = 0
                $ Trigger3 = 0
                $ Trigger4 = 0
                $ Trigger5 = 0
                return
    if not MultiAction:    
                $ R_OCount = 0
                $ Trigger = 0    
                $ Trigger2 = 0
                $ Trigger3 = 0
                $ Trigger4 = 0
                $ Trigger5 = 0   
                call Set_The_Scene
                ch_r "That's it. . . for now."
                return
    call GirlsAngry
    jump Rogue_SexMenu
# end Rogue_SexMenu //////////////////////////////////////////////////////////////////////            

label Rogue_Cheat_Menu:
    menu:
        "Level-Up":
            $ R_Hand += 5
            $ R_Blow += 5
            $ R_Swallow += 5
            $ R_Hand += 5
            $ R_Slap += 5
            $ R_Tit += 5
            $ R_Sex += 5
            $ R_Anal += 5
            $ R_Hotdog += 5
            $ R_Mast += 5
            $ R_Org += 5
            $ R_FondleB += 5
            $ R_FondleT += 5
            $ R_FondleP += 5
            $ R_FondleA += 5
            $ R_DildoP += 5
            $ R_DildoA += 5
            $ R_Plug += 5
            $ R_SuckB += 5
            $ R_InsertP += 5
            $ R_InsertA += 5
            $ R_LickP += 5    
            $ R_LickA += 5
            $ R_Blow += 5
            $ R_Swallow += 5
            $ R_CreamP += 5
            $ R_CreamA += 5
            $ R_SeenChest = 1
            $ R_SeenPanties = 1
            $ R_SeenPussy = 1
            "Hand [R_Hand], Blow [R_Blow], Swallow [R_Swallow]"
        "Level Reset":
            $ R_Hand = 0
            $ R_Blow = 0
            $ R_Swallow = 0
            "Hand [R_Hand], Blow [R_Blow], Swallow [R_Swallow]"
        "Toggle Taboo":
            if not Taboo:
                $ Taboo = 40
            else:
                $ Taboo = 0
        "Maxed":
                $ R_Love = 1000
                $ R_Inbt = 1000
                $ R_Obed = 1000
                $ R_Lust = 50
                $ R_Addict = 0 #how addicted she is
                $ R_Addictionrate = 0 #How faster her addiciton rises
                $ R_Kissed = 1 #How many times they've kissed
                $ R_Swallow = 0
        "50\%":
                $ R_Love = 500
                $ R_Inbt = 500
                $ R_Obed = 500
                $ R_Lust = 65
                $ R_Addict = 0 #how addicted she is
                $ R_Addictionrate = 10 #How faster her addiciton rises
                $ R_Kissed = 10 #How many times they've kissed
                $ R_Swallow = 0
        "25\%":
                $ R_Love = 250
                $ R_Inbt = 250
                $ R_Obed = 250
                $ R_Lust = 85
                $ R_Addict = 10 #how addicted she is
                $ R_Addictionrate = 50 #How faster her addiciton rises
                $ R_Kissed = 10 #How many times they've kissed
                $ R_Swallow = 0
        "Juice up":
            $ P_Semen += 5
            $ R_Action = 10
        "Cold Shower":
            $ P_Focus = 0
        "Exit":
            return
    jump Rogue_Cheat_Menu
    return
    
    
# For when she tags you to drain you start ////////////////////////////////////////////////////////////////////////
label R_Tag(Forced = 0):
    call Shift_Focus("Rogue")
    $ R_Arms = 0
    $ Rogue_Arms = 2
    if not Forced:
            $ R_Eyes = "closed"
            $ R_Brows = "sad"
    if R_Addict <= 40 and not Forced:
            $ R_Addict -= 10          
            $ R_Addictionrate += 1 if R_Addictionrate < 5 else R_Addictionrate 
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
            "She pulls off her glove and touches your face for a moment. A shiver runs through her, then she puts them back on."        
    else:
        if Forced and P_Lvl >= 5:
            menu:
                "She pulls off her glove and reaches for your face."
                "Catch her arm [[refuse].":
                        call RogueFace("surprised", 1) 
                        "As she reaches out, you bat her arm away. The brief contact isn't enough for her."
                        call RogueFace("angry") 
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10)
                        
                        if R_Addict >= 85 and not ApprovalCheck("Rogue", 500, "O"): #if she's strung out and not obedient
                                $ R_Eyes = "manic"                        
                                "She lashes out and leaps at you, grabbing you by the chin."
                                $ R_Eyes = "sly"   
                                if "no tag" not in R_RecentActions:
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -5)
                                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 5)
                                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 1)   
                        else:
                                ch_r "Not cool, [R_Petname]."
                                if "no tag" not in R_RecentActions:
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)                    
                                $ R_RecentActions.append("no tag")
                                $ R_DailyActions.append("no tag")
                                $ R_Arms = "gloved"
                                $ Rogue_Arms = 1
                                return                        
                "Let her.":
                        "She touches your face."
        else:    
            "She pulls off her glove and touches your face."
        $ R_Blush = 2
        while R_Addict > 40:     
                $ R_Addictionrate += 1 if R_Addictionrate < 5 else 0 
                $ R_Addict -= 15  
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
                "As she continues to touch you, a slight shiver passes through her."
        "Appearing sated, she puts her gloves back on."  
        $ R_Blush = 1
    $ R_Arms = "gloved"
    $ Rogue_Arms = 1
    call RogueFace    
    if Forced:
            $ R_RecentActions.append("forced tag")
            $ R_DailyActions.append("forced tag")
    $ R_RecentActions.append("tag")
    $ R_DailyActions.append("tag")
    return
# End Rogue "tag" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label R_Jackin(Cnt = 0, TempVar = 0):
    if "unseen" in R_RecentActions:
            $ P_RecentActions.append("cockout") 
            $ Trigger2 = "jackin"
            "You whip out your cock and start working it." 
    else:
            if not P_Semen:
                "You don't think that would accomplish much, the poor thing is napping." 
                return
            
            if "cockout" in P_RecentActions:
                    "You start working your cock."
            else:
                    "You whip out your cock and start working it." 
                    $ P_RecentActions.append("cockout")
                    call Seen_First_Peen("Rogue",Partner)
            
            $ Trigger2 = "jackin"
            if "jackin" in R_RecentActions:
                return            
            $ R_RecentActions.append("jackin")
            $ R_DailyActions.append("jackin") 
            
            if R_SEXP < 10:
                    call RogueFace("surprised", 2) 
                    $ R_Eyes = "down"
                    "Rogue blushes furiously, shocked at your behavior."  
                    call RogueFace("angry", 1) 
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 5) 
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")  
                    $ renpy.pop_call()
                    return
            elif R_SEXP <= 15:            
                    call RogueFace("surprised", 2) 
                    $ R_Eyes = "down"
                    "Rogue looks down at your cock with surprise."
                    call RogueFace("perplexed", 1) 
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 8)
                    return
            elif ApprovalCheck("Rogue", 1100, TabM = 3):
                    call RogueFace("surprised", 1) 
                    $ R_Eyes = "down"
                    "Rogue looks down at your cock and smiles."            
                    call RogueFace("sly", 1) 
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 70, 8)
            elif ApprovalCheck("Rogue", 500, "I", TabM=2):
                    call RogueFace("surprised", 1) 
                    $ R_Eyes = "down"
                    "Rogue glances at it, but just smiles in amusement."        
                    call RogueFace("sly", 1) 
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 70, 10)
            else:
                    call RogueFace("angry", 1) 
                    $ R_Eyes = "down"
                    "Rogue glances down at your cock with a scowl."        
                    $ R_Eyes = "sexy"                
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")  
                    return
            
            if R_Action:
                $ Options = ["none"]
                
                if R_Hand >= 5 and ApprovalCheck("Rogue", 1100, TabM = 3):
                        $ Cnt = R_Hand - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("hand") 
                            $ Cnt -= 1
                if R_Blow >= 5 and ApprovalCheck("Rogue", 1300, TabM = 3):
                        $ Cnt = R_Blow - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if "hungry" in R_Traits else 0
                        while Cnt:
                            $ Options.append("blow") 
                            $ Cnt -= 1
                if R_Tit >= 5 and ApprovalCheck("Rogue", 1200, TabM = 5):
                        $ Cnt = R_Tit - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("Tit") 
                            $ Cnt -= 1
                if R_Sex >= 5 and ApprovalCheck("Rogue", 1400, TabM = 5):
                        $ Cnt = R_Sex - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if R_Lust >= 70 else 0
                        while Cnt:
                            $ Options.append("sex") 
                            $ Cnt -= 1
                if R_Anal >= 5 and ApprovalCheck("Rogue", 1550, TabM = 5):
                        $ Cnt = R_Anal - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if R_Lust >= 70 and R_Loose else 0
                        while Cnt:
                            $ Options.append("anal") 
                            $ Cnt -= 1
                    
                $ renpy.random.shuffle(Options) 
                
                $ TempVar = Options[0]  
                $ del Options[:]  
                
                if TempVar == "hand":
                        ch_r "Sure you don't want me to handle that for you?"
                elif TempVar == "blow":
                        ch_r "Sure my mouth wouldn't do better?"
                elif TempVar == "tit":
                        ch_r "Sure you wouldn't prefer using these?"
                elif TempVar == "sex":
                        ch_r "Oh, you're making me pretty wet here. . ."
                elif TempVar == "anal":
                        ch_r "You've really got my ass tingling. . ."
                else:
                        ch_r "I like what I'm seeing here. . ."
                        return
                    
                menu:
                    extend ""
                    "No thanks, I've got this in hand.":
                        ch_r "Your loss, [R_Petname]."
                        return
                    "Hmm, sounds like a plan.": 
                        $ Situation = "shift"
                
                $ Trigger2 = 0
                    
                #Close out what you were doing    
                if Trigger == "strip":
                        $ Count = 0
                        $ R_Action -= 1    
                        $ R_SpriteLoc = StageRight 
                elif Trigger == "masturbation":
                        $ R_Action -= 1
                        $ R_Mast += 1    
                        call Checkout          
                else:
                        call CloseOut("Rogue")
                                
                show blackscreen onlayer black
                hide blackscreen onlayer black
                if TempVar == "hand":                
                        jump RHJ_Prep
                elif TempVar == "blow":
                        jump RBJ_Prep
                elif TempVar == "tit":
                        jump RTJ_Prep
                elif TempVar == "sex":
                        jump R_SexPrep
                elif TempVar == "anal":
                        jump R_AnalPrep
    return
# End Rogue "jackin it" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label R_TouchCheek: 
    call Shift_Focus("Rogue") 
    call RogueFace("surprised", 1) 
    if "no cheek" in R_DailyActions:
        "You reach out to brush Rogue's face with your hand, but she slaps it away."
        call RogueFace("angry")
        ch_r "Back off, asshole."
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -2)
        return
    else:
        "You reach out and brush Rogue's face with your hand, a shiver runs through her."
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
    $ R_Addict -= 2            
    $ R_Addictionrate += 1 if R_Addictionrate < 5 else 0 
    $ R_Addictionrate = 3 if R_Addictionrate < 3 else R_Addictionrate 
    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 70, 5)
        
    if ApprovalCheck("Rogue", 1000):
        call RogueFace("sexy", 1)
        ch_r "A promise of things to come, [R_Petname]?"
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
    elif ApprovalCheck("Rogue", 500):
        call RogueFace("smile", 1)
        ch_r "That was. . . nice."      
    elif "cheek" in R_DailyActions:        
        call RogueFace("angry", 1)
        ch_r "Hey, I told you to cut that out already."
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -2)
        $ R_DailyActions.append("no cheek")
    elif ApprovalCheck("Rogue", 250):
        $ R_Mouth = "smile"
        $ R_Brows = "normal"
        ch_r "A. . . little warning maybe next time?"
    else:
        call RogueFace("angry", 1)
        ch_r "Don't. . . don't do that."   
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 1)
    
    if "no cheek" in R_DailyActions: 
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck("Rogue", 300):
                    call RogueFace("sexy", 1)
                    ch_r "Well, ok, just cut it out though."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                else:
                    call RogueFace("angry", 1)
                    $ R_Eyes = "side"
                    ch_r "A likely story. . ."                 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)   
                    
            "You know you wanted it.":
                if ApprovalCheck("Rogue", 300, "OI"):
                    call RogueFace("normal", 1)
                    $ R_Eyes = "squint"
                    ch_r "Well. . . I guess, maybe. . ."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, -1) 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)                        
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2)
                else:
                    call RogueFace("angry", 2)
                    $ R_Eyes = "squint"
                    ch_r "Like hell I did."  
                    $ R_Blush = 1
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, -3) 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 3)                        
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
    else:
        menu:
            "Sorry, you looked so cute there.":
                if ApprovalCheck("Rogue", 850, "LI"):
                    call RogueFace("sexy", 1)
                    ch_r "I'll make sure to collect on that later."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                elif ApprovalCheck("Rogue", 500, "LI"):
                    call RogueFace("smile", 1)
                    ch_r "Aw, you're sweet."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                else:
                    call RogueFace("angry", 1)
                    $ R_Eyes = "side"
                    ch_r "Don't you \"cute\" me, just cut it out. . ."                 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)   
                    
            "You had a fly on you.":
                if ApprovalCheck("Rogue", 850, "LI"):
                    call RogueFace("sexy", 1)
                    ch_r "Oh? Was that all. . ."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, 1)                        
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 1)
                elif ApprovalCheck("Rogue", 600):
                    call RogueFace("normal")
                    ch_r "A fly, right. . ."
                else:
                    call RogueFace("angry", 1)
                    ch_r "A likely story, look, just don't touch me." 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)    
                    
            "Are you sure you didn't enjoy that?":
                if ApprovalCheck("Rogue", 650, "LI"):
                    call RogueFace("sexy", 1)
                    $ R_Eyes = "side"
                    ch_r "I suppose I did, at that."
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)  
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 1)                        
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 1)
                elif ApprovalCheck("Rogue", 500, "OI"):
                    call RogueFace("normal", 1)
                    ch_r "Well. . . I guess, maybe. . . no, quit it."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, -1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)  
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)                        
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2)
                else:
                    call RogueFace("angry", 1)
                    $ R_Eyes = "side"
                    ch_r "Grrrr. . ."   
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, -3)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)  
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 3)                        
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2)   
            
    $ R_RecentActions.append("cheek")
    $ R_DailyActions.append("cheek")
    return
# End Rogue "touch cheek" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

# Slap Ass

label R_Slap_Ass:
    call Shift_Focus("Rogue")
    # fix add sound here?
    if renpy.showing("Rogue_Doggy"):
            show Rogue_Doggy #fix, test this
            with vpunch
    elif renpy.showing("Rogue_BJ_Animation"):           #fix, make this animation work better when paused for this effect.
            show Rogue_BJ_Animation
            with vpunch
    elif renpy.showing("Rogue_TJ_Animation"):
            show Rogue_TJ_Animation  
            with vpunch
    elif renpy.showing("Rogue_HJ_Animation"):
            show Rogue_HJ_Animation  
            with vpunch
    else:
            show Rogue
            with vpunch
            
    $ R_Slap += 1 #add in slap-base obedience  
        
    $ R_Blush = 2 if Taboo else 1
    if ApprovalCheck("Rogue", 200, "O", TabM=1):   
            call RogueFace("sexy", 1)  
            $ R_Mouth = "surprised"
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 51, 3, 1)
            if Action_Check("Rogue", "recent", "slap") < 4:
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2) if R_Slap <= 5 else R_Obed
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 1) if R_Slap <= 10 else R_Obed
            "You slap her ass and she jumps with pleasure."
    else:                
            call RogueFace("surprised", 1)        
            if Action_Check("Rogue", "recent", "slap") < 4:
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)        
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -1)
            "You slap her ass and she looks back at you a bit startled."  
        
    if Trigger and R_Lust >= 100:         
            #If you're still going at it and Rogue can cum
            call R_Cumming
                            
    if Taboo:    
            if not ApprovalCheck("Rogue", 800, TabM=2):
                    if R_Slap <= 5:
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)  
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)      
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2)    
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -1)
                    "She looks pretty mad though."  
            elif not ApprovalCheck("Rogue", 1500, TabM=2):
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2) if R_Slap <= 5 else R_Obed
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -1)
                    "She looks a bit embarrassed."  
            else:                         #Over 1500
                    call RogueFace("sexy")
                    $ R_Mouth = "smile"
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 1) if R_Slap <= 5 else R_Obed
                    "She gives you a naughty grin." 
            $ R_Blush = 1
                
    $ R_RecentActions.append("slap") if Action_Check("Rogue", "recent", "slap") < 4 else R_RecentActions
    $ R_DailyActions.append("slap") if Action_Check("Rogue", "daily", "slap") < 10 else R_DailyActions
        
    return
    
# Slap ass end ////////////////////////////////////////////////////////////////////////


# R_Makeout //////////////////////////////////////////////////////////////////////
label R_Makeout:
    call Shift_Focus("Rogue")
    
    $ Approval = ApprovalCheck("Rogue", 500, TabM=1) # 50, 65, 80, Taboo -40(90)
    
    if Approval > 1 and not R_Kissed:        
        call RogueFace("sexy")
        $ R_Eyes = "side"
        ch_r "I've never really been able to do this, so I'm a bit excited to try. . ."   
    if Approval and not R_Kissed:        
        call RogueFace("sexy")
        $ R_Eyes = "side"
        ch_r "I guess it's worth a shot. . ."   
    elif Approval and "kissing" in R_RecentActions:
            call RogueFace("sexy", 1)
            ch_r "Mmm. . ."
            jump R_KissPrep
    elif Approval and "kissing" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["Gimme some sugar, sugar.",       
            "Didn't get enough earlier?",
            "{i}I'm{/i} used to being the one sucking people dry. . ."]) 
        ch_r "[Line]"
            
    elif Approval > 1 and R_Love > R_Obed:       
        call RogueFace("sexy")
        ch_r "Sure, why not?"   
    elif ApprovalCheck("Kitty", 500, "O") and R_Obed > R_Love:
        call RogueFace("normal")
        ch_r "If you wish."
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
    elif ApprovalCheck("Rogue", 250, "O") and ApprovalCheck("Rogue", 250, "L"): 
        call RogueFace("sexy")
        ch_r "Ok, fine."
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
    elif R_Addict >= 50:
        call RogueFace("sexy")
        $R_Eyes = "manic"
        ch_r "Hm. . . ok, let's do this."    
    elif Approval:       
        call RogueFace("bemused")
        ch_r "hmm, ok." 
    else:        
        call RogueFace("normal") # Else
        $ R_Mouth = "sad"
        ch_r "Nah, I don't think I'm interested."
        $ R_RecentActions.append("no kissing")                      
        $ R_DailyActions.append("no kissing") 
        return    
        
label R_KissPrep:    
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 10, 1)
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 20, 1)
    call R_Kissing_Launch("kiss you")
    if R_Kissed >= 10 and R_Inbt >= 300:
        call RogueFace("sucking")
    elif R_Kissed > 1 and R_Addict >= 50:
        call RogueFace("sucking")
    else:
        call RogueFace("kiss",2) 
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no kissing")
    
    if not R_Kissed: 
                #If it's the first time, it's only a simple kiss and then ends
                "You lean in and your lips meet Rogue's." 
                $ R_Eyes = "surprised"
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 15)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, 30) 
                "A slight spark passes between you and her eyes widen with surprise."
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 70, 5) 
                ch_r "Wow, [R_Petname], that was really something. . ."
                call RogueFace("bemused",1) 
                ch_r "Not the kind of zap I'm used to."
                $ R_Addict -= 5                 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 20)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 30)
                jump R_Kiss_After
    
    
    if R_Kissed >= 10 and R_Lust >= 80:
        "She's all over you, kissing all over your face and grinding against you."  
    elif R_Kissed > 7:
        "You deeply and passionately."
    elif R_Kissed > 3:
        "She's really getting into it, there's some heavy tongue action."
    else:
        "You and Rogue make out for a while." 
    $ Cnt = 0
    $ Trigger = "kiss you"
    $ Line = 0
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
     
label R_KissCycle:
    while Round >=0:
        call Shift_Focus("Rogue")
        call R_Kissing_Launch("kiss you")       
        call RogueLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                  
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                pass         
                                                        
                        "Slap her ass":                     
                                    call R_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump R_KissCycle  
                        
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Start jack'in it." if MultiAction and Trigger2 != "jackin":
                                call R_Jackin                        
                        "Stop jack'in it." if MultiAction and Trigger2 == "jackin":
                                "You stop jack'in it."
                                $ Trigger2 = 0
                                
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if R_Action and MultiAction:
                                                call Rogue_Offhand_Set
                                                if Trigger2:
                                                     $ R_Action -= 1
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if R_Action and MultiAction:
                                                    menu:  
                                                        "Move a hand to her breasts. . ." if R_Kissed >= 5 and MultiAction:
                                                                if R_Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call R_Kiss_After
                                                                    call R_Fondle_Breasts                          
                                                                    if Trigger == "fondle breasts": 
                                                                        $ Trigger2 = "kiss you"                                   
                                                                        call RFB_Prep   
                                                                    else: 
                                                                        $ Trigger = "kiss you"     
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                        "Move a hand to her thighs. . ." if R_Kissed >= 5 and MultiAction:
                                                                if R_Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call R_Kiss_After
                                                                    call R_Fondle_Thighs   
                                                                    if Trigger == "fondle thighs": 
                                                                        $ Trigger2 = "kiss you"      
                                                                        call RFT_Prep 
                                                                    else: 
                                                                        $ Trigger = "kiss you"     
                                                                else:
                                                                    "As your hands creep downwards, she grabs your wrists."
                                                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                                        "Never Mind":
                                                                jump R_KissCycle
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Rogue to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Rogue_Les_Change
                                            "Ask Rogue to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        if Partner == "Kitty":
                                                            call Kitty_Three_Change("Rogue")
                                                        elif Partner == "Emma":
                                                            call Emma_Three_Change("Rogue")                                                  
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0          
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Rogue")
                                            "Undress [Partner]":
                                                        if Partner == "Kitty":
                                                                call K_Undress   
                                                        elif Partner == "Emma":
                                                                call E_Undress 
                                            "Clean up Partner":
                                                        if Partner == "Kitty" and K_Spunk:
                                                                call Kitty_Cleanup("ask")    
                                                        elif Partner == "Emma" and E_Spunk:
                                                                call Emma_Cleanup("ask")  
                                                        else:
                                                                "She seems fine."
                                                                jump R_KissCycle 
                                            "Never mind":
                                                        jump R_KissCycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump R_KissCycle 
                        
                        "Back to Sex Menu" if MultiAction and R_Kissed >= 5:  
                                ch_p "Let's try something else." 
                                $ Situation = "shift"
                                $ Line = 0
                                jump R_Kiss_After
                        "End Scene": 
                                ch_p "Let's stop for now."
                                $ Line = 0
                                jump R_Kiss_After
        #End menu (if Line)
        
        call Shift_Focus("Rogue")
        call Sex_Dialog("Rogue",Partner)
        
        $ Cnt += 1
        $ Round -= 1  
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up     
        if P_Focus >= 100 or R_Lust >= 100:      
                    #If either of you could cum   
                    if P_Focus >= 100: 
                            #If you can cum:
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                    $ R_RecentActions.append("unsatisfied")                      
                                    $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump R_Kiss_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:       
                            #If you're still going at it and Rogue can cum
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump R_Kiss_After            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump R_Kiss_After                 
                
        if Partner:
                #Checks if partner could orgasm
                if Partner == "Kitty" and K_Lust >= 100:                                          
                    call K_Cumming
                elif Partner == "Emma" and E_Lust >= 100:                                          
                    call E_Cumming
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
label R_Kiss_After:
    call RogueFace("sexy") 
    
    $ R_Kissed += 1
    $ R_Action -=1
    $ R_Addictionrate += 2 if R_Addictionrate < 5 else 1 
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    
    call LikeUpdater("Rogue",1)
    
    if "kissing" not in K_RecentActions:
        if R_Love > 300:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, 4)
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 1)
        $ R_RecentActions.append("kissing")                      
        $ R_DailyActions.append("kissing") 
     
    if R_Kissed > 10: 
            pass        
    elif R_Kissed == 10:
            call RogueFace("smile", 1)        
            ch_r "You must really like my lips, huh?"    
    elif R_Kissed == 5:
        ch_r "We're really making this a regular thing."  
    elif R_Kissed == 1:    
        $ R_SEXP += 1 
        
    if not Situation and R_Kissed > 5 and R_Lust > 50 and ApprovalCheck("Rogue", 950):
            call RogueFace("sexy", 1)
            $R_Brows = "sad"
            ch_r "You maybe want to try something more?"  
     
    $ Tempmod = 0  
    if Situation:
        ch_r "Mmm, so what else did you have in mind?"
    else:
        call R_Pos_Reset  
    call Checkout
    return


# end Makeout //////////////////////////////////////////////////////////////////////

            
##  R_Masturbating //////////////////////////////////////////////////////////////////////
# Cnt 1 means she's seen you, Cnt 0 means she hasn't.
label R_Masturbate: #(Situation = Situation):
    call Shift_Focus("Rogue")
    if R_Mast:
        $ Tempmod += 10
    if R_SEXP >= 50:
        $ Tempmod += 25
    elif R_SEXP >= 30:
        $ Tempmod += 15
    elif R_SEXP >= 15:
        $ Tempmod += 5
    if R_Lust >= 90:
        $ Tempmod += 20
    elif R_Lust >= 75:
        $ Tempmod += 5
    if "exhibitionist" in R_Traits:      
        $ Tempmod += (3*Taboo) 
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount   
        
    $ Approval = ApprovalCheck("Rogue", 1200, TabM = 2) # 120, 135, 150, Taboo -80(200)
    
    call DrainWord("Rogue","unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "join":       # This triggers if you ask to join in        
                if Approval > 1 or (Approval and R_Lust >= 50):
                    menu:        
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if P_Semen and R_Action:
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                call RogueFace("sexy")
                                ch_r "Well, [R_Petname], I suppose I could use some help with these. . ."                  
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ R_Mast += 1
                                jump RM_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if P_Semen and R_Action:
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                                call RogueFace("sexy")
                                ch_r "Well, [R_Petname], I suppose you could help me with these. . ."                
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ R_Mast += 1
                                jump RM_Cycle
                        "Why don't we take care of each other?" if P_Semen and R_Action:
                                call RogueFace("sexy")
                                ch_r "Well what did you have in mind?"                    
                                $ renpy.pop_call()          #removes the call to this label 
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if R_Lust >= 50:
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)      
                                    call RogueFace("sexy")
                                    ch_r "Well, [R_Petname], I suppose I do at that . ."                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)  
                                    jump RM_Cycle
                                elif ApprovalCheck("Rogue", 1000):
                                    call RogueFace("sly")                        
                                    ch_r "Well I did, but I think I've got it taken care of for now. . ."
                                else:
                                    call RogueFace("angry")
                                    ch_r "Well I did, but now you've blown the mood."
                                    
                #else: You've failed all checks so she kicks you out.
                $ Rogue_Arms = 1  
                call RogueOutfit  
                $ R_Action -= 1
                $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0      
                $ renpy.pop_call()          #removes the call to this label 
                if Approval:     
                        call RogueFace("bemused", 2)
                        if bg_current == "bg rogue":
                            ch_r "So what did you come over for anyway, [R_Petname]?"   
                        else:
                            ch_r "So . . . fancy bumping into you here, [R_Petname]. . ." 
                        $ R_Blush = 1
                else:
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                        call RogueFace("angry")
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")  
                        if bg_current == "bg rogue":
                            ch_r "Well if you don't mind, I'd kind of appreciate you getting out of here. Maybe knock next time?"
                            "Rogue kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map  
                        else:
                            ch_r "Well if you don't mind, I'm getting out of here. Maybe knock next time?"
                            call Remove_Girl("Rogue")
                return                      #returns to sexmenu, which returns to original    
    #End of "Join" option
    
    
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
                if Approval > 2:                                                      # fix, add rogue auto stuff here
                        if R_Legs == "skirt":
                            "Rogue's hand snakes down her body, and hikes up her skirt."
                            $ R_Upskirt = 1
                        elif R_Legs == "pants":
                            "Rogue slides her hand down her body and into her jeans."  
                        elif HoseNum("Rogue") >= 5:
                            "Rogue's hand slides down her body and under her [R_Hose]."
                        elif R_Panties:                
                            "Rogue's hand slides down her body and under her [R_Panties]."
                        else:
                            "Rogue's hand slides down her body and begins to caress her pussy."
                        $ R_SeenPanties = 1
                        "She starts to slowly rub herself."
                        menu:
                            "What do you do?"
                            "Nothing.":                    
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)
                                    "Rogue begins to masturbate."
                            "Go for it.":       
                                    call RogueFace("sexy, 1")                    
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                                    ch_p "That is so sexy, [R_Pet]."
                                    call Rogue_Namecheck
                                    "You lean back and enjoy the show."
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                            "Ask her to stop.":
                                    call RogueFace("surprised")       
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                                    ch_p "Let's not do that right now, [R_Pet]."
                                    call Rogue_Namecheck
                                    "Rogue pulls her hands away from herself."
                                    call RogueOutfit
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)
                                    return            
                        jump RM_Prep
                else:                
                        $ Tempmod = 0                               # fix, add rogue auto stuff here
                        $ Trigger2 = 0
                return            
    #End if Rogue intitiates this action
    
    #first time
    if not R_Mast:                                                                
            call RogueFace("surprised", 1)
            $ R_Mouth = "kiss"
            ch_r "You want me to get myself off, while you watch?"
            if R_Forced:
                call RogueFace("sad")
                ch_r "So you just want to watch then?"
            
            
    #First time dialog             
    if not R_Mast and Approval:                                                      
            if R_Forced: 
                call RogueFace("sad")
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            elif R_Love >= (R_Obed + R_Inbt):
                call RogueFace("sexy")
                $ R_Brows = "sad"
                $ R_Mouth = "smile" 
                ch_r "Since my love life's been a bit. . . limited, I've gotten pretty good at this."          
            elif R_Obed >= R_Inbt:
                call RogueFace("normal")
                ch_r "If that's what you want, [R_Petname]. . ."            
            else: # Uninhibited 
                call RogueFace("sad")
                $ R_Mouth = "smile"             
                ch_r "I guess it could be fun with you watching. . ."    
    
    
    #Second time+ initial dialog
    elif Approval:                                                                       
            if R_Forced: 
                call RogueFace("sad")
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
                ch_r "You want to watch me again?"  
            elif Approval and "masturbation" in R_RecentActions:
                call RogueFace("sexy", 1)
                ch_r "I guess I have a bit more in me. . ."    
                jump RM_Prep
            elif Approval and "masturbation" in R_DailyActions:
                call RogueFace("sexy", 1)
                $ Line = renpy.random.choice(["You enjoyed the show?",       
                    "Didn't get enough earlier?",
                    "It is nice to have an audience. . ."]) 
                ch_r "[Line]"            
            elif R_Mast < 3:        
                call RogueFace("sexy", 1)
                $ R_Brows = "confused"
                ch_r "You like to watch, huh?"       
            else:       
                call RogueFace("sexy", 1)
                $ Rogue_Arms = 2
                $ Line = renpy.random.choice(["You sure do like to watch.",                 
                    "So you'd like me to go again?",                 
                    "You want to watch some more?",
                    "You want me ta diddle myself?"]) 
                ch_r "[Line]"
                $ Line = 0
    #End second time+ initial dialog
    
    #If she's into it. . .  
    if Approval >= 2:                                                                                
            if R_Forced:
                call RogueFace("sad")
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                ch_r "I suppose, let me get comfortable. . ." 
            else:
                call RogueFace("sexy", 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "I suppose it would help to have something nice to look at. . .",
                    "I've kind of needed this anyways. . .",
                    "Sure!", 
                    "I guess I could. . . give it a go.",
                    "Heh, ok, ok."]) 
                ch_r "[Line]"
                $ Line = 0
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
            jump RM_Prep   
            
    #If she's not into it, but maybe. . .    
    else:                                                                                       
        menu:
            ch_r "That's. . . a little intimate, [R_Petname]."
            "Maybe later?":
                    call RogueFace("sexy", 1)  
                    if R_Lust > 50:
                        ch_r "Well, definitely later. . . but I'll have to think about inviting you."
                    else:
                        ch_r "Hmm, maybe. . . I'll let you know."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)               
                    return
            "You look like you could use it. . .":             
                    if Approval:
                        call RogueFace("sexy")     
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Well. . . ok.",                 
                            "I suppose it would help to have something nice to look at. . .",
                            "I've kind of needed this anyways. . .",
                            "Sure!", 
                            "I guess I could. . . give it a go.",
                            "Heh, ok, ok."]) 
                        ch_r "[Line]"
                        $ Line = 0                   
                        jump RM_Prep
                    else:   
                        pass
                    
            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Rogue", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and R_Forced):
                        call RogueFace("sad")
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)                 
                        ch_r "Ok, fine. I'll give it a try."  
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 4)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                        $ R_Forced = 1  
                        jump RM_Prep
                    else:                              
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -20)     
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")
    # end of asking her to do it
    
    #She refused all offers.
    $ Rogue_Arms = 1                
    if R_Forced:
            call RogueFace("angry", 1)
            ch_r "I'm not doing something so. . . intimate with you watching."
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)         
            if R_Love > 300:
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)    
            $ R_RecentActions.append("angry")
            $ R_DailyActions.append("angry")   
            $ R_RecentActions.append("no masturbation")                      
            $ R_DailyActions.append("no masturbation") 
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            call RogueFace("angry", 1)          
            $ R_DailyActions.append("tabno") 
            ch_r "I can't do that here!"     
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)  
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)    
            return                
    elif R_Mast:
            call RogueFace("sad") 
            ch_r "Nope, not anymore, you'll have to go back to Internet porn."     
    else:
            call RogueFace("normal", 1)
            ch_r "Heh, no, I'm not doing that."  
    $ R_RecentActions.append("no masturbation")                      
    $ R_DailyActions.append("no masturbation") 
    $ Tempmod = 0 
    return

label RM_Prep: 
    $ R_Upskirt = 1    
    $ R_PantiesDown = 1 
    call Set_The_Scene  
    
    #if she hasn't seen you yet. . .
    if "unseen" in R_RecentActions:
            call RogueFace("sexy")
            $ R_Eyes = "closed"
            $ Rogue_Arms = 2
            "You see Rogue leaning back, masturbating. You don't think she's noticed you yet."
    else:    
            call RogueFace("sexy")
            $ Rogue_Arms = 2
            "Rogue lays back and starts to toy with herself."
            if not R_Mast:#First time        
                    if R_Forced:
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -20)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 45)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 35) 
                    else:
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 15)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 35)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 40)  
        
    
    $ Trigger = "masturbation"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no masturbation")
    $ R_RecentActions.append("masturbation")                      
    $ R_DailyActions.append("masturbation") 
            
label RM_Cycle:      
    $ Trigger = "masturbation"
    
    if Situation == "join":
        # resets the call made to this option
        $ renpy.pop_call() 
        $ Situation = 0 
        
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call RogueLust  
        if "unseen" in R_RecentActions:  
                $ R_Eyes = "closed"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if  P_Focus < 100:                                                    
                    #Player Command menu                                        
                    menu:
                        "Keep Watching.":
                                pass
                                
                        "Rogue. . .[[jump in]" if "unseen" not in R_RecentActions:                 
                                "Rogue slows what she's doing with a sly grin."
                                ch_r "Yeah, did you want something, [R_Petname]?"
                                $ Situation = "join"
                                call R_Masturbate               
                        "\"Ahem. . .\"" if "unseen" in R_RecentActions:  
                                jump RM_Interupted    
                                                   
                        "Start jack'in it." if Trigger2 != "jackin":
                                call R_Jackin                   
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0    
                                            
                        "Slap her ass":    
                                if "unseen" in R_RecentActions:
                                        "You smack Rogue firmly on the ass!"
                                        jump RM_Interupted                                          
                                else:
                                        call R_Slap_Ass                                        
                                        $ Cnt += 1
                                        $ Round -= 1    
                                        jump RM_Cycle  
                           
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Change what I'm doing":
                                menu:
                                    "Offhand action":
                                            if R_Action and MultiAction:
                                                call Rogue_Offhand_Set
                                                if Trigger2:
                                                     $ R_Action -= 1
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                           
                                    "Threesome actions (locked)" if not Partner or "unseen" in R_RecentActions: 
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in R_RecentActions:   
                                        menu:
                                            "Ask [Partner] to do something else":
                                                        if Partner == "Kitty":
                                                            call Kitty_Three_Change("Rogue")
                                                        elif Partner == "Emma":
                                                            call Emma_Three_Change("Rogue")     
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Rogue")
                                            "Undress [Partner]":
                                                        if Partner == "Kitty":
                                                                call K_Undress   
                                                        elif Partner == "Emma":
                                                                call E_Undress 
                                            "Clean up Partner":
                                                        if Partner == "Kitty" and K_Spunk:
                                                                call Kitty_Cleanup("ask")    
                                                        elif Partner == "Emma" and E_Spunk:
                                                                call Emma_Cleanup("ask")  
                                                        else:
                                                                "She seems fine."
                                                                jump RM_Cycle 
                                            "Never mind":
                                                        jump RM_Cycle 
                                    "Undress Rogue":
                                            if "unseen" in R_RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump RM_Interupted
                                            else:                                        
                                                    call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            if "unseen" in R_RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump RM_Interupted
                                            else:                      
                                                    call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RM_Cycle                               
                         
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RM_Interupted
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RM_Interupted
        #End menu (if Line)
        
        call Shift_Focus("Rogue")
        call Sex_Dialog("Rogue",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:
                        if "unseen" not in R_RecentActions: 
                            #if she knows you're there
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ P_Focus = 95
                            jump RM_Interupted
     
                    #If Rogue can cum
                    if R_Lust >= 100:                                               
                        call R_Cumming
                        jump RM_Interupted
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                            "Rogue still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump RM_Cycle  
                                "No, I'm done.":
                                    "You pull back."
                                    return
        if Partner:
                #Checks if partner could orgasm
                if Partner == "Kitty" and K_Lust >= 100:                                          
                    call K_Cumming
                elif Partner == "Emma" and E_Lust >= 100:                                          
                    call E_Cumming                    
        #End orgasm
        
        if "unseen" in R_RecentActions:
                if Round == 10:
                    "It's getting a bit late, Rogue will probably be wrapping up soon."  
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if Round == 10:
                    ch_r "We might want to wrap this up, it's getting late."  
                    $ R_Lust += 10
                elif Round == 5:
                    ch_r "Seriously, it'll be time to stop soon."     
                    $ R_Lust += 25   
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    if "unseen" not in R_RecentActions:
        ch_r "Ok, [R_Petname], that's enough of that for now."
    
label RM_Interupted:
    
    # If she hasn't noticed you're there before cumming
    if "unseen" in R_RecentActions:                         
                call RogueFace("surprised", 1)
                "Rogue stops what she's doing with a start, eyes wide."
                call Rogue_First_Bottomless(1) 
                call RogueFace("surprised", 1)
                
                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_r "H- how long you been stand'in there, [R_Petname]?" 
                        $ R_Eyes = "down"
                        menu:
                            ch_r "And why is your cock out like that?!"
                            "Long enough, it was an excellent show.":   
                                    call RogueFace("sexy")
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
                                    ch_r "Well, I imagine it was. . ."
                                    if R_Love >= 800 or R_Obed >= 500 or R_Inbt >= 500:
                                        $ Tempmod += 10
                                        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
                                        ch_r "And the view from this angle ain't so bad either. . ."  
                                    
                            "I. . . just got here?":
                                    call RogueFace("angry")                   
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_r "A likely story . . ."   
                                    if R_Love >= 800 or R_Obed >= 500 or R_Inbt >= 500:
                                            $ Tempmod += 10
                                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
                                            call RogueFace("bemused", 1)
                                            ch_r "Still, can't blame a fella for take'in inspirations."   
                                    else:
                                            $ Tempmod -= 10
                                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, -5)
                        call Seen_First_Peen("Rogue",Partner) 
                                    
                #you haven't been jacking it                    
                else:         
                        ch_r "H- how long you been stand'in there, [R_Petname]?"        
                        menu:
                            extend ""
                            "Long enough.":   
                                    call RogueFace("sexy", 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
                                    ch_r "Well I hope you got a good show out of it. . ."
                            "I just got here.":
                                    call RogueFace("bemused", 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)                    
                                    ch_r "A likely story . . ."   
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)    
                                
                call DrainWord("Rogue","unseen",1,0) #She sees you, so remove unseens
                $ R_Mast += 1
                if Round <= 10:
                    ch_r "It's getting too late to do much about it right now though."
                    return
                $ Situation = "join"        
                call R_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen
    
    #else, if She's seen you already    
    $ R_Action -= 1
    $ R_Mast += 1    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
            $ K_LikeRogue += 3 if K_LikeRogue >= 800 else 1
    if E_Loc == bg_current and "noticed rogue" in E_RecentActions: #If Emma was participating
            $ E_LikeRogue += 4 if E_LikeRogue >= 800 else 1
    call Checkout
    if Situation == "shift":        
        $ Situation = 0
        return
    $ Situation = 0
    if Round <= 10:
            ch_r "I need to take a little break here, [R_Petname]."
            return
    call RogueFace("sexy", 1)
    if R_Lust < 20:
        ch_r "That really worked for me, [R_Petname]. How about you?"
    else:
        ch_r "Yeah, what did you want?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if P_Semen and R_Action:
                $ Situation = "shift"
                return   
        "You could just keep going. . ." if P_Semen:
                call RogueFace("sly")
                if R_Action and Round >= 10:
                    ch_r "Well, alright. . ."
                    jump RM_Cycle
                else:
                    ch_r "I'm kinda worn out, maybe time for a break. . ."
        "I'm good here. [[Stop]":  
                if R_Love < 800 and R_Inbt < 500 and R_Obed < 500:
                    call RogueOutfit
                call RogueFace("normal")
                $ R_Brows = "confused"
                ch_r "Well. . . ok then. . ."
                $ R_Brows = "normal" 
        "You should probably stop for now." if R_Lust > 30:
                call RogueFace("angry")
                ch_r "Well if you say so."
    return
    
    
    
## end R_Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////











# Rogue_Offhand function //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


label Rogue_Offhand(TempLine=0):
    #This is the dialog for what you're doing with your other hand while a primary action takes place
    
    $ D20 = renpy.random.randint(1, 20)                                                                 # Taboo caught check
                    
    if not Trigger2: #If there are no offhand options set, return
        return    
    
    if Trigger2 == "kiss you":
                $ Line = renpy.random.choice([". Your lips gently slide across hers.", 
                        ". Her lips part as you hold her close.",    
                        ". You nibble her neck as she groans in pleasure.",
                        ". You squeeze her tightly as your tongues jostle.",
                        ". Her tongue dances around yours.",
                        ". She nibbles your ear as her hands slide across your back.",
                        ". Your hands slide down her body as your lips press hers.",
                        ". You kiss her passionately.", 
                        ". Your tongues swirl around each other's."])
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 75, 1) if R_Love >= 300 else R_Love
                $ PrimaryLust += 2 if R_Lust < 50 else 1
        
    elif Trigger2 == "fondle breasts":
                $ Line = renpy.random.choice([". You reach out and massage her glorious breasts.", 
                        ". You pass your hands gently over her warm breasts.", 
                        ". Her nipples catch lightly on your fingers as you grasp her warm flesh, you can feel them stiffen.",
                        ". She gasps as you lightly thumb her rigid nipples."])
                $ PrimaryLust += 3           
                $ TempFocus += 2 if P_Focus < 90 else 0 
        
    elif Trigger2 == "suck breasts":
            if R_Chest:
                $ Line = renpy.random.choice([". You bend down and motor-boat her breasts.",
                    ". You tease her nipples with your tongue through her top.",
                    ". You slowly lick her nipples through her moist top.", 
                    ". you gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    ". She gasps as you lightly lick her rigid nipples, poking through her top."])            
            else:
                $ Line = renpy.random.choice([". You bend down and motor-boat her breasts.",
                    ". You gently nibble at her nipples as you suck on them.",
                    ". You tease her nipples with your tongue.",
                    ". You slowly lick around, and then blow across her nipples.", 
                    ". You gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    ". She gasps as you lightly lick her rigid nipples."])
            $ PrimaryLust += 4 if 60 < R_Lust < 80 else 2  
            $ TempFocus += 3 if P_Focus < 90 else 0 
        
    elif Trigger2 == "fondle pussy":
            
            $ Line = renpy.random.choice([". You put your hand against her mound and grind against it.", 
                        ". You reach into her gap and she gasps as you slide your hand across and stroke her lips.", 
                        ". Her legs twitch a bit as you press your thumb against her.",
                        ". You slide a hand up her inner thigh, she moans a little as you reach the point where they meet."])
            $ PrimaryLust += 4 if 60 < R_Lust < 90 else 2        
            $ TempFocus += 4 if P_Focus < 90 else 0 
        
    elif Trigger2 == "lick pussy":
            if R_Legs != "pants" and not R_Panties:  
                $ Line = renpy.random.choice([". You slide your tongue into her pussy and flick the roof with deft strokes.", 
                    ". You spread the lips back and she gasps as you slide your tongue between them.", 
                    ". You can feel her twitching as you grind your tongue against her clit.",
                    ". She gasps as you suck on her clit.",
                    ". You rub her clit with your thumb as you dive into her pussy with your tongue.",
                    ". With a little nibble, you tug on her lower lips.",
                    ". You slowly lick into her gap and she gasps as you press the walls aside."])
            else:
                $ Line = renpy.random.choice([". You spread the lips back beneath the thin fabric, and she gasps as you slide your tongue across them.", 
                    ". She gasps as you suck on her clit through the fabric.",
                    ". You rub her clit with your thumb as you press against her pussy with your tongue.",
                    ". You put your hand against her mound and lick the juice that's collected.", 
                    ". With a little nibble, you tug back the fabric.",
                    ". You slowly lick into her gap and she gasps as you press the walls aside."])
            $ PrimaryLust += 5 if R_Lust > 50 else 2       
            $ TempFocus += 4 if P_Focus < 90 else 0 
            
    elif Trigger2 == "fondle ass":
            if R_Legs != "pants" and not R_Panties: 
                $ Line = renpy.random.choice([". You reach out and brush your hands across her bare ass.", 
                        ". You put your hand against her firm rear and grind against it.", 
                        ". You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        ". Her legs twitch a bit as you press your thumb against her.",
                        ". She gasps as you reach under her and lightly stroke her ass.",
                        ". You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            else:
                $ Line = renpy.random.choice([". You reach out and brush your hands across her ass.", 
                        ". You put your hand against her firm rear and grind against it.", 
                        ". You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        ". Her legs twitch a bit as you press your thumb against her.",
                        ". She gasps as you reach under her and lightly stroke her ass.",
                        ". You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            $ PrimaryLust += 2 if R_Lust < 50 else 1
            $ TempFocus += 1 if P_Focus < 50 else 0  
            $ TempFocus += 1 if P_Focus < 80 else 0   
        
    elif Trigger2 == "insert ass":
            $ Line = renpy.random.choice([". You reach out and slide a finger into her ass.", 
                    ". You slide a finger into her asshole and stroke the roof of it.", 
                    ". You can feel her twitching as you press your thumb against her clit.",
                    ". She gasps as you rub her asshole with your fingers.",
                    ". You rub her pussy with your thumb as you dive into her asshole with your middle finger.",
                    ". You reach into her gap and she gasps as you slide your hand across and press against her hole.", 
                    ". She gasps as you reach under her warm lips and lightly stroke her ass."])       
            $ PrimaryLust += 3 if R_Lust > 70 and R_Loose else 1
            $ TempFocus += 2 if P_Focus < 90 else 0 
        
    elif Trigger2 == "jackin":
            if Trigger == "masturbation":
                    $ Line = ". You stroke your cock as you watch her go."
            elif Trigger == "lesbian":
                    $ Line = ". You stroke your cock as you watch them."
            elif Trigger == "hand":
                    $ Line = renpy.random.choice([". You also give it a little rub.", 
                            ". As she does so, you polish the knob a bit.", 
                            ", and you help.",
                            ", your hand bumps into hers occasionally."])     
            elif Trigger == "blow":
                    if Speed >= 3:
                        $ Line = "."
                    else:
                        $ Line = renpy.random.choice([". You also give it a little rub.", 
                            ". As she does so, you work the shaft a bit.", 
                            ", and you help.",
                            ", her lips brush your hand occasionally."])    
            else:
                    $ Line = renpy.random.choice([", and with your other hand, you stroke your shaft.", 
                            ". You stroke your cock with your other hand.", 
                            ", and as you do, you stoke yourself."])   
            if "unseen" not in R_RecentActions:
                $ PrimaryLust += 3 if 20 < R_Lust < 70 else 2
                $ TempFocus += 1 if P_Focus < 70 else 0            
            $ TempFocus += 5
               
    return                      #End Rogue_Offhand check
    


label Rogue_Offhand_Set(Situation = Situation, TempTrigger = Trigger2):
    if Situation == "shift focus":        
            if TempTrigger:   
                $ Trigger2 = 0
#               $ Situation = 0
                if TempTrigger == "fondle breasts":
                        "You shift your attention to her breasts."
                        jump RFB_Prep
                elif TempTrigger == "suck breasts":
                        "You shift your attention to her breasts."
                        jump RSB_Prep
                elif TempTrigger == "fondle pussy":
                        "You shift your attention to her pussy."
                        jump RFP_Prep
                elif TempTrigger == "lick pussy":
                        "You shift your attention to her pussy."
                        jump RLP_Prep
                elif TempTrigger == "fondle ass":
                        "You shift your attention to her ass."
                        jump RFA_Prep
                elif TempTrigger == "insert ass":
                        "You shift your attention to her ass."
                        jump RIA_Prep
                else: #If Trigger2 is "kiss you"
                        "You go back to kissing her deeply."
                        jump R_KissPrep                
            else: #if there's no Trigger2
                "You aren't doing anything else to shift to."     
            return
    # End "shift" situation    
        
    if Trigger:
        $ Situation = "auto"                 
        menu:  
            "Also kiss her." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    "You lean in and start kissing her."
                    $ Trigger2 = "kiss you"
                    
            "Also fondle her breasts." if Trigger in ("fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle breasts"
                    call R_Fondle_Breasts
                    
            "Also suck her breasts." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "suck breasts"
                    call R_Suck_Breasts
                    
            "Also fondle her pussy." if Trigger in ("fondle breasts","fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle pussy"
                    call R_Fondle_Pussy
                    
            "Also fondle her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle ass"
                    call R_Fondle_Ass
                    
            "Also finger her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "suck breasts", "lick pussy", "lick ass", "sex", "hotdog", "foot", "dildo pussy"):
                    $ Trigger2 = "insert ass"
                    call R_Insert_Ass
                    
            "Also jack it." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "dildo pussy", "dildo anal"):
                    call R_Jackin
                    
            "Nevermind":
                pass
    else: #if a Trigger is not found. . .
        "There's some kind of bug here, let Oni know." 
        
    $ Situation = 0
    return

    
# end Rogue_Offhand function ////////////////////////////////////////////////////////////////////////



label Rogue_ShameIndex:
    $ R_ShameLevel = 0
    
    if Trigger == "kiss you":
        $ R_ShameLevel += 2
        
    elif Trigger in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ R_ShameLevel += 6
        
    elif Trigger in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ R_ShameLevel += 10
        
    elif Trigger in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand", "blow", "titjob", "masturbation"):
        $ R_ShameLevel += 15
    
    elif Trigger in ("sex",  "anal"):
        $ R_ShameLevel += 20
    
    
    if not Trigger2:
        pass
    if Trigger2 == "kiss you":
        $ R_ShameLevel += 2
        
    elif Trigger2 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ R_ShameLevel += 6
        
    elif Trigger2 in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ R_ShameLevel += 10
        
    elif Trigger2 in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand"):
        $ R_ShameLevel += 15    
        
        
    if not Trigger3:
        pass
    elif Trigger3 == "kiss you":
        $ R_ShameLevel += 2
    elif Trigger3 == "kiss girl":
        $ R_ShameLevel += 3
    elif Trigger3 == "kiss both":
        $ R_ShameLevel += 4
        
    elif Trigger3 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ R_ShameLevel += 6
        
    elif Trigger3 in ("fondle pussy"):
        $ R_ShameLevel += 10
        
    elif Trigger3 in ("dildo pussy", "dildo anal", "hand"):
        $ R_ShameLevel += 15
    
    
    $ R_ShameLevel += R_Shame #adds clothing based shame
    
    return
    
    
    
label Quick_Taboo(Chr = "Rogue", Action = 0): #fix, add some quick taboo penalties here if someone sees you flirting. 
    return
    
label Rogue_Taboo(Cnt= 1):            
    $ Cnt = Action_Check("Rogue", "recent", "spotted") if "spotted" in R_RecentActions else 1
    $ Cnt = 4 if Cnt > 4 else Cnt   
    
    $ D20 = renpy.random.randint(1, 20)     
    if D20 < 10:    
        #if you're at the point where the girls would notice you. . .    
        if Taboo > 20:
            if (Trigger == "kiss you" and not Trigger2 and not Trigger3):
                pass
            elif "Rogue" not in Rules:
                #if Xavier is looking. . .
                call RogueFace("surprised", 1)
                if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                    "Rogue stops what she's doing with a startled look."                
                else:
                    "You feel a slight buzzing in your head and stop what you're doing."
                ch_x "Cease that behavior at once! Come to my office immediately!" 
                call AllReset("Rogue")
                $ renpy.pop_call()        
                $ renpy.pop_call()
                call Rogue_Caught
                return
            else:
                #if you've disabled Xavier's looking
                ch_x "Hmmm. . ."
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 2) 
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 3) 
        if bg_current == "bg classroom" and E_Loc == "bg teacher":
            #If you're in class and Emma's there as a teacher. . .
            call Emma_Teacher_Caught("Rogue")
        call Girls_Noticed("Rogue")
            
    if Taboo <= 20:
            #This is a private space with others around.
            call Girls_Noticed("Rogue")
            return
    elif Cnt < 4:                                                       
            #if this has happened less than 4 times within the current cycle of events
            if "spotted" not in R_RecentActions:
                "Some of the other students notice you and Rogue."
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 2)               
                $ R_Rep -= 2                      
                $ P_Rep -= 2                       
            elif Cnt < 3:
                "A few more students notice you and Rogue."   
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 2)               
                $ R_Rep -= 1                    
                $ P_Rep -= 1  
            elif Cnt == 3:
                "You've got quite an audience."               
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 2)               
                $ R_Rep -= 1                    
                $ P_Rep -= 1
                
            if "exhibitionist" in R_Traits:                
                    call RogueFace("sexy", 0)                     
                    if "spotted" not in R_RecentActions:
                        ch_r "Let'em watch, [R_Petname]."                          
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 3) 
                    $ Line = "A"
            elif ApprovalCheck("Rogue", 650, "I", TabM=Cnt):            
                    #not an exhibitionist but very uninhibited       
                    call RogueFace("sexy", 1)                    
                    $ R_Brows = "sad"                           
                    if "spotted" not in R_RecentActions:                        
                        ch_r "Hmm, what should we do about this, [R_Petname]?" 
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 3)   
                    $ Line = "B"
            elif ApprovalCheck("Rogue", 1000, "OI", TabM=Cnt):     
                    #not an exhibitionist but obedient/uninhibited          
                    call RogueFace("surprised", 2)
                    "Rogue looks a bit panicked."
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 3)
                    $ Line = "C"
            else:  
                    # She fails her inhibition checks
                    call RogueFace("surprised", 2)
                    if "spotted" not in R_RecentActions:    
                        "Rogue bolts up with an embarassed look. She runs off while putting her clothes back on."  
                        $ R_Rep -= 3 if R_Rep >= 30 else R_Rep            
                    else:
                        "With a sudden embarrassed start, Rogue panics. She takes off while throwing her clothes together."
                    "You head back to your room."                    
                    $ Line = "stop"
                
            if Line != "stop":
                menu:
                    "What would you like to do?"
                    "Let them watch. . ." if "spotted" not in R_RecentActions:   
                        if Line == "A":                
                                call RogueFace("sexy", 0) 
                                ch_r "That's what I'm talking about."             
                        elif Line == "B":            
                                #not an exhibitionist but very uninhibited       
                                call RogueFace("sexy", 1)
                                $ R_Brows = "sad"               
                                ch_r "Uh, ok."    
                        elif Line == "C":     
                                call RogueFace("sexy",2)
                                if R_Obed > R_Inbt:
                                    $ R_Eyes = "side"
                                    ch_r "If you say so, [R_Petname]."
                                else:          
                                    $ R_Mouth = "smile"
                                    $ R_Brows = "sad"
                                    ch_r "Uh, I guess. . ."                        
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 5)                       
                        "You get back to it." 
                        $ R_Blush = 1
                    "Continue" if "spotted" in R_RecentActions:
                        if Line == "C":          
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 3) 
                    "Ok, let's stop.":   
                        if Line == "A":                            
                                call RogueFace("sad")
                                ch_r "Spoilsport."                                         
                        elif Line == "B":            
                                call RogueFace("sad")
                                ch_r "Yeah, probably." 
                        elif Line == "C":     
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)          
                                call RogueFace("smile")
                                ch_r "Heh, thanks [R_Petname]" 
                        "You both run back to your rooms."
                        $ Line = "stop"
                        
            if Line == "stop":            
                    $ R_RecentActions.append("caught")
                    $ R_DailyActions.append("caught")         
                    show blackscreen onlayer black 
                    call AllReset("Rogue")
                    call Remove_Girl("Rogue")
                    call RogueOutfit
                    hide blackscreen onlayer black 
                    $ renpy.pop_call()          
                    $ renpy.pop_call()       
                    $ renpy.pop_call()                    
                    jump Player_Room             
    elif "exhibitionist" not in R_Traits:     
        call RogueFace("sly")   
        $ R_Traits.append("exhibitionist") 
        "Rogue seems to have become something of an exhibitionist."
    elif D20 > 15:
        call RogueFace("sexy")
        "The crowd cheers."
        
    $ R_RecentActions.append("spotted") if Cnt < 4 else R_RecentActions
    $ R_DailyActions.append("spotted")  if "spotted" not in R_DailyActions else R_DailyActions
    return
    
#End Rogue Taboo / caught  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label Rogue_Noticed(Other = "Kitty",Silent=0, B = 0):
    if Partner == "Rogue" and "noticed kitty" in R_RecentActions and Other == "Kitty":
            return
    if Partner == "Rogue" and "noticed emma" in R_RecentActions and Other == "Emma":
            return        
            
    if not Silent and Partner != "Rogue":
            call RogueFace("surprised", 1)
            "Rogue noticed what you and [Other] are up to."
        
    if Other == "Kitty":            
            $ R_RecentActions.append("noticed kitty")
            $ K_RecentActions.append("noticed rogue")
            if "poly kitty" in R_Traits:
                $ B = (1000-(20*Taboo))            
            else:
                $ B = (R_LikeKitty - 500)                  
                if "dating" in R_Traits:
                    $ B -= 200
    elif Other == "Emma":            
            $ R_RecentActions.append("noticed emma")
            $ E_RecentActions.append("noticed rogue")
            if "poly emma" in R_Traits:
                $ B = (1000-(20*Taboo))            
            else:
                $ B = (R_LikeEmma - 500)                  
                if "dating" in R_Traits:
                    $ B -= 200
    
    $ R_SpriteLoc = StageFarRight  
    call Display_Rogue(0,0) 
    if Partner == "Rogue":
            $ Silent = 1
    $ Partner = "Rogue"    
    $ Line = 0        
    if ApprovalCheck("Rogue", 2000, TabM=2, Bonus = B) or ApprovalCheck("Rogue", 950, "L", TabM=2, Bonus = (B/3)): 
            #if she's very loose or really likes you
            call RogueFace("sexy", 1)
            if not Silent:
                    "She decides to join you."                                      
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 5)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 5) 
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 3)  
            if Other == "Kitty" and "poly kitty" not in R_Traits: 
                    $ R_Traits.append("poly kitty")     
            elif Other == "Emma" and "poly emma" not in R_Traits: 
                    $ R_Traits.append("poly emma") 
            call Rogue_Threeway_Set(Mode="start",ActiveGirl=Other) 
    elif ApprovalCheck("Rogue", 650, "O", TabM=2) and ApprovalCheck("Rogue", 450, "L", TabM=1) or ApprovalCheck("Rogue", 800, "O", TabM=2, Bonus = (B/3)): 
            #if she likes you, but is very obedient
            call RogueFace("sexy")
            if not Silent:
                    "She sits down patiently off to the side and watches."          
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5) 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 5)  
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 2) 
            if Other == "Kitty" and "poly kitty" not in R_Traits: 
                    $ R_Traits.append("poly kitty")     
            elif Other == "Emma" and "poly emma" not in R_Traits: 
                    $ R_Traits.append("poly emma")   
            call Rogue_Threeway_Set("watch",Mode="start",ActiveGirl=Other)     
    elif ApprovalCheck("Rogue", 650, "I", TabM=2) and ApprovalCheck("Rogue", 450, "L", TabM=1) or ApprovalCheck("Rogue", 800, "I", TabM=2, Bonus = (B/3)):
            #if she likes you, but is very uninhibited
            call RogueFace("sexy")
            if not Silent:
                    "She sits down and watches you with a hungry look."             
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5) 
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 2)     
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
            if Other == "Kitty" and "poly kitty" not in R_Traits: 
                    $ R_Traits.append("poly kitty")     
            elif Other == "Emma" and "poly emma" not in R_Traits: 
                    $ R_Traits.append("poly emma")       
            call Rogue_Threeway_Set("watch",Mode="start",ActiveGirl=Other) 
    elif ApprovalCheck("Rogue", 1500, TabM=2, Bonus = B):
            call RogueFace("perplexed", 1)
            if not Silent:
                    "She looks a little confused at what's happening, but she stays put and watches."
            if R_Love >= R_Obed and R_Love >= R_Inbt:
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 2)                 
            elif R_Obed >= R_Inbt:
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 2) 
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 2)  
            else:
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 2) 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 1) 
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5) 
            call Rogue_Threeway_Set("watch",Mode="start",ActiveGirl=Other) 
    elif ApprovalCheck("Rogue", 650, "L", TabM=1) or ApprovalCheck("Rogue", 400, "O", TabM=2):
            #if she likes you or is obedient, but not enough
            call RogueFace("angry", 2)
            if bg_current == "bg rogue": 
                    "She looks betrayed, and kicks you both out of the room."
            else:
                    "She looks betrayed, and storms out of the room."                   
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5) 
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5) 
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5) 
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, -5)
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 89, 10)
            $ Partner = 0     
            if Other == "Kitty" and "saw with kitty" not in R_Traits: 
                    $ R_Traits.append("saw with kitty")   
            elif Other == "Emma" and "saw with emma" not in R_Traits: 
                    $ R_Traits.append("saw with emma")    
            if bg_current == "bg rogue": #Kicks you out if in Rogue's room
                    $ R_RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl("Rogue")
    else:
            #if she doesn't like you much
            call RogueFace("surprised", 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 2) 
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 40, 20)     
            if Trigger != "kiss you":
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -10) 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, -5)
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 10)                    
            if bg_current == "bg rogue":
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -5) 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, -5)
                    "She looks embarrassed, and shoves you both out of the room."                   
            elif Trigger != "kiss you":
                "She looks embarrassed, and bolts from the room." 
            else:
                "She looks a bit disgusted and walks away."   
            $ Partner = 0                   
            if bg_current == "bg rogue": #Kicks you out if in Rogue's room
                    $ R_RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl("Rogue")
    if Line:
        # This plays a line from a threesome action, if there is one. 
        "[Line]."
        $ Line = 0
    return    
#End Rogue Noticed by another girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /