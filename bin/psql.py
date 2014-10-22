#!/usr/bin/env python
############################################################################
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
############################################################################

import os
import subprocess
import sys
import phoenix_utils

phoenix_utils.setPath()

phoenix_client_jar = phoenix_utils.phoenix_client_jar
# Backward support old env PHOENIX_LIB_DIR
phoenix_home_path = os.getenv('PHOENIX_LIB_DIR','')
if phoenix_home_path == "":
    phoenix_home_path = os.getenv('PHOENIX_HOME','')

if phoenix_client_jar == "":
    phoenix_client_jar = phoenix_utils.find("phoenix-*-client.jar", phoenix_home_path)

hbase_conf_path = os.getenv('HBASE_CONF_DIR','.')

# HBase configuration folder path (where hbase-site.xml reside) for
# HBase/Phoenix client side property override
java_cmd = 'java -cp "' + phoenix_utils.hbase_conf_path + os.pathsep + phoenix_utils.phoenix_client_jar + \
    '" -Dlog4j.configuration=file:' + \
    os.path.join(phoenix_utils.current_dir, "log4j.properties") + \
    " org.apache.phoenix.util.PhoenixRuntime " + ' '.join(sys.argv[1:])

subprocess.call(java_cmd, shell=True)
