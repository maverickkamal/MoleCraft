from dataclasses import dataclass, field
from typing import List
import uuid


@dataclass
class Atom:
    element: str
    x: int
    y: int
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    bonds: List[str] = field(default_factory=list)


@dataclass
class Bond:
    atom_a_id: str
    atom_b_id: str
    order: int = 1
    orientation: str = "H"
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
