"""
Обработка состояний
Класс Context хранит все методы которые могут вызываться
экземплярами класса State
"""

from __future__ import annotations
# позволяет использовать описание классов определенных ниже
from abc import ABC, abstractmethod
import PySimpleGUI as Sg
from src.products import Product
from src.order import Order


class Context:
    """
    Класс хранит текущее состояние и определяет интерфейс
    для выполнения действия по запросу клиентом
    """

    """Текущее состояние контекста"""
    __state = None

    def __init__(self, state: State):
        self.item_list_c = []
        self.item_list_s = []
        self.item_list_o = []

        self.transition_to(state)

        self.lazy_load()

        self.layout_main = [[Sg.Frame('Главное меню',
                                      layout=[[Sg.Button('Завершить', key='-EXIT-', size=15),
                                               Sg.Button('Стартовое меню', key='-START-', size=15)]])]]

        self.layout_mode = [[Sg.Button('Каталог товаров', key='-CATALOG-', visible=True, size=15),
                             Sg.Button('Склад', key='-STOCK-', visible=True, size=15),
                             Sg.Button('Заказ', key='-ORDER-', visible=True, size=15)]]

        self.layout_frame_mode = [[Sg.Frame('Режим работы', layout=self.layout_mode)]]

        self.layout_lbc = [
            [Sg.Listbox(self.item_list_c, key='-LBC-', s=(25, 10), select_mode=Sg.LISTBOX_SELECT_MODE_EXTENDED)],
            [Sg.Button('Выбрать', key='-LBCS-')]]
        self.layout_lbs = [
            [Sg.Listbox(self.item_list_s, key='-LBS-', s=(25, 10), select_mode=Sg.LISTBOX_SELECT_MODE_EXTENDED)],
            [Sg.Button('Выбрать', key='-LBSS-')]]
        self.layout_lbo = [
            [Sg.Listbox(self.item_list_o, key='-LBO-', s=(25, 10), select_mode=Sg.LISTBOX_SELECT_MODE_EXTENDED)],
            [Sg.Button('Выбрать', key='-LBOS-')]]

        self.layout_catalog = [[Sg.Frame('Каталог товаров', layout=self.layout_lbc)]]
        self.layout_stock = [[Sg.Frame('Склад', layout=self.layout_lbs)]]
        self.layout_order = [[Sg.Frame('Заказ', layout=self.layout_lbo)]]
        self.layout_output = [[Sg.T('Консоль вывода')], [Sg.Output(s=(800,10))]]

        # set layout
        self.layout = [[Sg.Column(self.layout_main)],
                       [Sg.Column(self.layout_frame_mode)],
                       [Sg.Column(self.layout_catalog, visible=False, key='-COLC-'),
                        Sg.Column(self.layout_stock, visible=False, key='-COLS-'),
                        Sg.Column(self.layout_order, visible=False, key='-COLO-')],
                       [Sg.Column(self.layout_output, visible=True)]]
        # run window
        self.window = Sg.Window('CkyCafe', self.layout, size=(800, 600))

    def lazy_load(self):
        """ Загрузка данных в модель """
        # загрузить из файлов в модель

        # получить данные из модели
        for itm in range(5):
            item = Product(f'Product {itm}', 10)
            self.item_list_c.append(item)

        self.item_list_s = ['Товар А', 'Товар B', 'Товар C']
        # item_list_o = ['Товар А', 'Товар B', 'Товар C']

        for itm_o in range(5):
            order = Order()
            self.item_list_o.append(order)

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
        event, values = self.context.window.read()
        print(event, values)

        if event == Sg.WIN_CLOSED or event == '-EXIT-':
            self.context.window.close()
            self.context.transition_to(StateEnd())
        elif event == '-CATALOG-':
            self.context.window['-COLC-'].update(visible=True)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=False)
            # self.context.window['-COL2-'].update(visible=True)
            self.context.transition_to(StateCatalog())
        elif event == '-STOCK-':
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=True)
            self.context.window['-COLO-'].update(visible=False)
            self.context.transition_to(StateStock())
        elif event == '-ORDER-':
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=True)
            self.context.transition_to(StateOrder())


class StateEnd(State):
    """
    Завершение
    """

    def handle_action(self):
        pass


class StateCatalog(State):
    """
    Состояние Каталог
    """

    def handle_action(self):
        event, values = self.context.window.read()
        print(event, values)

        if event == Sg.WIN_CLOSED or event == '-EXIT-':
            self.context.window.close()
            self.context.transition_to(StateEnd())
        elif event == '-START-':
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=False)
            self.context.transition_to(StateStart())
        # elif event == '-CATALOG-':
        #     self.context.window['-COLC-'].update(visible=True)
        #     self.context.window['-COLS-'].update(visible=False)
        #     self.context.window['-COLO-'].update(visible=False)
        #     # self.context.window['-COL2-'].update(visible=True)
        #     self.context.transition_to(StateCatalog())
        elif event == '-STOCK-':
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=True)
            self.context.window['-COLO-'].update(visible=False)
            self.context.transition_to(StateStock())
        elif event == '-ORDER-':
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=True)
            self.context.transition_to(StateOrder())
        elif event == '-LBCS-':
            print('Описание')
            for itm in values['-LBC-']:
                print(itm.name)


class StateStock(State):
    """ Состояние склад/запасы """

    def handle_action(self):
        event, values = self.context.window.read()
        print(event, values)
        if event == Sg.WIN_CLOSED or event == '-EXIT-':
            self.context.window.close()
            self.context.transition_to(StateEnd())
        elif event == '-START-':
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=False)
            self.context.transition_to(StateStart())
        elif event == '-CATALOG-':
            self.context.window['-COLC-'].update(visible=True)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=False)
            # self.context.window['-COL2-'].update(visible=True)
            self.context.transition_to(StateCatalog())
        # elif event == '-STOCK-':
        #     self.context.window['-COLC-'].update(visible=False)
        #     self.context.window['-COLS-'].update(visible=True)
        #     self.context.window['-COLO-'].update(visible=False)
        #     self.context.transition_to(StateStock())
        elif event == '-ORDER-':
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=True)
            self.context.transition_to(StateOrder())
        elif event == '-LBSS-':
            print('Описание')
            for itm in values['-LBS-']:
                print(itm)


class StateOrder(State):
    """ Состояние заказ """

    def handle_action(self):
        event, values = self.context.window.read()
        print(event, values)
        if event == Sg.WIN_CLOSED or event == '-EXIT-':
            self.context.window.close()
            self.context.transition_to(StateEnd())
        elif event == '-START-':
            # self.context.window['-CATALOG-'].update(visible=True)
            # self.context.window['-START-'].update(visible=False)
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=False)
            self.context.transition_to(StateStart())
        elif event == '-CATALOG-':
            self.context.window['-COLC-'].update(visible=True)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=False)
            # self.context.window['-COL2-'].update(visible=True)
            self.context.transition_to(StateCatalog())
        elif event == '-STOCK-':
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=True)
            self.context.window['-COLO-'].update(visible=False)
            self.context.transition_to(StateStock())
        elif event == '-ORDER-':
            self.context.window['-COLC-'].update(visible=False)
            self.context.window['-COLS-'].update(visible=False)
            self.context.window['-COLO-'].update(visible=True)
            self.context.transition_to(StateOrder())
        elif event == '-LBOS-':
            print('Описание')
            for itm in values['-LBO-']:
                print(itm.title)
