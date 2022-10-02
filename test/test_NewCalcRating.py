# -*- coding: utf-8 -*-
from typing import Dict, Tuple

from src.Types import DataType
from src.NewCalcRating import NewCalcRating
import pytest

RatingsType = Dict[str, float]


class TestCalcRating:

    @pytest.fixture()
    def input_data(self) -> Tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ],
            "Игорев Игорь Владимирович":
                [
                    ("математика", 50),
                    ("русский язык", 52),
                    ("программирование", 49),
                ],
            "Игорев Артем Владимирович":
                [
                    ("математика", 60),
                    ("русский язык", 60),
                    ("программирование", 60),
                    ("литература", 50)
                ]

        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000,
            "Игорев Игорь Владимирович": 50.3333,
            "Игорев Артем Владимирович": 57.5000,

        }

        return data, rating_scores

    def test_init_calc_rating(self, input_data: Tuple[DataType,
                                                      RatingsType]) -> None:

        calc_rating = NewCalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: Tuple[DataType, RatingsType]) -> None:

        rating = NewCalcRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]
