import pandas as pd

from app.carinsurance_model.config.core import config
from app.carinsurance_model.processing.features_preprocessing import (
    TemporalVariableTransformer,
)


def test_temporal_variable_transformer(sample_input_data: pd.DataFrame) -> None:
    # Given
    transformer = TemporalVariableTransformer(
        variable=config.model_config.temporal_var,  # Call Duration
        ref_variables=config.model_config.ref_vars,
    )
    assert sample_input_data["CallStart"].iat[0] == "17:17:42"
    assert sample_input_data["CallEnd"].iat[0] == "17:18:06"

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["CallDuration"].iat[0] == 24
