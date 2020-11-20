from typing import Tuple, Set, List


class State:
    def __init__(self,
                 player: List[int],
                 piedra: Set[Tuple[int, int]],
                 agua: Set[Tuple[int, int]],
                 aspa: Set[Tuple[int, int]],
                 llave: Tuple[int, int],
                 tiene_llave: bool
                 ) -> None:
        self.player = player
        self.piedra = piedra
        self.agua = agua
        self.aspa = aspa
        self.llave = llave
        self.has_llave = tiene_llave

    def get_player(self):
        return self.player

    def get_piedra(self):
        return self.piedra

    def get_agua(self):
        return self.agua

    def get_aspa(self):
        return self.aspa

    def get_llave(self):
        return self.llave

    def tiene_llave(self):
        return self.has_llave

    def __str__(self) -> str:
        return f"Player: {self.player} + Piedra: {self.piedra} + Agua + {self.agua} + Aspa: {self.aspa} + Llave: {self.llave} + Tiene llave: {self.tiene_llave()}"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash((self.agua, self.aspa, self.player, self.piedra, self.llave))

    def __eq__(self, other) -> bool:
        return (self.__module__ == other.__module__ and
                self.agua.__eq__(other.get_agua()) and
                self.aspa.__eq__(other.get_aspa()) and
                self.llave.__eq__(other.get_llave()) and
                self.piedra.__eq__(other.get_piedra()) and
                self.player.__eq__(other.get_player))


class Level:
    def __init__(self, tablero: Tuple[Tuple[int, ...], ...],
                 destino: Tuple[int, int],
                 enemigo: Tuple[int, int],
                 ) -> None:
        self.tablero = tablero
        self.destino = destino
        self.enemigo = enemigo

    def get_tablero(self):
        return self.tablero

    def get_destino(self) -> Tuple[int, int]:
        return self.destino

    def get_enemigo(self) -> Tuple[int, int]:
        return self.enemigo

    def __str__(self) -> str:
        return f"Enemigo: {self.enemigo} + Destino: {self.destino} + Tablero: {self.tablero}"
