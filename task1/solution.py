from abc import ABC, abstractmethod
import re
from typing import Final


IPV4: re.Pattern = re.compile(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')


class Connection(ABC):
    '''Симулирование подключения к устройству.'''

    MIN_PASSWORD_LENGTH: Final[int] = 8
    MAX_PASSWORD_LENGTH: Final[int] = 16

    def __init__(self, ip: str, host: str, login: str, password: str) -> None:
        self.validate_inputs(ip, password)
        self.ip = ip
        self.host = host
        self.login = login
        self.password = password

    def validate_inputs(self, ip, password) -> None:
        if not re.match(IPV4, ip):
            raise ValueError('Invalid IP address')
        if not Connection.MIN_PASSWORD_LENGTH <= \
                len(password) <= Connection.MAX_PASSWORD_LENGTH:
            raise ValueError(f'Password length must be between \
                {Connection.MIN_PASSWORD_LENGTH} and \
                    {Connection.MIN_PASSWORD_LENGTH} characters')

    @abstractmethod
    def open(self) -> None:
        pass
    
    @abstractmethod
    def close(self) -> None:
        pass
    
    @abstractmethod
    def send_command(self, command: str) -> None:
        pass
    
    @abstractmethod
    def get_printout(self) -> None:
        pass


class Telnet(Connection):
    '''Симулирование Telnet-подключения к устройству.'''

    def open(self) -> None:
        print(f'Открытие Telnet-соединения к {self.ip}...')

    def close(self) -> None:
        print(f'Закрытие Telnet-соединения к {self.ip}...')

    def send_command(self, command: str) -> None:
        print(f'Отправка команды "{command}" по Telnet-соединению к {self.ip}...')

    def get_printout(self) -> None:
        print('Получение принтаута Telnet-соединения')


class SSL(Connection):
    '''Симулирование SSL-подключения к устройству.'''

    def open(self) -> None:
        print(f'Открытие SSL-соединения к {self.ip}...')

    def close(self) -> None:
        print(f'Закрытие SSL-соединения к {self.ip}...')

    def send_command(self, command: str) -> None:
        print(f'Отправка команды "{command}" по SSL-соединению к {self.ip}...')

    def get_printout(self) -> None:
        print('Получение принтаута SSL-соединения')


if __name__ == '__main__':
    # Проверка:
    connection = Telnet(
        ip='127.0.0.1',
        host='localhost',
        login='login',
        password='password'
    )
    connection.open()
    connection.send_command('Отобразить текущий статус')
    connection.get_printout()
    connection.close()
