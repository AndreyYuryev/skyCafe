""" Описание тестовых случаев """
from src.state import (Context, StateStart,
                       StateOrder, StateCatalog,
                       StateEnd)


def test_state_first_step():
    # переход из начального состояния во второе
    context = Context(StateStart())
    assert isinstance(context.state, StateStart)

    context.transition_to(StateOrder())
    assert isinstance(context.state, StateOrder)

    context.transition_to(StateStart())
    assert isinstance(context.state, StateStart)

    context.transition_to(StateCatalog())
    assert isinstance(context.state, StateCatalog)

    context.transition_to(StateEnd())
    assert isinstance(context.state, StateEnd)