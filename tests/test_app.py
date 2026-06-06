import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#header")


def test_graph_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#sales-chart")


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-picker")