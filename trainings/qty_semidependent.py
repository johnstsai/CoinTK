from cointk.prescient_sim import compute_prescient
from cointk.strategies.prescient import QtySemidependent
from cointk.backtest import backtest


strategy = QtySemidependent()
compute_prescient(
    strategy, history_fnm='prescient_histories/qty_independent.npz')
backtest(strategy, datapart='train')
