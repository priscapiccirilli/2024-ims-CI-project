"""Module defining a Potion class for brewing potions.

This module contains a class called Potion, which represents a potion being brewed.
The Potion class includes attributes to track the potion's color, cooking status, container, heat source,
ingredients, simmer duration, and the name of the student brewing the potion.
It also provides methods for setting up the potion, adding ingredients, and managing potion attributes.
"""


class Potion:
    """Class representing a potion.

    This class provides functionality for brewing potions. It includes methods for setting up the potion,
    adding ingredients, and managing potion attributes such as color, cooking status, container, and heat source.

    Attributes:
    - colour: The color of the potion.
    - cooked: A boolean indicating whether the potion is cooked.
    - container: The container used to brew the potion.
    - heat_source: The heat source used to cook the potion.
    - ingredients: A list of ingredients in the potion.
    - simmer_duration: The duration for which the potion is simmered.
    - student_name: The name of the student brewing the potion.

    Methods:
    - setup: Add a container and/or heat_source to the potion.
    - add_ingredients: Add ingredients to the potion.

    """
    def __init__(self, student_name):
        """This is a class for brewing potions."""
        self.colour = 'there-is-no-potion-so-the-potion-has-no-color'
        self.cooked = False
        self.container = None
        self.heat_source = None
        self.ingredients = []
        self.simmer_duration = -1
        self.student_name = student_name

    def setup(self, container=None, heat_source=None):
        """Add a container and/or heat_source to the potion.

        Updates container and heat_source attributes in the class instance.

        Parameters
        ----------
        container : str, optional
            The name of the container to brew the potion in.
        heat_source : str, optional
            The name of the heat source used to cook the potions
        """
        if container == None:
            print(f'You have not specified a container - where do you think you will brew your potion?')
        if heat_source == None:
            print(f'You have not specified a heat source - how will you cook the potion?')
        self.container = container
        self.heat_source = heat_source

    def add_ingredients(self, ingredients=None):
        """Add ingredients to the potion.

        Updates ingredients and colour attributes in the class instance.

        Parameters
        ----------
        ingredients : array_like, optional
            A list of ingredients (str) to add to the potion.
        """
        if ingredients is None:
            print(f'You have added no ingredients - have you spilt them on the floor again?')
        else:
            self.ingredients = ingredients
            self.colour = "transparent"
