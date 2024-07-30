from individual import Individual


class PSO:
    def __init__(self, board_size: int = 8, n_individual: int = 100, n_iter: int = 100) -> None:
        self.board_size = board_size
        self.n_iter = n_iter
        self.n_individual = n_individual
        self.individual = [Individual.new_random(n=board_size) for _ in range(n_individual)]

    def run(self) -> Individual:
        raise NotImplementedError("Implementar esto")
