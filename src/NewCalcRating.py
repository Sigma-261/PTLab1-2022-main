# -*- coding: utf-8 -*-
from typing import Dict

from Types import DataType

RatingType = Dict[str, float]


class NewCalcRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        new_rating = {}
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        rating = list(self.rating.values())
        amount = len(self.data)
        index = amount // 2
        if amount % 2:
            median = sorted(rating)[index]
        else:
            median = sum(sorted(rating)[index - 1:index + 1]) / 2
        for key in self.data:
            if self.rating[key] >= median:
                new_rating[key] = self.rating[key]
        return new_rating
