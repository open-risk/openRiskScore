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

from hierarchicalScorecard import HierarchicalScorecard

"""
Test Example (TODO move to tests)
"""

# Load the scorecard structure from file
scorecard = json.load(open("./datasets/scorecard_TEST1.json"))

# Create a new scorecard
PFScore = HierarchicalScorecard(scorecard)

# Load the attribute values
scorecard_data = json.load(open("./datasets/data_TEST1.json"))

# calculate the score
score = PFScore.score(scorecard_data)

print(score)
