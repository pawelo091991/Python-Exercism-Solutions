# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """Calculate bake time.

    :param number_of_layers: int number of lasagna layers.
    :return: int time in minutes to prepare lasagna 

    Function that takes the number of lasagna layers and calculates bake time in oven 
    """
    return 2 * number_of_layers

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :param number_of_layers: int number of lasagna layers. 
    :return: int elapsed bake time

    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time