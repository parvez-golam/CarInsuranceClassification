"""
Note: These tests will fail if the model is not trained.
"""

import pandas as pd

from app.carinsurance_model.predict import make_prediction


def test_make_prediction(sample_input_data: pd.DataFrame) -> None:
    # Given
    expected_first10_pred_values = [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    expected_no_predictions = 1000

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], int)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert predictions[0:10] == expected_first10_pred_values
