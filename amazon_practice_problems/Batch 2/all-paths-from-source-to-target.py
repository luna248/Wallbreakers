class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        retArr = []

        def dfs(curr_route, curr_node):
            if(curr_node == len(graph)-1):
                retArr.append(curr_route)

            for next_node in graph[curr_node]:
                dfs(curr_route + [next_node], next_node)

        for node in graph[0]:
            dfs([0]+[node], node)

        return retArr
