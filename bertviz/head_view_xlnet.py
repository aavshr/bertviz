# coding=utf-8
# Copyright 2018 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Change log
# 07/13/19  Jesse Vig   Adapted to xlnet model


"""Module for postprocessing and displaying transformer attentions.

This module is designed to be called from an ipython notebook.
"""

import json
from bertviz.attention import get_attention_xlnet
from IPython.core.display import display, HTML, Javascript
import os

def show(model, tokenizer, text):
    vis_html = """
      <span style="user-select:none">
        Layer: <select id="layer"></select>
      </span>
      <div id='vis'></div>
    """
    display(HTML(vis_html))
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    vis_js = open(os.path.join(__location__, 'head_view.js')).read()
    attn_data = get_attention_xlnet(model, tokenizer, text)
    params = {
        'attention': attn_data,
        'default_filter': "all"
    }
    display(Javascript('window.params = %s' % json.dumps(params)))
    display(Javascript(vis_js))