import vampytest

from ..terminal_control_commands import create_command_up


def _iter_options():
    yield -10, ''
    yield -1, ''
    yield 0, ''
    yield 1, f'\u001b[{1}A'
    yield 10, f'\u001b[{10}A'


@vampytest._(vampytest.call_from(_iter_options()).returning_last())
def test__create_command_up(part):
    """
    Tests whether ``create_command_up`` works as intended.
    
    Parameters
    ----------
    amount : `str`
        The amount to move the cursor by.
    
    Returns
    -------
    output : `bool`
    """
    output = create_command_up(part)
    vampytest.assert_instance(output, str)
    return output
