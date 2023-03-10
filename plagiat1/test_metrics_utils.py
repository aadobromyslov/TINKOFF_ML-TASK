from typing import Tuple
import numpy as np
from etna.datasets import TSDataset
from etna.metrics import MAE
from etna.metrics import MAPE

from etna.metrics import MSE
from etna.metrics.utils import compute_metrics

    
def test_compute_metrics(train: Tuple[TSDataset, TSDataset]):
        (forecast, true_df) = train
        metrics = [MAE('per-segment'), MAE(mode='macro'), MSE('per-segment'), MAPE(mode='macro', eps=1e-05)]
        expected_keys = ["MAE(mode = 'per-segment', )", "MAE(mode = 'macro', )", "MSE(mode = 'per-segment', )", "MAPE(mode = 'macro', eps = 1e-05, )"]
        result = compute_metrics(metrics=metrics, y_true=true_df, y_pred=forecast)
        np.testing.assert_array_equal(sorted(expected_keys), sorted(result.keys()))
