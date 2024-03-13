
from brewing import potion_class
from brewing import containers
from brewing import cooking
from brewing import inspection
import pytest

def test_simmer():
    my_potion = potion_class.Potion(student_name="test")
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)

    assert my_potion.simmer_duration == 5

@pytest.mark.xfail
def test_simmer2():
    my_potion = potion_class.Potion(student_name="test")
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    cooking.simmer(my_potion, duration=None)

    assert my_potion.simmer_duration == 0