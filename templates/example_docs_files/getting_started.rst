Getting Started
===============

Welcome to the Brewing Package! This guide will help you get started with using the package in your Python projects.


Usage
-----

Once you have installed the package (See installation instructions), you can start using it in your Python projects. Here's a quick example of how to brew a potion using the Brewing Package:

.. code-block:: python

    import potion_class
    import containers
    import cooking
    import inspection
    my_potion = potion_class.Potion(student_name=student_name)
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    cooking.simmer(my_potion, duration=5)
    inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')

For more detailed usage instructions and examples, refer to the documentation of each module:

- :doc:`Potion Module </potion_module>`
- :doc:`Ingredients Module </ingredients_module>`
- :doc:`Inspection Module </inspection_module>`

