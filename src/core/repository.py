import abc


class AbstractRepository(abc.ABC):
    """Абстрактная модель репозитория."""

    @abc.abstractmethod
    async def get(self, *args, **kwargs):
        """Метод получения записи по id из БД."""
        raise NotImplementedError

    @abc.abstractmethod
    async def add(self, *args, **kwargs):
        """Метод добавления записи в БД."""
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, *args, **kwargs):
        """Метод обновления записи в БД."""
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, *args, **kwargs):
        """Метод удаления записи из БД."""
        raise NotImplementedError

    @abc.abstractmethod
    async def list(self, *args, **kwargs):
        """Метод получения всех записей из БД."""
        raise NotImplementedError

    @abc.abstractmethod
    async def filter(self, *args, **kwargs):
        """Метод получения отфильтрованных записей из БД."""
        raise NotImplementedError
