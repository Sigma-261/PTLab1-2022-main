# -*- coding: utf-8 -*-
from typing import Dict

from Types import DataType

RatingType = Dict[str, float]


def calc_median(amount, rating):
    index = amount // 2
    if amount % 2:
        return sorted(rating)[index]
    return sum(sorted(rating)[index - 1:index + 1]) / 2


class NewCalcRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        q1_rating = {}
        q2_rating = {}
        q3_rating = {}
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        rating = list(self.rating.values())
        amount = len(self.data)
        median = calc_median(amount=amount, rating=rating)
        for key in self.data:
            if self.rating[key] > median:
                q3_rating[key] = self.rating[key]
            elif self.rating[key] < median:
                q1_rating[key] = self.rating[key]
        q3 = calc_median(amount=len(q3_rating), rating=list(q3_rating.values()))
        q1 = calc_median(amount=len(q1_rating), rating=list(q1_rating.values()))
        for key in self.data:
            if q1 < self.rating[key] < q3:
                q2_rating[key] = self.rating[key]
        return q2_rating
