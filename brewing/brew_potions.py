"""Module for brewing potions.

This module provides functions for brewing potions. It includes functions for creating different types of potions, such as example potions and Python expert potions.
"""

from brewing import potion_class
from brewing import containers
from brewing import cooking
from brewing import inspection


def make_example_potion(student_name="ASPP student"):
    """Create an example potion instance.

    Parameters
    ----------
    student_name : str, optional
        The name of the student brewing the potion. Default is "ASPP student".

    Returns
    -------
    my_potion : Potion instance
        An instance of the Potion class representing the example potion.
    """
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print(f"You successfully ran make_example_potion, {student_name}, well done :).")
    return my_potion


def make_python_expert_potion(student_name):
    """Create a Python expert potion instance

    This function is responsible for creating a Python expert potion for a specific student.
    The potion is brewed according to the standards required for achieving expertise in Python.

    Parameters
    ----------
    student_name : str
        The name of the student brewing the potion.

    Returns
    -------
    my_potion : Potion instance
        An instance of the Potion class representing the example potion.

    Notes
    -----
    This function is a placeholder and requires implementation to define the brewing process
    for the Python expert potion.
    """
    print("I am a Python Expert")
    # todo: write this function!
    return


if __name__ == "__main__":
    my_name = 'ASPP student'
    my_potion = make_example_potion(student_name=my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')
