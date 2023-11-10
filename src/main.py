""" Точка входа для проекта """
from src.state import Context, StateStart, StateEnd


def main():
    """ Стартовая точка проекта """
    context = Context(StateStart())
    context.welcome()
    while not isinstance(context.state, StateEnd):
        context.action()
    context.goodbye()


if __name__ == '__main__':
    # Запуск проекта
    main()
