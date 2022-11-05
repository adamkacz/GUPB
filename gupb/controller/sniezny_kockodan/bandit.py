from enum import Enum
import random

MENHIR_MOVEMENT_COUNTER_INIT: int = 50

EPSILON = 0.1


class Tactics(Enum):
    ATTACKER = {
        'attack_pass': True,
        'menhir_movement_count': MENHIR_MOVEMENT_COUNTER_INIT
    }
    FAST_MENHIR = {
        'attack_pass': False,
        'menhir_movement_count': 0
    }
    CLASSIC = {
        'attack_pass': False,
        'menhir_movement_count': MENHIR_MOVEMENT_COUNTER_INIT
    }


POSSIBLE_TACTICS = [
    Tactics.ATTACKER,
    Tactics.FAST_MENHIR,
    Tactics.CLASSIC
]


class Bandit:

    def __init__(self):
        self.q: dict[Tactics, float] = {}
        for tactic in POSSIBLE_TACTICS:
            self.q[tactic] = 0

        self.n: dict[Tactics, int] = {}
        for tactic in POSSIBLE_TACTICS:
            self.n[tactic] = 0

        self.current_tactics: Tactics = random.choice(POSSIBLE_TACTICS)
        self.searching_index: float = EPSILON

    def choose_tactics(self) -> None:
        if self.searching_index > random.random():
            self.current_tactics = random.choice(POSSIBLE_TACTICS)
        else:
            self.current_tactics = max(self.q, key=self.q.get)

    def update_tables(self, reward: int) -> None:
        self.n[self.current_tactics] += 1
        self.q[self.current_tactics] += 1 / self.n[self.current_tactics] * (reward - self.q[self.current_tactics])
        self.choose_tactics()
