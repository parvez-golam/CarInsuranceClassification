from typing import List

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class TemporalVariableTransformer(BaseEstimator, TransformerMixin):
    """Temporal Call duration transformer."""

    def __init__(self, variable: str, ref_variables: List[str]):

        if not isinstance(ref_variables, list):
            raise ValueError("ref. variables should be a list")

        self.variable = variable
        self.ref_variables = ref_variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        # we need this step to fit the sklearn pipeline
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:

        #  so that we do not over-write the original dataframe
        X = X.copy()

        X[self.variable] = (
            pd.to_datetime(X[self.ref_variables[1]], format="%H:%M:%S")
            - pd.to_datetime(X[self.ref_variables[0]], format="%H:%M:%S")
        ) / np.timedelta64(1, "s")

        return X


class Mapper(BaseEstimator, TransformerMixin):
    """Categorical variable mapper."""

    def __init__(self, variables: List[str], mappings: dict):

        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables
        self.mappings = mappings

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        # we need the fit statement to accomodate the sklearn pipeline
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)

        return X
