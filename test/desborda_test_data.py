#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# This file is part of agora-results.
# Copyright (C) 2017  Agora Voting SL <agora@agoravoting.com>

# agora-results is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License.

# agora-results  is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with agora-results.  If not, see <http://www.gnu.org/licenses/>.

test_desborda_1 = {
"input":
"""A1f,A2m,A3f,A4m,A5f,A6m,A7f,A8m,A9f,A10m,A11f,A12m,A13f,A14m,A15f,A16m,A17f,A18m,A19f,A20m,A21f,A22m,A23f,A24m,A25f,A26m,A27f,A28m,A29f,A30m,A31f,A32m,A33f,A34m,A35f,A36m,A37f,A38m,A39f,A40m,A41f,A42m,A43f,A44m,A45f,A46m,A47f,A48m,A49f,A50m,A51f,A52m,A53f,A54m,A55f,A56m,A57f,A58m,A59f,A60m,A61f,A62m
A1f,A2m,A3f,A4m,A5f,A6m,A7f,A8m,A9f,A10m,A11f,A12m,A13f,A14m,A15f,A16m,A17f,A18m,A19f,A20m,A21f,A22m,A23f,A24m,A25f,A26m,A27f,A28m,A29f,A30m,A31f,A32m,A33f,A34m,A35f,A36m,A37f,A38m,A39f,A40m,A41f,A42m,A43f,A44m,A45f,A46m,A47f,A48m,A49f,A50m,A51f,A52m,A53f,A54m,A55f,A56m,A57f,A58m,A59f,A60m,A61f,A62m
B1f,B2m,B3f,B4m,B5f,B6m,B7f,B8m,B9f,B10m,B11f,B12m,B13f,B14m,B15f,B16m,B17f,B18m,B19f,B20m,B21f,B22m,B23f,B24m,B25f,B26m,B27f,B28m,B29f,B30m,B31f,B32m,B33f,B34m,B35f,B36m,B37f,B38m,B39f,B40m,B41f,B42m,B43f,B44m,B45f,B46m,B47f,B48m,B49f,B50m,B51f,B52m,B53f,B54m,B55f,B56m,B57f,B58m,B59f,B60m,B61f,B62m
""",
"config": """[
    [
        "agora_results.pipes.results.do_tallies",
        {
            "ignore_invalid_votes": true
        }
    ],
    [
        "agora_results.pipes.desborda.podemos_desborda",
        {
            "women_names": [
            ]
        }
    ]
]""",
"output":
"""A1f, 160
A2m, 158
A3f, 156
A4m, 154
A5f, 152
A6m, 150
A7f, 148
A8m, 146
A9f, 144
A10m, 142
A11f, 140
A12m, 138
A13f, 136
A14m, 134
A15f, 132
A16m, 130
A17f, 128
A18m, 126
A19f, 124
A20m, 122
A21f, 120
A22m, 118
A23f, 116
A24m, 114
A25f, 112
A26m, 110
A27f, 108
A28m, 106
A29f, 104
A30m, 102
A31f, 100
A32m, 98
A33f, 96
A34m, 94
A35f, 92
A36m, 90
A37f, 88
A38m, 86
A39f, 84
A40m, 82
A41f, 80
B2m, 79
B1f, 80
A42m, 78
B3f, 78
B4m, 77
A43f, 76
B6m, 75
B5f, 76
A44m, 74
B7f, 74
B8m, 73
A45f, 72
B10m, 71
B9f, 72
A46m, 70
B11f, 70
B12m, 69
A47f, 68
B14m, 67
B13f, 68
A48m, 66
"""
}
 
