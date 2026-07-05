from src.data_loader import load_all_assets
from src.preprocessing import clean_data

def test_imports():
    assert callable(load_all_assets)
    assert callable(clean_data)