#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from runner.koan import *


class AboutDecoratingWithFunctions(unittest.TestCase):
    def addcowbell(fn):
        fn.wow_factor = 'COWBELL BABY!'
        return fn

    @addcowbell
    def mediocre_song(self):
        return "o/~ We all live in a broken submarine o/~"

    def test_decorators_can_modify_a_function(self):
        assert_match(__, self.mediocre_song())
        self.assertEqual(__, self.mediocre_song.wow_factor)

    # ------------------------------------------------------------------

    def xmltag(fn):
        def func(*args):
            return '<' + fn(*args) + '/>'
        return func

    @xmltag
    def render_tag(self, name):
        return name

    def test_decorators_can_change_a_function_output(self):
        self.assertEqual(__, self.render_tag('llama'))
