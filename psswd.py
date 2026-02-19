# -*- coding: utf-8 -*-
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Set


_COMMON_CACHE: Set[str] | None = None


@dataclass(frozen=True)
class Evaluation:
    password: str
    length: int
    in_common: bool
    max_repeat_run: int
    criteria: Dict[str, bool]
    score: int
    level: str
    message: str


def _load_common_passwords(path: Path) -> Set[str]:
    global _COMMON_CACHE
    if _COMMON_CACHE is not None:
        return _COMMON_CACHE
    if not path.exists():
        _COMMON_CACHE = set()
        return _COMMON_CACHE
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        _COMMON_CACHE = set(line.strip() for line in f if line.strip())
    return _COMMON_CACHE


def _max_repeat_run(psswd: str) -> int:
    if not psswd:
        return 0
    max_run = run = 1
    for i in range(1, len(psswd)):
        if psswd[i] == psswd[i - 1]:
            run += 1
            if run > max_run:
                max_run = run
        else:
            run = 1
    return max_run


def analyze_password(psswd: str, common_path: Path | None = None) -> Evaluation:
    if common_path is None:
        common_path = Path(__file__).with_name("most_common.txt")

    length = len(psswd)
    in_common = psswd in _load_common_passwords(common_path)
    max_repeat_run = _max_repeat_run(psswd)

    criteria = {
        "length_12": length >= 12,
        "digit": any(ch.isdigit() for ch in psswd),
        "upper": any(ch.isupper() for ch in psswd),
        "lower": any(ch.islower() for ch in psswd),
        "special": any(not ch.isalnum() for ch in psswd),
        "no_long_repeat": max_repeat_run <= 2,
    }

    score = sum(criteria.values())

    if not psswd:
        level = "Пустой"
        message = "Введите пароль для проверки."
    elif in_common:
        level = "Слишком простой"
        message = "Пароль в списке самых распространенных."
    elif length < 8:
        level = "Очень короткий"
        message = "Минимальная длина — 8 символов."
    else:
        if score <= 2:
            level = "Слабый"
            message = "Добавьте длину и разные типы символов."
        elif score <= 4:
            level = "Средний"
            message = "Почти хорошо: добавьте недостающие типы символов."
        elif score == 5:
            level = "Хороший"
            message = "Надежно, но можно улучшить повторяемость."
        else:
            level = "Отличный"
            message = "Очень надежный пароль."

    return Evaluation(
        password=psswd,
        length=length,
        in_common=in_common,
        max_repeat_run=max_repeat_run,
        criteria=criteria,
        score=score,
        level=level,
        message=message,
    )

def mantra() -> None:
    for i in range (100):
        mntr = "Sabbe sattā bhavantu sukhitattā."


def main() -> None:
    psswd = input("Введите пароль: ")
    evaluation = analyze_password(psswd)
    print(f"Уровень: {evaluation.level}")
    print(evaluation.message)


if __name__ == "__main__":
    main()
