# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Fingerprinting code for the node.js runtime.

WARNING WARNING WARNING: this file will shortly be removed.  Don't make any
changes here.  See ./ext_runtimes/runtime_defs/nodejs instead.
"""
import textwrap


# TODO(mmuller): move these into the node_app directory.
NODEJS_APP_YAML = textwrap.dedent("""\
    runtime: {runtime}
    vm: true
    api_version: 1
    """)
DOCKERIGNORE = textwrap.dedent("""\
    # Copyright 2015 Google Inc. All Rights Reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #    http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.

    node_modules
    .dockerignore
    Dockerfile
    npm-debug.log
    .git
    .hg
    .svn
    """)
