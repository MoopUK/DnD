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
    # Write the character you defined in characters.rpy, and "what the character says" in speech marks
    bw "You've woke up after a"
    bw "...heavy..."
    bw "night of drinking"
    dm "(Like... real heavy... honestly we're suprised you aren't dead)"
    scene start
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

# - A QUESTION: These are how to make choices in Ren'Py.
# You can link them to different "Labels" with 'jump [label name]' on each separate answer OR just add one at the end
# if it doesn't change the scene too much. I've done 'jump plan' at the end of all three choices in this case as
# we're continuing the story like normal. The choice is what you're doing there first, rather than changing to different scenes.
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
                # scene sets the background image, in this case to a map (once I make and put in a map)
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
                passerby "You're here!"
                dm "The passerby marks your map"
                passerby"and here... Take this."
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
                dm "(You see the boat transport dock down the street and check your map to find out where you are)"
                scene mapstart
                dm "(That is QUITE the distance from home...)"
                bw "Oooh! A penny!"
                dm "(You found 20 gold on the floor, score!)"
                # Adds X-amount of money to coin purse
                $ coinsLeft += 20
                dm "(You'll need 50 gold to get home.)"
                # [coinsleft] displays the number of current coinsleft
                dm "(you have [coinsLeft] gold)"

    jump plan
label plan:
# plan consists of:
# - killing creatures in the area, but they're already claimed by these cool adventurers
# in a cool party, fuck, why do you never get to be in a cool party?

# - the casino, suggested to you by an old man, what could go wrong?
# snail races are at casino are how you get your coin

# - Lemonade stand: Someone asked for grapes, you make a huge fuss over how stupid
# it would be to make a drink out of grapes, break your lemonade stand in the
# process and take your earnings to the casino to destress
# Money making options (kill monsters, lemonade stand, casino)

# QUESTION:
    "How are you earning enough gold to get home?"
    menu:
        "Reward posters for monsters in the area":
            scene wanted
            dm "(You go to the wanted posters in the nearby tavern)"
            dm "(You shiver at the thought of a spider pidgeon hybrid)"
            dm "(But it pays 100g each!)"
            dm "(You hear cheers and screams of delight outside and take a look...)"
            scene outside
            dm "(They've already been killed and the rewards claimed by some cool adventurers
             in a cool party)"
            bw "why do you never get to be in a cool party?"
            dm "(They're so cool they somehow killed every Spidpigeon, slime, and blood foxes in existance!)"
            dm "(This depresses you immensely, and you decide on going to the
            casino to destress and maybe win enough to get home)"
            dm "(What is more relaxing than over stimulation of flashing lights and noises?)"

        "A Lemonade Stand":
            dm "(You find some bark on the side of the road and make up a sign for a lemonade stand)"
            dm "(Finding a lemon tree and conveniently a pitcher right next to it, you make lemonade and try to sell it make
            up the money needed to get home)"
            dm "(At one point a humanoid-mouse was screaming something at you about the differences between lemons and lemon juice)"
            dm "(But a humanoid-racoon dragged her away from you apologising profusely)"
            $ coinsLeft += 20
            $ timeLeft -= 10
            dm "(Ten hours have passed, you've made 20 gold)"
            dm "(and then someone asks you for grapes...)"
            dm "(You make a huge fuss over how stupid it would be to make a
            drink out of grapes!)"
            dm "(You break your lemonade stand in the process and can no longer continue selling lemonade.)"
            $ timeLeft -= 5
            dm "(After 5 hours of raging, you decide to take your earnings to the casino to destress and get the rest of the money needed to get home)"

        "Casino":
            scene outside
            dm "(You overhear how easy it is to win on the snail races in the casino...)"
            dm "(Gambling is the easiest way to make money, right?)"
            bw "Gambling is a terrible way to make money!"
            you "Shut up brain worm, you just want me to miss my little Timmy's lute recital!"
            bw "Why would I want that? I told you about the recital in the first place!"
            dm "(You ignore the brain worm and head to the casino)"

    jump dice_rolling

label dice_rolling:
    # WIP Casino background
    scene casino
    # Dice roll - Random number generator between 1 and 20, to signify a D20 dice.
    # Using random function to do a very simple 1 - 20 dice roll
    $ import random
    # You want a random interger between 1 and 20
    $ roll = random.randint(1, 20)

    "(You go to the snail races at some part of this endevor for coin so you can get home)"
    "(You pay 10 gold to play)"
    $ coinsLeft -= 10
    "Roll for luck!"
    "You rolled [roll] on a d20!"
    if roll == 20:
        scene casinorace5
        dm "(The second the gun goes off the snail is already at the finish line)"
        dm "(Nobody knows what happened. It was just there! Done! First place!)"
        dm "(Pete from the SnailWorld Records was also present and watching the match)"
        pete "New world record!"
        dm "(The snail is proud of itself)"
        you "What was the time?"
        dm "(Pete looks at you)"
        pete "To hell if I know! But nobody is ever going to beat it!"
        dm "(Pete is a *little* inebriated and won't even remember seeing this race in the morning)"
        dm "(Which is a shame too, he loves snails so much and this was the greatest snail race of all time)"
        dm "(Oh well, let's move on)"
        dm "(You win, 50 gold!)"
        $ coinsLeft += 50

    elif roll >= 19:
        scene casinorace1
        dm "(The snail looks amped up)"
        dm "(Stretching it's little... snail legs... tail...?)"
        dm "(Whatever snails have!)"
        dm "(It stands by the starting line)"
        dm "(As the gun goes off it ZOOMS straight to the front of the line!)"
        scene casinorace6
        dm "(The other snails snailing them in comparison!)"
        dm "(You can't believe it! Nobody can believe it! It's almost like the snail is on a battery powered Tech Deck!)"
        dm "(Whatever one of those are!)"
        dm "(And it gets 1st place before the smoke has even left the gun)"
        dm "(Winning you 40 gold!)"
        $ coinsLeft += 40

    elif roll >= 15:
        scene casinorace1
        dm "(The gun goes off and the snails are amped up!)"
        scene casinorace2
        dm "(Your snail isn't that much faster than the others...)"
        dm "(But they're just fast enough to be near to the front of the line)"
        scene casinorace3
        dm "(Getting you 2nd place)"
        scene casinorace4
        dm "(Winning you 30 gold)"
        $ coinsLeft += 30

    elif roll >= 9:
        scene casinorace1
        dm "(Your snail has just enough strength not to complete fumble the entire race)"
        dm "(Unfortunately though, it is not strong enough to win...)"
        dm "(You got into 3rd place)"
        dm "(Winning no gold, but you were given a 'One Free Try' token as a runner up prize)"
        dm "(It literally adds 10 gold to your bag again)"
        dm "(So at least it didn't cost you anything...)"
        $ coinsLeft += 10

    elif roll >= 2:
        scene casinorace1
        dm "(The snail looks hopeful, but as the gun goes off to start the race)"
        # Playing an audio sound in game you've put into audio folder
        play sound "audio/Snailcramp.mp3"
        dm "(Ohhh that's not a good sound)"
        scene sadsnailcasino
        dm "(The crowd gasps... someone even throws up at the sight...)"
        dm "(The snail got snail cramp.)"
        dm "(The poor thing winces and cries out in pain)"
        dm "(As the priority for the medical world's knowledge of snail
        treatment isn't anywhere near the top of the list)"
        dm "(A casino bouncer takes the snail out back and shoots it with a shotgun to put it out of it's misery)"
        scene casinorace7
        dm "(The other snails glare at you like they know this is your fault for a bad roll)"
        dm "(They have also learned to try to keep their very common ailment of snail cramp to themselves from now on)"
        dm "(Else they meet the same fate.)"
        dm "(You won no gold.)"

    elif roll == 1:
        scene angrysnailone
        dm "(The snail looks at you, dead in the eyes.)"
        dm "(It knows how terribly you've just rolled.)"
        dm "(You're going to make it look bad! At the races of all places!)"
        scene angrysnailonetwo
        dm "(This is it's place of work you idiot!)"
        scene angrysnailone
        dm "(If this snail had hands, it'd be throwing them.)"
        scene casinorace1
        dm "(To spite you, when the gun goes off to start the race,)"
        dm "(It slithers backwards as fast as it can until it falls off the table)"
        dm "(Coming not only in last place, but technically not even starting the race in the first palce)"
        dm "(Disqualifying you and everyone else that bet on it.)"
        dm "(Everyone else who bet on Ol' Slimey glare at you)"
        dm "(You should probably watch your back when you leave later)"
        dm "(You will have to pick another snail for the next race)"
        dm "(And pay an extra 10 gold penalty from the racing fee, to stop a riot breaking out)"
        dm "(Losing you 20 gold.)"
        $ coinsLeft -= 20

# If run out of money you get auto game over, if max out coins auto game win end
# No coin ending (nocoinleft)
if coinsLeft <= 0:
    jump nocoinleft
# Maxxed out coin ending (allthecoin)
elif coinsLeft >= 100:
    jump allthecoin

# This is asking player/you if you want to continue snail racing, even if you have enough coins to end it.
# The limitation of "There is no end." is working here as a psychological thing, as you've won the game and
# you could go home and be on time for Little Timmy's lute recital but.... You could roll a d20 next? What happens when
# you win big, eyyyyy? lol
# QUESTION:
$ timeLeft -= 5
dm "(you have [timeLeft] hours left until Little Timmy's lute recital and [coinsLeft] gold.)"
dm "(It takes 12 hours to travel by boat, and you only need 50 gold for the ticket)"
bw "Soooo.... Do you want to bet on another race? :)"
bw "You don't have to stop, you could just keep going, what if you win the JACKPOT?!"
menu:
    "Just one more race! I don't want it to end!":
        jump dice_rolling
    "No, I think I have enough to go home and don't want to risk losing it all":
        jump endings

# Game endings
label endings:
    if coinsLeft >= 50:
        jump win
    elif coinsLeft <=40:
        jump lose

label win:
    "winner"
    "(For legal reasons this game is a joke, please don't gamble on snail races,
    or on any races, but if you REALLY have to at least gamble responsibily)"
    return

label lose:
    "lose"
    "(For legal reasons this game is a joke, please don't gamble on snail races,
    or on any races, but if you REALLY have to at least gamble responsibily)"
    return

label nocoinleft:
    dm "(You have ran out of coin at the snail races...)"
    dm "(And so, you missed little timmy's lute recital)"
    dm "(The divorce mages take your fields)"

    "(For legal reasons this game is a joke, please don't gamble on snail races,
    or on any races, but if you REALLY have to at least gamble responsibily)"
    return

label allthecoin:
    dm "(You don't need to gamble anymore)"
    dm "(You've maxed out the coins!)"
    dm "(Not only do you get the boat back to little Timmy's recital on time,)"
    dm "(you also buy your partner a beautiful gold encrusted snail ornament fron the casino gift shop)"
    dm "(For some reason, they LOVE it! And show all of their confused friends)"
    dm "(Little Timmy loves you too. And plays the lute like a pro.)"
    lt "When I grow up, I'm going to be a gambler just like you!"
    dm "(You've never been so proud.)"
    "(For legal reasons this game is a joke, please don't gamble on snail races,
    or on any races, but if you REALLY have to at least gamble responsibily)"
    return

# This ends the game.
    return
