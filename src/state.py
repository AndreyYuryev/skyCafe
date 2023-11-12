"""
Обработка состояний
Класс Context хранит все методы которые могут вызываться
экземплярами класса State
"""

from __future__ import annotations
# позволяет использовать описание классов определенных ниже
from abc import ABC, abstractmethod
import PySimpleGUI as Sg


class Context:
    """
    Класс хранит текущее состояние и определяет интерфейс
    для выполнения действия по запросу клиентом
    """

    """Текущее состояние контекста"""
    __state = None

    def __init__(self, state: State):
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        Изменение состояния.
        Может вызываться в обработчике конкретного State
        для смены состояния.
        """
        self.__state = state
        self.__state.context = self

    @property
    def state(self):
        return self.__state

    def welcome(self):
        """
        Интерфейс действий welcome
        :return:
        """
        self.__state.handle_welcome()

    def goodbye(self):
        """
        Интерфейс действия goodbye
        :return:
        """
        self.__state.handle_goodbye()

    def action(self):
        """
        Интерфейс действий action
        """
        self.__state.handle_action()


class State(ABC):
    """
    Базовый класс состояния.
    Объявляет методы, которые реализуют конкретные состояния,
    а также предоставляет ссылку на объект контекст связанный
    с состоянием.
    """

    @property
    def context(self):
        """
        Возвращает контекст
        :return:
        """
        return self.__context

    @context.setter
    def context(self, context: Context):
        """
        Устанавливает контекст
        :param context:
        :return:
        """
        self.__context = context

    def handle_welcome(self):
        """ Приветственное действие """
        Sg.popup('Добро пожаловать в наше кафе!')

    def handle_goodbye(self):
        """ Прощальное окно """
        Sg.popup('До свидания. Ждем вас в нашем кафе!')

    @abstractmethod
    def handle_action(self):
        """
        Описание обработчика действия request_a
        :return:
        """


class StateStart(State):
    """
    Начальное состояние
    """

    def handle_action(self):


        point = int(input(f'\n1-Сделать заказ\n2-Посмотреть каталог\n3-Завершение работы\n'))
        match point:
            case 1:
                self.context.transition_to(StateOrder())
            case 2:
                self.context.transition_to(StateCatalog())
            case 3:
                self.context.transition_to(StateEnd())


class StateEnd(State):
    """
    Завершение
    """

    def handle_action(self):
        pass


class StateOrder(State):
    """
    Состояние Процесс заказа
    """

    def handle_action(self):
        cart = dict()
        answer = ''
        while answer != 'n':
            answer = input('ID позиции количество')
            if answer == 'n':
                break
            item, quantity = map(int, answer.split())
            cart[item] = quantity
        for key, value in cart.items():
            print(f'Заказано: {key} {value} штук')
            # добавить в корзину товар

        self.context.transition_to(StateOrdered())


class StateOrdered(State):
    """
    Состояние Заказано
    """

    def handle_action(self):
        point = int(input(f'\n1-Заказать товар\n2-Посмотреть каталог\n3-Запросить склад\n4-Вернуться в начало\n'))
        match point:
            case 1:
                self.context.transition_to(StateOrder())
            case 2:
                self.context.transition_to(StateCatalog())
            case 3:
                self.context.transition_to(StateDelivery())
            case 4:
                self.context.transition_to(StateStart())


class StateCatalog(State):
    """
    Состояние Каталог
    """

    def handle_action(self):
        print('Показываем каталог')
        for item in range(5):
            print(f'Товар {item}')
        point = int(input(f'\n1-Заказать товар\n2-Вернуться в начало\n'))
        match point:
            case 1:
                self.context.transition_to(StateOrder())
            case 2:
                self.context.transition_to(StateStart())
            case 3:
                pass


class StateDelivery(State):
    """
    Состояние Запрос склада
    """

    def handle_action(self):
        print('Ждем подтверждения от склада')
        point = int(input(f'\n1-Забрать товар\n2-Изменить заказ\n'))
        match point:
            case 1:
                self.context.transition_to(StateDelivered())
            case 2:
                self.context.transition_to(StateOrder())
            case 3:
                pass


class StateDelivered(State):
    """
    Состояние Запрос склада
    """

    def handle_action(self):
        print('Товар выдан')
        point = int(input(f'\n1-Перейти в начало\n2-Завершение работы\n'))
        match point:
            case 1:
                self.context.transition_to(StateStart())
            case 2:
                self.context.transition_to(StateEnd())
            case 3:
                pass
