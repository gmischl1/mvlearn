import pytest
import numpy as np
from mvlearn.preprocessing import mv_data_split

RANDOM_SEED = 10
np.random.seed(RANDOM_SEED)

@pytest.fixture(scope='module')
def r_data():
    data = list()
    for _ in range(3):
        data.append(np.random.random((20, 10)))

    return data

def test_data_split(r_data):
    train_Xs, test_Xs = mv_data_split(r_data, random_state=RANDOM_SEED)
    assert len(train_Xs) == 3
    assert len(test_Xs) == 3
    
    for X in train_Xs:
        assert X.shape == (15, 10)
    for X in test_Xs:
        assert X.shape == (5, 10)
    
def test_data_split_params(r_data):
    
    train_Xs, test_Xs = mv_data_split(r_data, test_size=0.2, train_size=None,
                                      random_state=RANDOM_SEED, shuffle=True,
                                      stratify=None)
    assert len(train_Xs) == 3
    assert len(test_Xs) == 3
    
    for X in train_Xs:
        assert X.shape == (16, 10)
    for X in test_Xs:
        assert X.shape == (4, 10)