#!/usr/bin/python3

import feedback_pipeline

def create_mock_settings():
    settings = {}
    settings["configs"] = "code/input"
    settings["allowed_arches"] = ["armv7hl","aarch64","ppc64le","s390x","x86_64"]

def test_build_completion():
    assert 1 == 1

def test_get_configs():
    feedback_pipeline.get_configs(feedback_pipeline.load_settings(create_mock_settings()))