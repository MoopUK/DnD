# Script for any characters

#-----------------------------------------------------
################# Character List ####################

# You define your characters with this line of code (as seen used below):
# define [character in script.rpy] = Character("[Character name]", color="[HEX Colour you want character name tag to be in]"
#-----------------------------------------------------

# Dungeon Master
define dm = Character("DM")

# Narrator / The Game Developer - a fairy brain worm from the whiskey you drank
define bw = Character("Brain worm", color="#FBC3A7") # Dark peach colour name tag

# Player / You
define you = Character("Player", color="#77878f") # Slate Grey colour name tag

# Your son Little Timmy
define lt = Character("Little Timmy", color="#00fa9a") # Spring Green colour name tag

# Passerby
define passerby = Character("A passerby", color="#cf3476") #Telemangenta colour name tag

# Pete (The Snail World Record enthusiast)
define pete = Character("Pete", color="E2C787") # Snail shell colour name tag

#-----------------------------------------------------
################# Character Images ####################
# Any character you want to show on screen you define the images like so:
# image [image name you write in script.rpy to show said image]:
#   "[image name in your files]" (eg: for images/playerHappy.png it would be "playerHappy")
#    zoom 0.5 (if you need to resize an image you can "zoom")


# General expressions I use for character's facial expressions in all games:
# - neutral face
# - sad/crying
# - happy
# - angry
# - confused
# - embarrassed/shy
#------------------------------------------------------

# Currently have no images made but this is the generic template for a character I always
# copy/paste from previous games and edit accordingly once I start adding images

# player (Player)
image player n:
    "playern"
    zoom 0.5
image player sad:
    "playersad"
    zoom 0.5
image player happy:
    "playerhappy"
    zoom 0.5
image player angry:
    "playerangry"
    zoom 0.5
image player confused:
    "playerconfused"
    zoom 0.5
image player shy:
    "playershy"
    zoom 0.5
