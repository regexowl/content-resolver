#!/usr/bin/python3

import feedback_pipeline

def create_mock_settings():
    settings = {}
    settings["configs"] = "code/input/configs"
    settings["allowed_arches"] = ["armv7hl","aarch64","ppc64le","s390x","x86_64"]

    return settings

def test_build_completion():
    assert 1 == 1

def test_get_configs():
    feedback_pipeline.get_configs(create_mock_settings())

print(feedback_pipeline.get_configs(create_mock_settings()))