from abc import abstractmethod

class Renderer:
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def tick(self) -> None:
        pass