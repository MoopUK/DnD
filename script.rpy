# The script of the game goes in this file.

###############################################################################
######################## Initial Game Idea Draft ##############################
###############################################################################

# Base game premise:
    # - DND with Player needing money to get to somewhere to not miss an event...

    # - Your Little Timmy's first lute recital is why you need to go home lol idk

    # - You wake up after a HEAVY night of drinking, are infected with a brain worm, and
    # your coin purse is empty so you need to make money to get home within 72 hours.

    # - The best way to get cash is the snail races at the casino.
    # - This is because:
    #   - All monsters in the area have already been killed, and their rewards collected by another party
    #   - Your Lemonade stand would have worked but you get angry and break the lemonade stand

# Casino info:
    # - Each turn in the snail races at the casino will take [undecided]-hours of your time,
    # You really need to get home asap!

    # - It'll take 12 hours to get home? So Player needs to keep in mind 12 hours is needed spare to win.

    # - It will cost 50 gold to get home? And the coin purse will hold 100 coins maximum.
    # (Maybe the Casino will kick you out when you earn your maximum? And you go home as nothing else to do)

# Game Jam Limitation 'There is no end':
    # - There is no end - If you sucumb to the gambling addiction you could gamble to no end.
    # Rather than a game that is ongoing forever, this will technically have *endings*, but
    # it'll be a symbolic gambling addiction neverending situation at the *endings* of the game if you
    # don't walk away once you make enough to get home (50 gold minimum)


###############################################################################
############# 72 HOUR TIMER CODE && COIN PURSE COUNTER CODE ###################
###############################################################################
# The Coin Counter
# - Location of coin counter on the game screen, images used for coin counter, and
# the coin amount raising or falling
screen coinsLeft():
    zorder 100
    vbar value AnimatedValue(coinsLeft, maxCoin, delay=1.0):
        xalign 0.988 yalign 0.008
        xmaximum 47
        ymaximum 327
        left_bar Frame("images/statusBars/coinEmpty.png", 100, 10)
        right_bar Frame("images/statusBars/coinFull.png", 100, 10)
        thumb "images/statusBars/coinThumb.png"
        thumb_offset 30
    imagebutton idle "images/statusBars/coinText.png" xalign 1.00 yalign 0.06 xmaximum 47 ymaximum 327 action NullAction()
# Starting coins (0), and max allowed coins (100)
default coinsLeft = 0
default maxCoin = 100
#-------------------------------------------------------------------------------
# The Time Remaining Counter
# Location of timer on the game screen, images used for timer falling/counting down
screen timeLeft():
    zorder 100
    vbar value AnimatedValue(timeLeft, maxTime, delay=1.0):
        xalign 0.001 yalign 0.001
        xmaximum 47
        ymaximum 327
        left_bar Frame("images/statusBars/timeLeftEmpty.png", 1, 10)
        right_bar Frame("images/statusBars/timeLeftFull.png", 1, 10)
        thumb "images/statusBars/timeLeftThumb.png"
        thumb_offset 30
    imagebutton idle "images/statusBars/timeLeftText.png" xalign 0.02 yalign 0.06 xmaximum 47 ymaximum 327 action NullAction()
# The time start (1) and maximum time (72 hours to get to the lute recital)
default timeLeft = 1
default maxTime = 72

################################################################################
######################### GAME SCENE START #####################################
################################################################################

# The game starts here.
label start:
    bw "You've woke up after a"
    bw "...heavy..."
    bw "night of drinking"
    dm "(Like... real heavy... honestly we're suprised you aren't dead)"
    you "Who is TALKING in my head!?!"
    bw "Your newest friend, Brain Worm! I was hybernating in that whiskey you drank"
    bw "Don't worry, I won't eat all of your brain, I have a very low metabolism"
    you "I'd rather not have a brain worm in my head at all to be honest"
    bw "Don't worry about it new best friend.... oh yeah!"
    bw "You need to go!"
    bw "Your partner sent word via crow post and.... oh god... OH GOD!!!"
    bw "It's Little Timmy's lute recital in 72 hours!"
# Shows the timer on the left of the game screen
    show screen timeLeft
# Telling game how much time is left initially
    $ timeLeft = 72
    bw "If you miss this your partner will call the divorce mages"
    bw "And the divorce mages are going to have a field day..."
    bw "And they're gonna have your fields!"
    bw "F'kin divorce mages!"
    bw "F***!!!"
    you "How many times have you been divorced?"
    dm "Don't worry about i..."
    bw "I mean don't worry about it! YOU NEED TO GET BACK HOME FAST!"
    bw "GOTTA GO FAST!"
    "(72 Hours Remaining)"

# QUESTION:
    dm "What do you do first?"
    menu:
        "Check my coin purse":
            # Shows the coin purse top right of the game screen
                show screen coinsLeft
                dm "(You check your bag of holding and/or where you keep you coin)"
                dm "(I don't know where you keep it, I'm not a cop.)"
                dm "(But the coin purse and/or bag of holding is barren of coin)"
                bw "Yeah... about that..."
                dm "(You glare at the brain worm)"
                bw "I mean, you drank a LOT last night and they sold this fancy bottle..."
                bw "Came out on a little boat with some bar people cheering..."
                bw "You err... liked it so much you paid for that experience at least 12 times"
                bw "even I lost count"
                dm "(You see Rusty Richard's dive bar down the street and check your map to find out where you are)"
                scene mapstart
                dm "(It is quite a distance...)"
                bw "Ooooh! A penny!"
                dm "(You find 20 gold on the floor, score!)"
                # Adds X-amount of money to coin purse
                $ coinsLeft += 20
                dm "(You'll need 50 gold to get home.)"
                # [coinsleft] displays the number of current coinsleft
                dm "(you have [coinsLeft] gold)"

        "Ask a passerby where I am":
                dm "(You ask a passerby where you are)"
                passerby "I'd remember for some coin..."
                dm "(You check your bag of holding for your coin purse and see that it is barren of coin)"
            # Shows the coin purse top right of the game screen
                show screen coinsLeft
                bw "Yeah... about that..."
                dm "(You glare at the brain worm)"
                bw "I mean, you drank a LOT last night and they sold this fancy bottle..."
                bw "Came out on a little boat with some bar people cheering..."
                bw "You err... liked it so much you paid for that experience at least 12 times"
                bw "even I lost count"
                dm "(The passerby looks at you with pity)"
                passerby "Brain worms huh? My uncle had those after drinking in Rusty Richards dive bar"
                passerby "You're in LOCATION, and here..."
                # Adds X-amount of money to coin purse
                $ coinsLeft += 20
                passerby "Hope that helps you get something to eat"
                dm "(You thank the passerby and check your map)"
                scene mapstart
                dm "(You'll need 50 gold to get home.)"
                # [coinsleft] displays the number of current coinsleft
                dm "(you have [coinsLeft] gold)"

        "Check my bag of holding to see if there's ANYTHING to get rid of my hangover":
                dm "(There is not.)"
            # Shows the coin purse top right of the game screen
                show screen coinsLeft
                dm "(You also notice a lack of coin in your posession)"
                bw "Yeah... about that..."
                dm "(You glare at the brain worm)"
                bw "I mean, you drank a LOT last night and they sold this fancy bottle..."
                bw "Came out on a little boat with some bar people cheering..."
                bw "You err... liked it so much you paid for that experience at least 12 times"
                bw "even I lost count"
                dm "(You see Rusty Richard's dive bar down the street and check your map to find out where you are)"
                scene mapstart
                dm "(It is quite a distance...)"
                bw "Oooh! A penny!"
                dm "(You found 20 gold on the floor, score!)"
                # Adds X-amount of money to coin purse
                $ coinsLeft += 20
                dm "(You'll need 50 gold to get home.)"
                # [coinsleft] displays the number of current coinsleft
                dm "(you have [coinsLeft] gold)"

    jump plan
label plan:
    "how to get home"
# plan consists of:
# - killing creatures in the area, but they're already claimed by these cool adventurers
# in a cool party, fuck, why do you never get to be in a cool party?

# - the casino, suggested to you by an old man, what could go wrong?
# snail races are at casino are how you get your coin

# - Lemonade stand: asked for grapes, you make a huge fuss over how stupid
# it would be to make a drink out of grapes, break your lemonade stand in the
# process and take your earnings to the casino to destress
# Money making options (kill monsters, lemonade stand, casino)


# Casino


# Endings

    # This ends the game.
    return
