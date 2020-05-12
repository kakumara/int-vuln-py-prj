# Copyright 2019 Sonatype Inc.
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
from setuptools import setup

with open('requirements.txt') as requirements:
    REQUIRED = requirements.read().splitlines()

setup(
    name='test_jake',
    version=__version__,
    url="https://github.com/sonatype-nexus-community/intentionally-vulnerable-python-project",
    author="Sonatype Community",
    author_email="community-group@sonatype.com",
    description="A simple application to test vulnerability scanning with Jake",
    long_description="A simple application to test vulnerability scanning with Jake",
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    python_requires='>=3.6',
    install_requires=REQUIRED,
    entry_points={
        'console_scripts':
            ['test_jake=__main__:main']
    }
)
