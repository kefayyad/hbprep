# Kristina Fayyad 9/14/2019
# Hackbright Prep 9/3/2019-10/3/2019
#
# MastermindGame, course project
#

# Status:
#   9/22 starting code
#   9/19/2019 3:20pm, not sure if all pseudo code,
#   9/24/2019 game works but needs additions
#           see code for details
#   9/25 - added checks for valid user code
#           and now hidden code is randomly generated
#   9/26 - continue to allow peg set to be
#           selected emojis see PEG_BULLETS
#           and figure out how to get UserWarning
#           to input emojis in repl.it terminal
#   9/26 should allow user to quit with "q" when
#       asked to enter code
#   9/26 emoticons worked in terminal!! repl.it was the problem
#   9/26 also to do - ask user color pegs or letters
#       then set peg_set
#   9/26 NEED to get a different yellow peg - done Lemon
#   
#   SHOULD clean up some code, especially in checking user code
#   DONE,  PRINT a nicer board - done

#   DONE,  SHOULD save hidden_str - recreated too many times! 

#   Cleaned up some code and put into small functions, 

# Allow user to enter "q" if they want to quit, instead of user code
# since guessing 12 times can be tiring!
# USE copy paste for now to quickly enter codes

# ***************
# PROJECT Presentation ideas - 4 minutes!
# run in terminal so I can demo with colored pegs/emojis

# NOTE: that hidden code IS shown for test and demos, because
# the Mastermind is a slow game from the user's side. It takes
# time to logically come up with guesses.

# Explain game clearly - so RUN and show with two guesses
#
#           Ask someone to give me a code, colors/emojis are OK
#
# play it two times, explain the code checks on the board

# explain the main function:
# SO NEED TO BE ABLE TO SEE THIS OR HAVE IT AS A PDF
# 
# IF TIME DEMO:
# Some things I can handle?
#
# user code -  too short
#
# user code - invalid peg
#
#               These invalid guesses to not count against user
#
# User can only take 12 guesses, then game is over
#
#  Keep track of shortest game for the user, taking the fewest
# number of guesses to find the hidden code
#
# 
#
#
# 



# Initial idea notes:
#
# slower game to play, because user needs to think!
# Computer picks a code, hidden_code
# While True
#   User is prompted for a code
#   Check the code
#   display the code check, and user code
#   if code matches hidden code
#       tell user they FOUND the code!
#       break
#   End of game
#
#
# Enhancements for later
# User picks 4 or 5 code length
# Use colored emojis
# Or ask user if color blind and use letters
# instead

# **********  Some of my early thinking
# hidden_code
# try_code # what the user chose
# colors_right # a list
# positions_colors_right # a list
# usually print entire board each time.
# print guesses in order first
# which is OPPOSITE to how board game
# displays
#
# use list for codes, they have order
# make sure user inputs a proper code
# with available colors and code length
# is as setup at start of game
# user input MUST be checked!
#
# board printed could be like this
# for a single line:
# ooox G B R Y
# o is color right, x is position right,
# but no position is specified by the o,x
# and NOTHING right is "----"
# *********** End of early thinking
#
#
# Pseudocode
#
# set max_guesses = 12 # max times user can guess,
#                       # with a valid guess
# set user_guesses = 0
# set success = False
# While (user_guesses <= max_guesses) And (Not success)
#   Prompt user for a code
#   Check the code
#   print the board - yes, all lines in the board
#
#   if code matches hidden code
#       tell user they FOUND the code!!
#       set success = True
#
#   End of game
#
#
#

# code starts here

# to get for loop to iterate over multiple lists
# use zip
import itertools

# for the colored pegs used for hidden and user codes
# I didn't need this to display or to enter emoticons
# from keyboard
# import emoji

# for generating hidden code
import random

def get_user_name():
    """ Prompt user for name, greet, and
    return user name """

    print()
    a_user_name = (input("What is your name? ")).title()

    return(a_user_name)


def welcome_and_how_to_play(a_name, a_instructions):
    """ welcome user and print instructions """

    print()
    print("Welcome to Mastermind, {}!".format(a_name))
    print()
    print("This is how to play the game:")
    print(a_instructions)

    # get the code length to be used in game

def get_code_length():
    """ #MVP set to 5 LATER prompt user for length of code 3, 4, 5 
    and returns code length """

    #MVP set to 5, as in board game
    a_code_length = 5
    return(a_code_length)



def make_hidden_code(a_code_length, a_peg_set):
    """ Create random hidden code from set of peg colors, 
    code length and return a list of code as a list and  as a string"""

    # A CODE is a list of 5 characters MVP
    # the colors of the rainbow:  ROY G BIV
    # This should use ["R", "O", "Y", "G", "B", "I", "V"]
    # MVP display it, for testing

    # Normal game: DON'T display hidden_code !

    # early MVP, fix hidden_code
    #    a_code_str = "RBGYI"
    # later MVP testing! ask user for hidden_code,
    # need to have good complete set of test cases
    # to test edge cases

    # print()
    # a_code_str = (input("Enter hidden code for testing: ")).upper()
    # a_code_list = list(a_code_str)


    # randomly generate code of length a_code_length
    # from items in a_peg_set


        # make a code list of length given
        # create one random peg at a time
    idx = 0                 # initialize index in code list
    a_code_list = []     # initialize code list
    while idx < a_code_length:

        a_code_list.append(random.choice(a_peg_set))
        idx += 1

    # create the string version of the hidden code, from the list
    a_code_str = " "
    a_space = " "
    a_code_str = a_space.join(a_code_list)


    print()
    print("Still testing/demoing, so... show the")
    print("randomly generated hidden code")

    print(a_code_str)

    return(a_code_list, a_code_str)



# Function to prompt user for a code
# with peg set given, code length 

def get_user_code(a_code_length, a_peg_set):
    """ ask user for code from set of peg colors
    and return their code as a list"""

    # A CODE will be a list of 5 characters MVP
    # the colors of the rainbow:  ROY G BIV
    # This should use ["R", "O", "Y", "G", "B", "I", "V"]
    # No duplicates allowed at first - OK, logic DOES
    # handle duplicates

    # THIS DOES NOT handle user deleting characters 
    # while entering code

    #     # MVP, fix user_code
    # a_code = ["Y", "B", "O", "V", "I"]

    # Seeems like a lot of logic for check user_code

    # loop to get valid code from user
    valid_code = False      # intialize to NO valid code to start

    while not valid_code:

        # earlier MVP simple, don't check for valid code

        print()
        if a_peg_set == PEG_LETTERS:

            print("Code, no spaces/upper/lower ok, e.g.roygb")

        # THIS works even with emoji pegs, but should add condition
        # to only do .upper on letter pegs
        a_code_str = (input("Enter code:")).upper()
 #       print("User code is: ", a_code_str)

        # if code length OK
        if len(a_code_str) == a_code_length:

            # iterate over string
            # until string is valid code NEED BETTER COMMENT HERE

            idx = 0
            while (idx < a_code_length):
                # print("peg: ", a_code_str[idx])

                if a_code_str[idx] not in a_peg_set:
                    print("invalid peg: ", a_code_str[idx])
                    break

                    # peg ok, move to next one
                else:
                    idx += 1    # increment index

            # all pegs ok if idx max value
            if idx == a_code_length:

            # now we have a valid code
                # print("user code is ok")
                valid_code = True

        else:
            print("Code wrong length")

    # create code as a list from string
    a_code_list = list(a_code_str)

    #print("code as list: ", a_code_list)
    return(a_code_list)





# Function to check if code matches hidden_code
# This is the FUN STUFF!

# long function, can I add small functions from within?
# Yes, see notes below for some for loops
def check_code(a_code, a_hidden_code):

    """ Check if a_code matches hidden_code
    and return a list of checks and success_flag """

    success_flag = False

    # THIS assumes code length 5!!
    success_checks = "xxxxx"  #NEED To handle code length!


    color_checks =  ""   # color OK o's
    pos_checks = ""        # position+color OK x's

    # ASSUMES code length 5!
    no_checks = "-----"     # init, assume all pegs NOT OK

    # later concatenate above check strings; return it
    #
    # MVP a_code and hidden_code are simple strings
    # assume each is 5 characters long
    # don't check for acceptable codes for MVP
    #

    # to handle multiple peg colors,
    # the search can be:
    # must make a COPY of list;
    # NOTE: use of "= just points to same list object in memory

    left_pegs = a_hidden_code.copy()

    # *******
    # NOTES on OLD WAY NOT GOOD loop over pegs in a_code and a_hidden_code
    # ADD comments on logic
    # THIS DOES NOT handle case where
    # H gbbbb
    # U bbbbb
    # because first peg removes a "b" from left_pegs
    # which messes up logic when there is a peg
    # match the last time!
    # *********

    # This way works:
    # Prioritize peg position matches, when managing left_pegs.
    # Take care of peg matches first! with a loop
    # Then look for color matches with a loop

    # print()
    # print("H code: {}".format(a_hidden_code))
    # print("U code: {}".format(a_code))
    # print()


    # this for loop SHOULD BE a function , maybe find_peg_matches
    # loop over codes, look for peg matches only
    for (a_peg, h_peg) in zip(a_code, a_hidden_code):

        # print()
        # print("u peg: {}  h_peg: {}".format(a_peg, h_peg))
        #print("hidden code: ", a_hidden_code)

        if a_peg == h_peg:      # peg match!

            # print()
            # print("peg match: ", a_peg, h_peg)

            # remove h_peg from list left_pegs

            left_pegs.remove(a_peg)
        #    print("after remove, left_pegs: ", left_pegs)

            # append x to pos_checks, since a peg matches
            pos_checks = "{}{}".format(pos_checks, "x")

            # remove 1 "-" from no_checks, to account for
            # a peg match
            no_checks = no_checks[1:]

    # print()
    # print("after peg matches:")
    # print("pos_checks: ", pos_checks)
    # print("left_pegs: ", left_pegs)

    # COULD check pos_checks and set success
    # and avoid next for loop


    # this for loop SHOULD be a function, maybe find_color_matches
    # loop over codes look for color match
    # DON'T need to do this if code matches!
    for (a_peg, h_peg) in zip(a_code, a_hidden_code):

        if a_peg == h_peg:  # don't do anything
                            # peg matches handled above
            pass   # is there better logic than
                    # doing this?

        elif a_peg in left_pegs:    # color match only

            # print()
            # print("color match: {} left pegs: {}".format(a_peg, left_pegs))

            # remove h_peg from list left_pegs
            left_pegs.remove(a_peg)
            # print("after remove, left_pegs: ", left_pegs)

            # append o to color_checks
            color_checks = "{}{}".format(color_checks, "o")

            # remove 1 "-" from no_checks
            no_checks = no_checks[1:]

        else:   # no peg match
                # do I need this else?
            pass
            # print()
            # print(" no peg/color match ", a_peg, h_peg)
              # don't touch no_checks; it was initialized
            # to assume no matches

    if pos_checks == success_checks:  # all pegs good!

        # not such a good print statement, but
        # print("hidden: ", a_hidden_code)
        # print("code:   ", a_code)
        # print("checks: ", pos_checks)
        # print()
        # print("code matches!")

        success_flag = True                     # set flag to show user guessed code

                    # create the string of code checks for guess just checked
    checks = "{}{}{}".format(no_checks, color_checks, pos_checks)

    # print("checks: ", checks)
                                # return the checks string and flag if user found code
    return([checks, success_flag])




def print_nice_board(a_guesses, a_checks):
    """ Print a nice board, all guesses and checks so far 
    with some borders and guess number"""

    top_lower_border = "------------------------------"

    guess_num = 0       # init guess num

    print()

    print("Your game so far: ")

    print(top_lower_border)

    # iterate over multiple lists, the guesses and checks, to print each line
    for (a_guess, a_check) in zip(a_guesses, a_checks):


        guess_num += 1          # increment guess_num

        # print list of chars as string with spaces
        # USE JOIN as I did for hidden code
        guess_str = ""
        a_space = " "
        guess_str = a_space.join(a_guess)
        #print(guess_str)

        # there must be a nicer and cleaner way - YES see join above
        # guess_str = ""
        # for a_peg in a_guess:
        #     guess_str = "{} {}".format(guess_str, a_peg)

        # print each line in board, handling double digit guess num, which is longer
        # should be nicer way
        print()
        if guess_num < 10:          # single digit guess has 1 more space after guess num
            print("| {}   {}  {}  |".format(guess_num, guess_str, a_check))
        else:                                   # double digit guess_num
            print("| {}  {}  {}  |".format(guess_num, guess_str, a_check))


    print(top_lower_border)




    # a_guesses a_checks are lists of the
    # current checks/guesses in the game so far
def print_board(a_guesses, a_checks):
    """ Print all guesses and checks so far, no borders """

    print()
    print("Your game so far: ")

    for (a_guess, a_check) in zip(a_guesses, a_checks):

        # there must be a nicer and cleaner way
        # to print list of chars as string with spaces
        guess_str = ""
        for a_peg in a_guess:
            guess_str = "{} {}".format(guess_str, a_peg)

        print()
        print("{}  {}".format(guess_str, a_check))



def print_peg_set(a_peg_set):
    """ Show the user what pegs they can use , a_peg_set is a list"""

    a_double_space = "  "
    print("You can use these pegs for your code:")
    print(a_double_space.join(a_peg_set))





def tell_guesses_in_game(a_min_user_guesses, a_user_guesses):
    """  After a game, if they solved it, 
    tell user about their guesses for this game  """

                                            # something isn't quite right here, think!
    if a_min_user_guesses >  0:             # they have guessed it at least one time
            print()
            if a_min_user_guesses == 1:           # DON'T address user again, seems odd
                print("You solved it in {} guess!".format(a_user_guesses)) #for grammar, singular
            else:
                print("You solved it in {} guesses!".format(a_user_guesses))




def tell_user_best_game(a_user_name, a_min_user_guesses):
    """  When the user is all done playing. If user solved it at least once, 
    tell them their best game. """

    if a_min_user_guesses >  0:           # user solved it at least once
                                          # if min_user_guesses = 0, they never solved it

        print()
                    # handle singular/plural on "guesses"
        if a_min_user_guesses == 1:
            print("{}, your best game was {} guess!".format(a_user_name, a_min_user_guesses))
        else:
            print("{}, your best game was {} guesses!".format(a_user_name, a_min_user_guesses))



# Start with variable code_length fixed, for MVP.
# SET code length to 5
# Enhancement: ask user for choice of code length, 3-5
#
# Use a list to represent code. Use
# peg_colors is a list of the characters representing
# the colors of the rainbow:  ROY G BIV
# Enhancement: use emoji's with those colors or just
# colored dots
#
# randomly set hidden_code, from available peg_colors
#
# DON'T display hidden_code !

# prompt user to guess code,
# which is a sequence of 4
# letters, one for each color.
# Require that code only has valid colors letters -
# so need to check that user code is valid.
#
# I made the logic handle multiple colors
# Does it matter now if duplicate colors are allowed?
# Or are duplicate colors an enhancement. duplicate
# colors makes it harder for the user to guess the code
# MVP, no duplicate colors allwowed
# prompt again
# save it in user_code
#
#
# Enhancement: keep track of how many times user guesses
# the code. Save this in num_user_wins
#
# DONE Enhancement: keep track of user_min_guesses, which
# is the shortest number of guesses the user needed
# to guess a code
#
# DONE Set number of max times user can guess the code
# as on the board game - 12. Use variable max_guesses
#
# Enhancement. prefer using emojis but
# ask if user wants letters. Allows for color blind user.
# Note - MVP, using letters handles color blind user.
# Emojis or colored pegs are NOT good for color blind
# user.
#
# DONE need a variable to store the board
# The board can be a list of lists
# two lists used:
# guesses and checks.
# and hidden_code is part of board
# Each list represents a line on the board
# They are ordered: first guess is first in list
#
# This function checks code against guess_code
# and returns number of colors ok and number of pegs ok
#
# function to check_code given a_code and guess_code
# loop over pegs/letters in a_code
#   if the peg is the same color as a peg in guess_code
#       increment colors_ok
#       OR build the string of color check "o"s -
#        YES this is better
#
#   if the peg is in the same position as peg in guess_code
#       increment pegs_ok
#       OR build the string of peg check solid "o"s
#       YES this is better
#   return a list of two strings (colors_check, pegs_check)
#
# NOT doing it this way
# check the code and update the lists
# of colors_ok and pegs_ok
# These are lists of ints. Each one corresponds to
# the code in the list of user guesses.
#
#
# NOT done this way
# Each line on the board is a list of 3 items
# the first item is code_guess
# the second item is the colors_ok, int
# NO it will be a string colors_check
# the third item is pegs_ok, int
# NO it will be a string pegs_ok
#
# or at first, maintain three lists;
# one is guesses
# one is colors_ok, a list of ints
# one is pegs_ok, a list of ints
#
#
# Need a new name for this. It doesn't print
# the string. Just returns the string.
# Or we already have the string "o"s above
# DONT need this, string is built above
# function print_colors_check(a_num)
#   make a string of "o"s of length a_num
#   return the string
# DONT need this, string is built above
# Need a new name for this. It doesn't print
# the string. Just returns the string.
# Or we already have the string of solid "o"s above
#
# function print_pegs_check(a_num)
#   make a string of solid "o"s of length a_num
#   return the string
#

# function to display_board
# loop over lines on the board, in order
#
#   print colors_check, pegs_check, code,
#       on one line
#
#   This is how actual board looks
#
#   To solve the code it is important
#   to see all guesses/checks at once
#   not mixed with input of code from user
#
#

# main function to play the game


# peg sets are tuples, so they can't be changed.
# PEG_LETTERS is here becuase it is needed in get_user_code
PEG_LETTERS = ("R", "O", "Y", "G", "B", "I", "V")

    # Solved: terminal on mac handles emojis typed by user
    # Can't type emojis in repl.it terminal/interpreter 
   
PEG_BULLETS = ("🍎", "🏀", "🍋", "🍏", "🌎", "🏐", "😈")


#  ***********  High level function to play the game ***********
#  *************************************************************

def mastermind():
    """ Play mastermind: Guess the hidden code! """


    INSTRUCTIONS = """
    A hidden_code of 5 pegs is randomly generated.

    You guess the code on each turn and
    see a code check after each turn.

    The code check helps you figure out the code.

    "x" means a peg is right color and position
    "o" means a peg is right color
    "-" means a peg is not right color/position

    Note!
    Code check does NOT correspond to peg positions.

    You get only 12 guesses, like in the real board game.
    """

    MAX_GUESSES = 12

    code_length = get_code_length()

 #   print("code_length: ", code_length)

    # get the user's name
    user_name = get_user_name()

    min_user_guesses = 0  # set per user, initialize to 0
                        # because you cannot have 0 guesses

    # Tell the user how to play
    welcome_and_how_to_play(user_name, INSTRUCTIONS)


    # SHOULD create a function to have user choose pegs
    # MVP, easier for me to start with PEG_LETTERS, because
    # I never used emoticons before and input/output of letters is simple

                # for now, keep one of these uncommented to SET peg set
    # a_peg_set = PEG_LETTERS          
    a_peg_set = PEG_BULLETS
   

    # show the user what pegs they can use
    print_peg_set(a_peg_set)

    # a loop to see if user wants to play again,
    # then make a new code, and keep track of
    # min guesses for their best game

    play_again = True  # initialize, to play at least once

    while play_again:    # while user wants to play more, so start a new game

                # intialize variables per game
        user_guesses = 0     # set per game
        success = False     # init this flag; user didn't find code yet

                # initialize, need these guesses and checks to print board
        guesses_list = []     # save all guesses in a game
        checks_list = []    # save code checks in a game

                # make hidden_code, a list
                # give it code length and peg set, and capture
                # hidden code list and hidden string
        hidden_code_info = make_hidden_code(code_length,a_peg_set)
        hidden_code = hidden_code_info[0]       # grab code as list
        hidden_str = hidden_code_info[1]        # grab code as string


        # SHOULD put WHILE loop in a functon, maybe let_user_guess
        # while user has more guesses and not found code
        # Note: user_code and guess are the SAME
        # ask user for a new guess
        # condition is < so that user can do it one
        # more time UP TO MAX_GUESSES
        #
        while ((user_guesses < MAX_GUESSES) and (not success)):

            user_code = get_user_code(code_length, a_peg_set)

            # NEED TO handle return of False or something
            # from get_user_code
            # to allow user to quit in middle of game
            # but don't ask each time, just use a "q"
            # for a guess as a quit and figure
            # out the logic

            guesses_list.append(user_code) #save guesses

            user_guesses = user_guesses + 1

            # print("before check code")
            # print("H code: ", hidden_code)
            # print("U code: ", user_code)
            results = check_code(user_code, hidden_code)

                                # capture results[0] = is checks
                                # add to list of all checks
            checks_list.append(results[0])     # save check for each guess
            success = results[1]    # capture success flag

         #   print("results: {} success: {}".format(results[0], success))

         #   print_board(guesses_list, checks_list)

            print()

            print_nice_board(guesses_list, checks_list)



        # *********   GAME is over now   **********************
        # SO either user guessed the code or ran out of guesses

        #  if success, keep track of
        # min_user guesses over many games
        # other things to do if success
        # tell user they guessed it and show
        # board with hidden code
        # This should be in a function maybe handle_success
        if success:

            print()
            print("{}, you found the code!".format(user_name))
           
            print()
            print("   {}".format(hidden_str))

            if min_user_guesses != 0 :    # after the first game
                # min_user_guesses is smallest
                # of user_guesses and min_user_guesses
                min_user_guesses = min(min_user_guesses, user_guesses)
            else:           # first time
                min_user_guesses = user_guesses

            # no success and reached MAX_GUESSES
        else:       # no success so don't update min_user_guesses

            print()
            print("GAME OVER: Code not found after {} guesses ".format(MAX_GUESSES))

            print("Hidden code was:")
            
            print(hidden_str)

        # test if user guessed it and print a message about min guesses for this user
        tell_guesses_in_game(min_user_guesses, user_guesses)
        

        print()
        print("End of game")

        # NEED TO REQUIRE and check y/n and lower case it
        # these variable names are not good
        # but I like play_again in while loop
        print()
        new_game = (input("{}, do you want to play again? ".format(user_name))).lower()

        if new_game == "n":
            play_again = False

            # user wants to play again, is there anything to do?
            # is this else needed?
        else:
            pass
            # print("Need to add logic for new game")
            # print(" or I don't need this 'else'")

    # ****** USER is done playing Mastermind *********

    # tell user their best game
    tell_user_best_game(user_name, min_user_guesses)


    print()
    print("Ending Mastermind!")
    print()


# Play the game; call the high level function
mastermind()
