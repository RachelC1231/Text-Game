INTRO = f"""\
    Forest Adventure Game
    This game want you to go throgh the forest avoid dangers and return back to your home safely.
    There are one route that helps you get back home faster and three kinds of animals live in   the forest you may randomly encounter in this game:
                1.Route 2.Wolf 3.Bear 4.Tiger.
    You have 4 ways to choose:
                1.Explore 2.Detour 3.Hide 4.Flee 5. Rest

    For hide and rest both do not need energy.
    For explore, detour and flee need 1 energy.
    Any wrong choice will make your score decrease.
    When you encounter Wolf, Bear, you need with at least 2 energy to detour them it may take    long distance to reach home and incress 1 score. Explore a route adds up one point. For Tiger only can be hide to get a point. 

    If you are not sure directly flee will keep the original score, but 1 energy will be deducted. 
    To get the energy you must have to rest.
    All the incorrect choice will lost 1 score.
    Initial score is 5. If your score reaches 10 you win. Also if the score is negative, you lose.
    If total turns you played more than 10 it means that you passed through the distance of the  forest and successfully arrrived home.
    """

CHOICES = f"""\
    ----
    D. Detour.
    E. Explore.
    F. Flee
    H. Hide 
    R. Rest
    S. Status Check.
    Q. Quit
    ---
"""

