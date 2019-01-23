#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostCoroutine2Conan(base.BoostBaseConan):
    name = "boost_coroutine2"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_coroutine2"
    lib_short_names = ["coroutine2"]
    header_only_libs = ["coroutine2"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_context",
    ]


