# encoding: utf-8

# (c) 2019 - 2026 Open Risk (https://www.openriskmanagement.com)
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

"""
This script illustrates a basic federated estimation workflow
It assumes a certain configuration of model servers is in place, e.g. that you have
successfully run the spawn_cluster.sh script and tested that the servers are live
"""

import requests
import numpy as np

# TODO remove weight hardwiring, fetch this data shape with controlled API
# TODO split main functions into modules

# Number of participating model servers
n = 4

# Weights to use in the averaging
weights = {'1': 0.25, '2': 0.25, '3': 0.25, '4': 0.25}
# weights = {'1': 0.5, '2': 0.5}

# Number of epochs to iterate
Epochs = 5

print(80 * '=')
print('Federated Credit Scoring Test Run')
print(80 * '=')

# Construct on the fly the list of model server URL's
url_list = []
for k in range(n):
    ko = k + 1
    model_server_url = 'http://127.0.0.1:500' + str(ko)
    url_list.append(model_server_url)

# Check the model server's status
for k in range(n):
    model_server_url = url_list[k]
    print('Checking server url: ', model_server_url)
    res = requests.get(model_server_url)
    print(res.json())

print(80 * '=')
print('Initialization')
print(80 * '=')
# Send a start signal to the cluster of model servers and retrieve first parameter estimation
coeffs = {}
intercepts = {}
for k in range(n):
    ko = k + 1
    model_server_url = url_list[k]
    print('Initializing server url: ', model_server_url + "/start")
    res = requests.get(model_server_url + "/start")
    data = res.json()
    print('Server :', model_server_url, ' Estimates: ', res.json())
    coeffs[str(ko)] = data['coefficients']
    intercepts[str(ko)] = data['intercept']

# Get the shape of the coefficient vector from server 1 results
m = len(coeffs['1'])

print(80 * '=')
print('First Averaging')
print(80 * '=')
# Average the estimated parameters
avg_coef = np.zeros(m)
avg_intercept = 0.0
for l in range(m):
    for k in range(1, n):
        ko = k + 1
        avg_coef[l] += weights[str(ko)] * coeffs[str(ko)][l]
        avg_intercept += weights[str(ko)] * intercepts[str(ko)]
data = {'intercept': avg_intercept, 'coefficients': avg_coef.tolist()}
print('Averaged Estimates: ', data)
print(80 * '=')

# Loop over the desired number of epochs
headers = {'Content-Type': 'application/json'}
for e in range(Epochs):
    # Send averaged parameters to all servers
    # Retrieve new estimates
    print('Epoch: ', e)
    print(80 * '-')
    for k in range(n):
        ko = k + 1
        model_server_url = url_list[k]
        res = requests.post(model_server_url + "/update", json=data, headers=headers)
        data = res.json()
        coeffs[str(ko)] = data['coefficients']
        intercepts[str(ko)] = data['intercept']
        print('Server :', model_server_url, ' Estimates: ', res.json())

    # Average the updated parameters
    avg_coef = np.zeros(m)
    avg_intercept = 0.0
    for l in range(m):
        for k in range(n):
            ko = k + 1
            avg_coef[l] += weights[str(ko)] * coeffs[str(ko)][l]
            avg_intercept += weights[str(ko)] * intercepts[str(ko)]
    data = {'intercept': avg_intercept, 'coefficients': avg_coef.tolist()}
    print('Averaged Estimates: ', data)

# print final estimate
# print('Final Estimate: ', data)
