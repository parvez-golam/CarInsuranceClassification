from feature_engine.encoding import OneHotEncoder
from feature_engine.imputation import CategoricalImputer
from feature_engine.selection import DropFeatures
from feature_engine.transformation import YeoJohnsonTransformer
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Binarizer, StandardScaler

from app.carinsurance_model.config.core import config
from app.carinsurance_model.processing import features_preprocessing as pp

model_pipe = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute categorical variables with string missing
        (
            "missing_imputation",
            CategoricalImputer(
                imputation_method="missing",
                variables=config.model_config.categorical_vars_with_na_missing,
            ),
        ),
        # impute categorical variables with mode value
        (
            "frequent_imputation",
            CategoricalImputer(
                imputation_method="frequent",
                variables=config.model_config.categorical_vars_with_na_frequent,
            ),
        ),
        # == TEMPORAL VARIABLES ====
        (
            "call_duration",
            pp.TemporalVariableTransformer(
                variable=config.model_config.temporal_var,
                ref_variables=config.model_config.ref_vars,
            ),
        ),
        ("drop_features", DropFeatures(features_to_drop=config.model_config.ref_vars)),
        # ==== VARIABLE TRANSFORMATION =====
        (
            "yeojohnson",
            YeoJohnsonTransformer(
                variables=config.model_config.numerical_yeo_vars,
            ),
        ),
        (
            "binarizer",
            SklearnTransformerWrapper(
                transformer=Binarizer(threshold=0),
                variables=config.model_config.binarize_vars,
            ),
        ),
        # === mappers ===
        (
            "mapper_month",
            pp.Mapper(
                variables=config.model_config.map_vars,
                mappings=config.model_config.month_mappings,
            ),
        ),
        # == CATEGORICAL ENCODING
        # encode categorical with one hot encoding
        (
            "categorical_encoder",
            OneHotEncoder(
                drop_last=True,
                variables=config.model_config.categorical_vars_encode,
            ),
        ),
        # scale
        ("scaler", StandardScaler()),
        # ml model
        (
            "clf",
            RandomForestClassifier(
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
