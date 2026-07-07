"""
Shortest path

Giving a string list with elements for the length of nodes at first index telling how many nodes in the list, and
followed with connections that from node to node.

Find the shortest path for started from the first node and ended to the last node.

Example 1:
input: ["4", "A", "B", "C", "D", "A-B", "A-C", "B-C", "C-D"]
output: "A-C-D"

"""

from typing import List

class Solution:
    def shortestPath(self, strArr: List[str]) -> str:
        # prepare data
        nodeNum = int(strArr[0])
        nodes = strArr[1:nodeNum+1]
        paths = strArr[nodeNum + 1:]
        pathSet = set(paths)

        # nodes from where to where
        fm = nodes[0]
        to = nodes[-1]

        # Calcualte shortest path ####################

        # Definition
        dist={}
        dist_copy={}
        prev={}

        # Initiation
        dist[fm] = 0
        prev[fm] = -1

        # O(n^2)
        for node_fm in nodes:
            for node_to in nodes:
                if node_fm == node_to:
                    dist_copy[node_fm] = dist[node_fm]
                else:
                    path = '-'.join([node_fm, node_to])
                    if path in pathSet:
                        sum_dist = 1 + dist_copy[node_fm]
                        if node_to not in dist or dist[node_to] > sum_dist:
                            dist[node_to] = 1 + dist_copy[node_fm]
                            prev[node_to] = node_fm

                            print(f"{path} in {pathSet}, node_fm={node_fm}, node_to={node_to}"
                                  f", dist[{node_to}]={dist[node_to]}"
                                  f", dist_copy[{node_fm}]={dist_copy[node_fm]}")

        # Display the table
        print(f"Vertex\tdist\tdist_copy\tPrev")
        for node in nodes:
            print(f"{node}\t\t{dist[node]}\t\t{dist_copy[node]}\t\t\t{prev[node]}")

        # Generate the shortest path string
        res = []
        node = to
        res.append(node)
        while node in prev:
            val = prev[node]
            if val == -1:
                break
            res.insert(0, val)
            node = val

        output = "-".join(res)
        print(f"output={output}")

        return output

    