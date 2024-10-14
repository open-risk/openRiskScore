# (c) 2021 - 2024 Open Risk (https://www.openriskmanagement.com)
#
# openRiskScore is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of openRiskScore. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

import json

import requests

from hierarchicalScorecard import HierarchicalScorecard

"""
A realistic Scorecard Example using a fully specified scorecard:
The European Banking Authority's Project Finance Specialized Lending Specification

This example fetches the attribute data from a remote server

"""

# Load the scorecard structure from file
scorecard = json.load(open("./datasets/scorecard_EBA_PF.json"))

# Create a new project finance scorecard
PFScore = HierarchicalScorecard(scorecard)

# Load the attribute values from a remote end point
# select the endpoint
server_url = 'http://localhost:8000/api/portfolio_data/scorecards/'
scorecard_id = '1/'
# fetch the data
response = requests.get(server_url + scorecard_id)
# TODO validate conformance
scorecard_data = response.json()['scorecard_data']

# calculate the score
score = PFScore.score(scorecard_data)

print(score)
