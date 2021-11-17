#!/usr/bin/python3

import feedback_pipeline

def test_build_completion():
    assert 1 == 1

def test_get_configs():
    feedback_pipeline.get_configs(feedback_pipeline.load_settings())