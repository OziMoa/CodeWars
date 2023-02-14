""" DESCRIPTION:
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
  """


def tower_builder(n_floors):
    # build here
    totallen = n_floors * 2
    tower = []
    for i in range(1, n_floors+1):
        blank = int( (totallen - (2 * i )) / 2)
        print(blank)
        tower.append( ' ' * blank + '*' * (2 * i - 1) + ' ' * blank )

    return tower
