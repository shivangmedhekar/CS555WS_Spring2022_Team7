# ---------------------------------------------------------------------------- #
#                         US 05: Marriage before death                         #
# ---------------------------------------------------------------------------- #

from datetime import datetime
from UserStories.helper_functions import difference_in_dates
def marriage_before_death(marriage_date: datetime.date, death_date:datetime.date) -> bool:
    """
    Marriage should occur before death of either spouse

    Args:
        marriageDate (_type_): _description_
        deathDate (_type_): _description_

    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
    """
    # if the marriage date & death date are empty/null
    if not marriage_date or not death_date:
        return True

    # if the death date is after the marriage date
    no_of_days_differnece = difference_in_dates(start_date = marriage_date, end_date = death_date, unit = 'days')
    
    if no_of_days_differnece >= 0:
        return True

    # if the marriage date is after the death date
    else:
        raise Exception("marriage {} is after death {}".format(str(marriage_date, str(death_date))))