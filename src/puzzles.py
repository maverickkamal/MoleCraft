from dataclasses import dataclass, field
from typing import List, Tuple, Dict
from enum import Enum


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


@dataclass
class Puzzle:
    name: str
    formula: str
    difficulty: Difficulty
    carbons: List[Tuple[int, int]]
    target_atoms: List[Tuple[str, int, int]]
    target_bonds: List[Tuple[Tuple[int, int], Tuple[int, int], int]]
    hint: str = ""
    time_limit: int = 60


EASY_PUZZLES = [
    Puzzle(
        name="Methane",
        formula="CH4",
        difficulty=Difficulty.EASY,
        carbons=[(30, 10)],
        target_atoms=[
            ("H", 28, 10), ("H", 32, 10), ("H", 30, 8), ("H", 30, 12)
        ],
        target_bonds=[
            ((30, 10), (28, 10), 1),
            ((30, 10), (32, 10), 1),
            ((30, 10), (30, 8), 1),
            ((30, 10), (30, 12), 1),
        ],
        hint="Carbon needs 4 hydrogens",
        time_limit=45,
    ),
    Puzzle(
        name="Ethane",
        formula="C2H6",
        difficulty=Difficulty.EASY,
        carbons=[(28, 10), (32, 10)],
        target_atoms=[
            ("H", 26, 10), ("H", 28, 8), ("H", 28, 12),
            ("H", 34, 10), ("H", 32, 8), ("H", 32, 12),
        ],
        target_bonds=[
            ((28, 10), (32, 10), 1),
            ((28, 10), (26, 10), 1),
            ((28, 10), (28, 8), 1),
            ((28, 10), (28, 12), 1),
            ((32, 10), (34, 10), 1),
            ((32, 10), (32, 8), 1),
            ((32, 10), (32, 12), 1),
        ],
        hint="Two carbons connected, each with 3 H",
        time_limit=60,
    ),
    Puzzle(
        name="Propane",
        formula="C3H8",
        difficulty=Difficulty.EASY,
        carbons=[(26, 10), (30, 10), (34, 10)],
        target_atoms=[
            ("H", 24, 10), ("H", 26, 8), ("H", 26, 12),
            ("H", 30, 8), ("H", 30, 12),
            ("H", 36, 10), ("H", 34, 8), ("H", 34, 12),
        ],
        target_bonds=[
            ((26, 10), (30, 10), 1),
            ((30, 10), (34, 10), 1),
            ((26, 10), (24, 10), 1),
            ((26, 10), (26, 8), 1),
            ((26, 10), (26, 12), 1),
            ((30, 10), (30, 8), 1),
            ((30, 10), (30, 12), 1),
            ((34, 10), (36, 10), 1),
            ((34, 10), (34, 8), 1),
            ((34, 10), (34, 12), 1),
        ],
        hint="Chain of 3 carbons",
        time_limit=75,
    ),
    Puzzle(
        name="Water",
        formula="H2O",
        difficulty=Difficulty.EASY,
        carbons=[],
        target_atoms=[
            ("O", 30, 10), ("H", 28, 10), ("H", 32, 10)
        ],
        target_bonds=[
            ((30, 10), (28, 10), 1),
            ((30, 10), (32, 10), 1),
        ],
        hint="Oxygen in center, H on sides",
        time_limit=30,
    ),
    Puzzle(
        name="Ammonia",
        formula="NH3",
        difficulty=Difficulty.EASY,
        carbons=[],
        target_atoms=[
            ("N", 30, 10), ("H", 28, 10), ("H", 32, 10), ("H", 30, 12)
        ],
        target_bonds=[
            ((30, 10), (28, 10), 1),
            ((30, 10), (32, 10), 1),
            ((30, 10), (30, 12), 1),
        ],
        hint="Nitrogen with 3 hydrogens",
        time_limit=30,
    ),
    Puzzle(
        name="Hydrogen Chloride",
        formula="HCl",
        difficulty=Difficulty.EASY,
        carbons=[],
        target_atoms=[
            ("Cl", 30, 10), ("H", 28, 10)
        ],
        target_bonds=[
            ((30, 10), (28, 10), 1),
        ],
        hint="Simple H-Cl bond",
        time_limit=20,
    ),
    Puzzle(
        name="Methanol",
        formula="CH3OH",
        difficulty=Difficulty.EASY,
        carbons=[(28, 10)],
        target_atoms=[
            ("H", 26, 10), ("H", 28, 8), ("H", 28, 12),
            ("O", 32, 10), ("H", 34, 10)
        ],
        target_bonds=[
            ((28, 10), (26, 10), 1),
            ((28, 10), (28, 8), 1),
            ((28, 10), (28, 12), 1),
            ((28, 10), (32, 10), 1),
            ((32, 10), (34, 10), 1),
        ],
        hint="Carbon with 3H and an OH group",
        time_limit=60,
    ),
    Puzzle(
        name="Hydrogen Peroxide",
        formula="H2O2",
        difficulty=Difficulty.EASY,
        carbons=[],
        target_atoms=[
            ("O", 28, 10), ("O", 32, 10), ("H", 26, 10), ("H", 34, 10)
        ],
        target_bonds=[
            ((28, 10), (32, 10), 1),
            ((28, 10), (26, 10), 1),
            ((32, 10), (34, 10), 1),
        ],
        hint="Two oxygens bonded together",
        time_limit=40,
    ),
    Puzzle(
        name="Hydrogen",
        formula="H2",
        difficulty=Difficulty.EASY,
        carbons=[],
        target_atoms=[
            ("H", 29, 10), ("H", 31, 10)
        ],
        target_bonds=[
            ((29, 10), (31, 10), 1),
        ],
        hint="Two hydrogens bonded",
        time_limit=15,
    ),
    Puzzle(
        name="Chlorine",
        formula="Cl2",
        difficulty=Difficulty.EASY,
        carbons=[],
        target_atoms=[
            ("Cl", 29, 10), ("Cl", 31, 10)
        ],
        target_bonds=[
            ((29, 10), (31, 10), 1),
        ],
        hint="Two chlorines bonded",
        time_limit=15,
    ),
]

MEDIUM_PUZZLES = [
    Puzzle(
        name="Ethene",
        formula="C2H4",
        difficulty=Difficulty.MEDIUM,
        carbons=[(28, 10), (32, 10)],
        target_atoms=[
            ("H", 28, 8), ("H", 28, 12),
            ("H", 32, 8), ("H", 32, 12),
        ],
        target_bonds=[
            ((28, 10), (32, 10), 2),
            ((28, 10), (28, 8), 1),
            ((28, 10), (28, 12), 1),
            ((32, 10), (32, 8), 1),
            ((32, 10), (32, 12), 1),
        ],
        hint="Double bond between carbons",
        time_limit=60,
    ),
    Puzzle(
        name="Ethyne",
        formula="C2H2",
        difficulty=Difficulty.MEDIUM,
        carbons=[(28, 10), (32, 10)],
        target_atoms=[
            ("H", 26, 10), ("H", 34, 10),
        ],
        target_bonds=[
            ((28, 10), (32, 10), 3),
            ((28, 10), (26, 10), 1),
            ((32, 10), (34, 10), 1),
        ],
        hint="Triple bond between carbons",
        time_limit=60,
    ),
    Puzzle(
        name="Formaldehyde",
        formula="CH2O",
        difficulty=Difficulty.MEDIUM,
        carbons=[(30, 10)],
        target_atoms=[
            ("H", 28, 10), ("H", 32, 10), ("O", 30, 8)
        ],
        target_bonds=[
            ((30, 10), (28, 10), 1),
            ((30, 10), (32, 10), 1),
            ((30, 10), (30, 8), 2),
        ],
        hint="Aldehyde: C=O double bond",
        time_limit=60,
    ),
    Puzzle(
        name="Carbon Dioxide",
        formula="CO2",
        difficulty=Difficulty.MEDIUM,
        carbons=[(30, 10)],
        target_atoms=[
            ("O", 26, 10), ("O", 34, 10)
        ],
        target_bonds=[
            ((30, 10), (26, 10), 2),
            ((30, 10), (34, 10), 2),
        ],
        hint="Double bonds to both oxygens",
        time_limit=45,
    ),
    Puzzle(
        name="Ethanol",
        formula="C2H5OH",
        difficulty=Difficulty.MEDIUM,
        carbons=[(26, 10), (30, 10)],
        target_atoms=[
            ("H", 24, 10), ("H", 26, 8), ("H", 26, 12),
            ("H", 30, 8), ("H", 30, 12),
            ("O", 34, 10), ("H", 36, 10)
        ],
        target_bonds=[
            ((26, 10), (30, 10), 1),
            ((26, 10), (24, 10), 1),
            ((26, 10), (26, 8), 1),
            ((26, 10), (26, 12), 1),
            ((30, 10), (30, 8), 1),
            ((30, 10), (30, 12), 1),
            ((30, 10), (34, 10), 1),
            ((34, 10), (36, 10), 1),
        ],
        hint="Ethane with OH group",
        time_limit=75,
    ),
    Puzzle(
        name="Acetic Acid",
        formula="CH3COOH",
        difficulty=Difficulty.MEDIUM,
        carbons=[(26, 10), (30, 10)],
        target_atoms=[
            ("H", 24, 10), ("H", 26, 8), ("H", 26, 12),
            ("O", 30, 8), ("O", 34, 10), ("H", 36, 10)
        ],
        target_bonds=[
            ((26, 10), (30, 10), 1),
            ((26, 10), (24, 10), 1),
            ((26, 10), (26, 8), 1),
            ((26, 10), (26, 12), 1),
            ((30, 10), (30, 8), 2),
            ((30, 10), (34, 10), 1),
            ((34, 10), (36, 10), 1),
        ],
        hint="Carboxylic acid: C=O and O-H",
        time_limit=90,
    ),
    Puzzle(
        name="Propene",
        formula="C3H6",
        difficulty=Difficulty.MEDIUM,
        carbons=[(24, 10), (28, 10), (32, 10)],
        target_atoms=[
            ("H", 24, 8), ("H", 24, 12),
            ("H", 28, 8), ("H", 28, 12),
            ("H", 34, 10), ("H", 32, 12)
        ],
        target_bonds=[
            ((24, 10), (28, 10), 2),
            ((28, 10), (32, 10), 1),
            ((24, 10), (24, 8), 1),
            ((24, 10), (24, 12), 1),
            ((28, 10), (28, 8), 1),
            ((28, 10), (28, 12), 1),
            ((32, 10), (34, 10), 1),
            ((32, 10), (32, 12), 1),
        ],
        hint="Double bond at one end",
        time_limit=90,
    ),
    Puzzle(
        name="Acetone",
        formula="C3H6O",
        difficulty=Difficulty.MEDIUM,
        carbons=[(24, 10), (30, 10), (36, 10)],
        target_atoms=[
            ("H", 22, 10), ("H", 24, 8), ("H", 24, 12),
            ("O", 30, 8),
            ("H", 38, 10), ("H", 36, 8), ("H", 36, 12)
        ],
        target_bonds=[
            ((24, 10), (30, 10), 1),
            ((30, 10), (36, 10), 1),
            ((30, 10), (30, 8), 2),
            ((24, 10), (22, 10), 1),
            ((24, 10), (24, 8), 1),
            ((24, 10), (24, 12), 1),
            ((36, 10), (38, 10), 1),
            ((36, 10), (36, 8), 1),
            ((36, 10), (36, 12), 1),
        ],
        hint="Ketone: C=O in middle",
        time_limit=90,
    ),
    Puzzle(
        name="Formic Acid",
        formula="HCOOH",
        difficulty=Difficulty.MEDIUM,
        carbons=[(30, 10)],
        target_atoms=[
            ("H", 28, 10), ("O", 30, 8), ("O", 34, 10), ("H", 36, 10)
        ],
        target_bonds=[
            ((30, 10), (28, 10), 1),
            ((30, 10), (30, 8), 2),
            ((30, 10), (34, 10), 1),
            ((34, 10), (36, 10), 1),
        ],
        hint="Simplest carboxylic acid",
        time_limit=60,
    ),
    Puzzle(
        name="Dimethyl Ether",
        formula="C2H6O",
        difficulty=Difficulty.MEDIUM,
        carbons=[(24, 10), (36, 10)],
        target_atoms=[
            ("H", 22, 10), ("H", 24, 8), ("H", 24, 12),
            ("O", 30, 10),
            ("H", 38, 10), ("H", 36, 8), ("H", 36, 12)
        ],
        target_bonds=[
            ((24, 10), (30, 10), 1),
            ((30, 10), (36, 10), 1),
            ((24, 10), (22, 10), 1),
            ((24, 10), (24, 8), 1),
            ((24, 10), (24, 12), 1),
            ((36, 10), (38, 10), 1),
            ((36, 10), (36, 8), 1),
            ((36, 10), (36, 12), 1),
        ],
        hint="Ether: C-O-C",
        time_limit=75,
    ),
]

HARD_PUZZLES = [
    Puzzle(
        name="Butane",
        formula="C4H10",
        difficulty=Difficulty.HARD,
        carbons=[(22, 10), (26, 10), (30, 10), (34, 10)],
        target_atoms=[
            ("H", 20, 10), ("H", 22, 8), ("H", 22, 12),
            ("H", 26, 8), ("H", 26, 12),
            ("H", 30, 8), ("H", 30, 12),
            ("H", 36, 10), ("H", 34, 8), ("H", 34, 12)
        ],
        target_bonds=[
            ((22, 10), (26, 10), 1),
            ((26, 10), (30, 10), 1),
            ((30, 10), (34, 10), 1),
            ((22, 10), (20, 10), 1),
            ((22, 10), (22, 8), 1),
            ((22, 10), (22, 12), 1),
            ((26, 10), (26, 8), 1),
            ((26, 10), (26, 12), 1),
            ((30, 10), (30, 8), 1),
            ((30, 10), (30, 12), 1),
            ((34, 10), (36, 10), 1),
            ((34, 10), (34, 8), 1),
            ((34, 10), (34, 12), 1),
        ],
        hint="Linear chain of 4 carbons",
        time_limit=120,
    ),
    Puzzle(
        name="Butadiene",
        formula="C4H6",
        difficulty=Difficulty.HARD,
        carbons=[(22, 10), (26, 10), (30, 10), (34, 10)],
        target_atoms=[
            ("H", 22, 8), ("H", 22, 12),
            ("H", 26, 12),
            ("H", 30, 12),
            ("H", 34, 8), ("H", 34, 12)
        ],
        target_bonds=[
            ((22, 10), (26, 10), 2),
            ((26, 10), (30, 10), 1),
            ((30, 10), (34, 10), 2),
            ((22, 10), (22, 8), 1),
            ((22, 10), (22, 12), 1),
            ((26, 10), (26, 12), 1),
            ((30, 10), (30, 12), 1),
            ((34, 10), (34, 8), 1),
            ((34, 10), (34, 12), 1),
        ],
        hint="Alternating double bonds",
        time_limit=120,
    ),
    Puzzle(
        name="Glycine",
        formula="C2H5NO2",
        difficulty=Difficulty.HARD,
        carbons=[(26, 10), (32, 10)],
        target_atoms=[
            ("N", 24, 10), ("H", 22, 10), ("H", 24, 8),
            ("H", 26, 12),
            ("O", 32, 8), ("O", 36, 10), ("H", 38, 10)
        ],
        target_bonds=[
            ((26, 10), (32, 10), 1),
            ((26, 10), (24, 10), 1),
            ((24, 10), (22, 10), 1),
            ((24, 10), (24, 8), 1),
            ((26, 10), (26, 12), 1),
            ((32, 10), (32, 8), 2),
            ((32, 10), (36, 10), 1),
            ((36, 10), (38, 10), 1),
        ],
        hint="Amino acid: NH2-C-COOH",
        time_limit=120,
    ),
    Puzzle(
        name="Urea",
        formula="CH4N2O",
        difficulty=Difficulty.HARD,
        carbons=[(30, 10)],
        target_atoms=[
            ("O", 30, 6),
            ("N", 26, 10), ("H", 24, 10), ("H", 26, 12),
            ("N", 34, 10), ("H", 36, 10), ("H", 34, 12)
        ],
        target_bonds=[
            ((30, 10), (30, 6), 2),
            ((30, 10), (26, 10), 1),
            ((30, 10), (34, 10), 1),
            ((26, 10), (24, 10), 1),
            ((26, 10), (26, 12), 1),
            ((34, 10), (36, 10), 1),
            ((34, 10), (34, 12), 1),
        ],
        hint="Two NH2 groups on carbonyl",
        time_limit=120,
    ),
    Puzzle(
        name="Methyl Formate",
        formula="C2H4O2",
        difficulty=Difficulty.HARD,
        carbons=[(26, 10), (34, 10)],
        target_atoms=[
            ("H", 26, 8),
            ("O", 26, 12),
            ("O", 30, 10),
            ("H", 34, 8), ("H", 34, 12), ("H", 36, 10)
        ],
        target_bonds=[
            ((26, 10), (26, 8), 1),
            ((26, 10), (26, 12), 2),
            ((26, 10), (30, 10), 1),
            ((30, 10), (34, 10), 1),
            ((34, 10), (34, 8), 1),
            ((34, 10), (34, 12), 1),
            ((34, 10), (36, 10), 1),
        ],
        hint="Ester: C(=O)-O-C",
        time_limit=120,
    ),
    Puzzle(
        name="Chloroform",
        formula="CHCl3",
        difficulty=Difficulty.HARD,
        carbons=[(30, 10)],
        target_atoms=[
            ("H", 30, 8),
            ("Cl", 28, 10), ("Cl", 32, 10), ("Cl", 30, 12)
        ],
        target_bonds=[
            ((30, 10), (30, 8), 1),
            ((30, 10), (28, 10), 1),
            ((30, 10), (32, 10), 1),
            ((30, 10), (30, 12), 1),
        ],
        hint="One H, three Cl on carbon",
        time_limit=60,
    ),
    Puzzle(
        name="Acetaldehyde",
        formula="C2H4O",
        difficulty=Difficulty.HARD,
        carbons=[(26, 10), (32, 10)],
        target_atoms=[
            ("H", 24, 10), ("H", 26, 8), ("H", 26, 12),
            ("O", 32, 8), ("H", 34, 10)
        ],
        target_bonds=[
            ((26, 10), (32, 10), 1),
            ((26, 10), (24, 10), 1),
            ((26, 10), (26, 8), 1),
            ((26, 10), (26, 12), 1),
            ((32, 10), (32, 8), 2),
            ((32, 10), (34, 10), 1),
        ],
        hint="CH3-CHO aldehyde",
        time_limit=90,
    ),
    Puzzle(
        name="Nitromethane",
        formula="CH3NO2",
        difficulty=Difficulty.HARD,
        carbons=[(28, 10)],
        target_atoms=[
            ("H", 26, 10), ("H", 28, 8), ("H", 28, 12),
            ("N", 32, 10), ("O", 32, 8), ("O", 34, 10)
        ],
        target_bonds=[
            ((28, 10), (26, 10), 1),
            ((28, 10), (28, 8), 1),
            ((28, 10), (28, 12), 1),
            ((28, 10), (32, 10), 1),
            ((32, 10), (32, 8), 2),
            ((32, 10), (34, 10), 1),
        ],
        hint="CH3 with NO2 group",
        time_limit=120,
    ),
    Puzzle(
        name="Propanol",
        formula="C3H7OH",
        difficulty=Difficulty.HARD,
        carbons=[(22, 10), (28, 10), (34, 10)],
        target_atoms=[
            ("H", 20, 10), ("H", 22, 8), ("H", 22, 12),
            ("H", 28, 8), ("H", 28, 12),
            ("H", 34, 8), ("H", 34, 12),
            ("O", 38, 10), ("H", 40, 10)
        ],
        target_bonds=[
            ((22, 10), (28, 10), 1),
            ((28, 10), (34, 10), 1),
            ((22, 10), (20, 10), 1),
            ((22, 10), (22, 8), 1),
            ((22, 10), (22, 12), 1),
            ((28, 10), (28, 8), 1),
            ((28, 10), (28, 12), 1),
            ((34, 10), (34, 8), 1),
            ((34, 10), (34, 12), 1),
            ((34, 10), (38, 10), 1),
            ((38, 10), (40, 10), 1),
        ],
        hint="Propane with OH",
        time_limit=120,
    ),
    Puzzle(
        name="Lactic Acid",
        formula="C3H6O3",
        difficulty=Difficulty.HARD,
        carbons=[(22, 10), (28, 10), (34, 10)],
        target_atoms=[
            ("H", 20, 10), ("H", 22, 8), ("H", 22, 12),
            ("O", 28, 8), ("H", 28, 6),
            ("O", 34, 8), ("O", 38, 10), ("H", 40, 10)
        ],
        target_bonds=[
            ((22, 10), (28, 10), 1),
            ((28, 10), (34, 10), 1),
            ((22, 10), (20, 10), 1),
            ((22, 10), (22, 8), 1),
            ((22, 10), (22, 12), 1),
            ((28, 10), (28, 8), 1),
            ((28, 8), (28, 6), 1),
            ((34, 10), (34, 8), 2),
            ((34, 10), (38, 10), 1),
            ((38, 10), (40, 10), 1),
        ],
        hint="CH3-CHOH-COOH",
        time_limit=150,
    ),
]


MOLECULE_FACTS = {
    "Methane": "Methane is the main component of natural gas.",
    "Ethane": "Ethane is the second-largest component of natural gas.",
    "Propane": "Propane is commonly used as fuel for grills and heaters.",
    "Water": "A single glass of water has more molecules than there are glasses of water in all the oceans.",
    "Ammonia": "Ammonia is used in most commercial fertilizers.",
    "Hydrogen Chloride": "Hydrogen chloride dissolved in water is hydrochloric acid.",
    "Methanol": "Methanol is the simplest alcohol and is toxic to humans.",
    "Hydrogen Peroxide": "Hydrogen peroxide is used by bombardier beetles as a defense mechanism.",
    "Hydrogen": "Hydrogen is the most abundant element in the universe.",
    "Chlorine": "Chlorine gas was used as a chemical weapon in World War I.",
    "Ethene": "Ethene (ethylene) is used to ripen bananas artificially.",
    "Ethyne": "Ethyne (acetylene) burns hot enough to cut through steel.",
    "Formaldehyde": "Formaldehyde is used to preserve biological specimens.",
    "Carbon Dioxide": "CO2 makes up only 0.04% of Earth's atmosphere but drives climate change.",
    "Ethanol": "Ethanol is the alcohol in alcoholic beverages.",
    "Acetic Acid": "Acetic acid is what gives vinegar its sour taste.",
    "Propene": "Propene (propylene) is used to make polypropylene plastic.",
    "Acetone": "Acetone is the main ingredient in nail polish remover.",
    "Formic Acid": "Formic acid is what makes ant stings burn. Its name comes from 'formica' (Latin for ant).",
    "Dimethyl Ether": "Dimethyl ether is being studied as a diesel fuel replacement.",
    "Butane": "Butane is the fuel in disposable lighters.",
    "Butadiene": "Butadiene is used to make synthetic rubber for tires.",
    "Glycine": "Glycine is the simplest amino acid and a building block of proteins.",
    "Urea": "Urea was the first organic compound synthesized from inorganic materials (1828).",
    "Methyl Formate": "Methyl formate is used as a fumigant for dried fruits and cereals.",
    "Chloroform": "Chloroform was one of the first anesthetics used in surgery.",
    "Acetaldehyde": "Acetaldehyde is what causes hangovers -- your body produces it when breaking down alcohol.",
    "Nitromethane": "Nitromethane is used as fuel in drag racing cars.",
    "Propanol": "Propanol is used as a solvent in the pharmaceutical industry.",
    "Lactic Acid": "Lactic acid builds up in your muscles during intense exercise.",
}


def get_puzzles(difficulty: Difficulty) -> list:
    if difficulty == Difficulty.EASY:
        return EASY_PUZZLES
    elif difficulty == Difficulty.MEDIUM:
        return MEDIUM_PUZZLES
    else:
        return HARD_PUZZLES
