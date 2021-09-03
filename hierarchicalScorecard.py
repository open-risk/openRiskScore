# (c) 2021 Open Risk (https://www.openriskmanagement.com)
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


import networkx as nx
from networkx.readwrite import json_graph


class HierarchicalScorecard:

    def __init__(self, structure):
        self.structure = structure
        self.G = json_graph.tree_graph(structure)

    def score(self, data):
        """

        The weight of each node is used to construct the weighted average partial score that is being aggregated to
        the node parent (summing over all sibling nodes)

        """

        leaf_nodes = [x for x in self.G.nodes() if self.G.out_degree(x) == 0]
        path_scores = []
        for x in leaf_nodes:

            # construct path from root to leaf node of scorecard
            path = nx.shortest_path(self.G, source='0', target=x)
            scores = []
            # get the partial score of the leaf node
            i = len(path) - 1
            weight = self.G.nodes[x]['weight']  # this weight should be unity
            attribute = data[x]
            partial_score = weight * attribute
            i -= 1
            scores.append(partial_score)
            # iterate over path
            while i >= 0:
                node = path[i]
                weight = self.G.nodes[node]['weight']
                partial_score = weight * scores[0]
                i -= 1
                scores.insert(0, partial_score)
            path_scores.append(scores)

        total_score = 0
        for scores in path_scores:
            total_score += scores[0]
        return round(total_score)
