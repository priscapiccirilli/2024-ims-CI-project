import pytest

from brewing import potion_class
from brewing import containers
from brewing import cooking
from brewing import inspection


@pytest.fixture
def example_potion():
    my_potion = potion_class.Potion(student_name="Harry")
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    return my_potion

def test_inspection_by_Snape_correct(example_potion, capsys):
    """Test inspection_by_Snape function with correct potion.

    This test checks the behavior of the inspection_by_Snape function when provided with a correct potion.
    It verifies that the function prints the correct message indicating the potion passed inspection.

    Parameters:
    - example_potion: Fixture providing an instance of Potion class with correct attributes.
    - capsys: Pytest fixture to capture stdout/stderr output.

    """
    # Call the function with the correct potion
    inspection.inspection_by_Snape(example_potion, target_potion='example_potion')
    # Capture the printed output
    captured = capsys.readouterr()
    # Assert that the correct message is printed
    assert "You pack your bags and leave as fast as you can!" in captured.out

def test_inspection_by_Snape_wrong_container(example_potion, capsys):
    """Test inspection_by_Snape function with incorrect container.

    This test checks the behavior of the inspection_by_Snape function when provided with a potion
    that has the wrong container. It verifies that the function prints the correct error message
    and penalty imposed by Snape.

    Parameters:
    - example_potion: Fixture providing an instance of Potion class with correct attributes.
    - capsys: Pytest fixture to capture stdout/stderr output.

    """
    # Modify the container of the potion to make it wrong
    example_potion.container = 'pewter_cauldron'
    # Call the function with the potion
    inspection.inspection_by_Snape(example_potion, target_potion='example_potion')
    # Capture the printed output
    captured = capsys.readouterr()
    # Assert that the correct error message and penalty are printed
    assert "You have used the wrong cauldron or heat" in captured.out
    assert "I am taking 10 points from Ravenclaw, Harry. Start again!" in captured.out

def test_inspection_by_Snape_wrong_ingredients(example_potion, capsys):
    """Test inspection_by_Snape function with incorrect ingredients.

    This test checks the behavior of the inspection_by_Snape function when provided with a potion
    that has the wrong ingredients. It verifies that the function prints the correct error message
    and penalty imposed by Snape.

    Parameters:
    - example_potion: Fixture providing an instance of Potion class with correct attributes.
    - capsys: Pytest fixture to capture stdout/stderr output.

    """
    # Modify the ingredients of the potion to make them wrong
    example_potion.ingredients = ['snake_skin', 'fish_eyes', 'unicorn_hair']
    # Call the function with the potion
    inspection.inspection_by_Snape(example_potion, target_potion='example_potion')
    # Capture the printed output
    captured = capsys.readouterr()
    # Assert that the correct error message and penalty are printed
    assert "You have used the wrong ingredients" in captured.out
    assert "I am taking 10 points from Gryffindor, Harry. Start again!" in captured.out

def test_inspection_by_Snape_undercooked(example_potion, capsys):
    """Test inspection_by_Snape function with undercooked potion.

    This test checks the behavior of the inspection_by_Snape function when provided with a potion
    that is undercooked. It verifies that the function prints the correct error message
    and penalty imposed by Snape.

    Parameters:
    - example_potion: Fixture providing an instance of Potion class with correct attributes.
    - capsys: Pytest fixture to capture stdout/stderr output.

    """
    # Modify the simmer duration of the potion to make it undercooked
    example_potion.simmer_duration = 1
    # Call the function with the potion
    inspection.inspection_by_Snape(example_potion, target_potion='example_potion')
    # Capture the printed output
    captured = capsys.readouterr()
    # Assert that the correct error message and penalty are printed
    assert "Your potion is undercooked!" in captured.out
    assert "I am taking 10 points from Hufflepuff, Harry. Start again!" in captured.out


def test_simmer_function_correct(example_potion):
    """Test simmer function with correct simmer duration.

    This test checks the behavior of the simmer function when provided with a correct simmer duration.
    It verifies that the potion's simmer duration and cooked attributes are updated correctly.

    Parameters:
    - example_potion: Fixture providing an instance of Potion class with correct attributes.

    """
    # Call the simmer function with a correct simmer duration
    cooking.simmer(example_potion, duration=3)
    # Assert that the potion's simmer duration is updated correctly
    assert example_potion.simmer_duration == 3
    # Assert that the potion's cooked attribute is set to True
    assert example_potion.cooked is True

def test_stir_function_clockwise(example_potion, capsys):
    """Test stir function with clockwise direction.

    This test checks the behavior of the stir function when stirring the potion clockwise.
    It verifies that the potion's color is updated correctly and the appropriate message is printed.

    Parameters:
    - example_potion: Fixture providing an instance of Potion class with correct attributes.
    - capsys: Pytest fixture to capture stdout/stderr output.

    """
    # Call the stir function with clockwise direction
    cooking.stir(example_potion, direction='clockwise')
    # Capture the printed output
    captured = capsys.readouterr()
    # Assert that the correct message is printed
    assert "NO!! Your potion turns vomit-yellow. Did you stir in the right direction?" in captured.out
    # Assert that the potion's color is updated correctly
    assert example_potion.colour == "vomit-yellow"

def test_stir_function_anticlockwise(example_potion, capsys):
    """Test stir function with anti-clockwise direction.

    This test checks the behavior of the stir function when stirring the potion anti-clockwise.
    It verifies that the potion's color is updated correctly and the appropriate message is printed.

    Parameters:
    - example_potion: Fixture providing an instance of Potion class with correct attributes.
    - capsys: Pytest fixture to capture stdout/stderr output.

    """
    # Call the stir function with anti-clockwise direction
    cooking.stir(example_potion, direction='anti-clockwise')
    # Capture the printed output
    captured = capsys.readouterr()
    # Assert that the correct message is printed
    assert "Your potion turns a lovely newt-green." in captured.out
    # Assert that the potion's color is updated correctly
    assert example_potion.colour == "newt-green"