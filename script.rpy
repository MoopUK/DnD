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

# The game starts here.
label start:
# Waking up and needing money
    dm "You wake up after a heavy night of drinking..."
    dm "Starting timer..."
    show screen timeLeft
    $ timeLeft = 72
    dm "... and coin purse for debug"
    show screen coinsLeft
    $ coinsLeft = 0
    dm "Minus 30 hours and plus 30 coins for debug"
    $ timeLeft -= 30
    $ coinsLeft += 30
    dm "success/debugging"
    dm "Now working as expected :D"
    $ coinsLeft -= 20
    dm "hehe... coins go down"
    dm "Also working as expected"

# Money making options (kill monsters, lemonade stand, casino)


# Casino


# Endings

    # This ends the game.
    return
