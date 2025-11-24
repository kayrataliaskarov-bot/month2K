from tkinter.font import names
from typing import Self


class Distance:
    _CONVERSION_TO_METERS = {
        'mm': 0.001, 'millimeter': 0.001, 'millimeters': 0.001,
        'cm': 0.01, 'centimeter': 0.01, 'centimeters': 0.01,
        'm': 1.0, 'meter': 1.0, 'meters': 1.0,
        'km': 1000.0, 'kilometer': 1000.0, 'kilometers': 1000.0,
    }

    def __init__(self, value: float, unit: str = 'm'):
        unit = unit.lower()
        if unit not in self._CONVERSION_TO_METERS:
            raise ValueError(f"Неизвестная единица: {unit}")
        self.value = float(value)
        self.unit = unit

    def _to_meters(self) -> float:
        return self.value * self._CONVERSION_TO_METERS[self.unit]

    def _from_meters(self, meters: float) -> Self:
        return Distance(meters / self._CONVERSION_TO_METERS[self.unit], self.unit)

    def __str__(self) -> str:
        return f"{self.value} {self.unit}"

    def __repr__(self) -> str:
        return f"Distance({self.value}, '{self.unit}')"

    def __add__(self, other: Self) -> Self:
        if not isinstance(other, Distance):
            return NotImplemented
        return self._from_meters(self._to_meters() + other._to_meters())

    def __radd__(self, other):
        return self if other == 0 else self.__add__(other)

    def __sub__(self, other: Self) -> Self:
        if not isinstance(other, Distance):
            return NotImplemented
        result = self._to_meters() - other._to_meters()
        if result < 0:
            raise ValueError("Результат не может быть отрицательным")
        return self._from_meters(result)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            return NotImplemented
        return abs(self._to_meters() - other._to_meters()) < 1e-9

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, Distance):
            return NotImplemented
        return self._to_meters() < other._to_meters()

    def __le__(self, other: Self) -> bool:
        return self < other or self == other

    def __gt__(self, other: Self) -> bool:
        return not self <= other

    def __ge__(self, other: Self) -> bool:
        return not self < other


if names == "main":
    d1 = Distance(10, 'm')
    d2 = Distance(2, 'km')
    d3 = Distance(150, 'cm')
    d4 = Distance(500, 'millimeters')

    print(d1)
    print(d2)
    print(repr(d3))

    print(d1 + d2)
    print(d2 + d3)
    print(d1 + d3 + d4)

    print(d2 - d1)
    print(d1 - d3)

    try:
        print(d1 - d2)
    except ValueError as e:
        print("Ошибка:", e)

    print(d1 > d3)
    print(d2 == Distance(2000, 'meters'))
    print(d1 < Distance(1, 'km'))