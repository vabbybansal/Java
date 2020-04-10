# DP
# Learning : Use Djikstra's simply using heap



# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.


# class Solution(object):
#     def networkDelayTime(self, times, N, K):
#         """
#         :type times: List[List[int]]
#         :type N: int
#         :type K: int
#         :rtype: int
#         """
#
#         # Hash map to store min time of signal incoming at a particular node
#         incomingTimeMap = dict()
#
#         # Convert times to hash_map
#         navMap = dict()
#         incomingNodeSet = set()
#
#         for directedEdge in times:
#             tempSource = directedEdge[0]
#             tempDest = directedEdge[1]
#             tempTime = directedEdge[2]
#
#             if tempDest != K:
#                 incomingNodeSet.add(tempDest)
#
#             if tempSource not in navMap:
#                 navMap[tempSource] = []
#             navMap[tempSource].append({
#                 'name': tempDest,
#                 'time': tempTime
#             })
#
#         # Quick check to see if all the nodes have some incoming edge apart from the source node. If not, return -1 right away
#         if len(incomingNodeSet) != N-1:
#             return -1
#
#         def nav(node, sumTime, path):
#
#             # Check feasibility (a node should not repeat - cycle)
#             if node in path:
#                 return
#             else:
#                 path.add(node)
#
#             # Log time. If some time already exists for the node, then the updated time should be the min time reaching at the node
#             if node not in incomingTimeMap:
#                 incomingTimeMap[node] = sumTime
#             else:
#                 incomingTimeMap[node] = min(sumTime, incomingTimeMap[node])
#
#             # Navigate further
#             if node in navMap:
#                 for destNode in navMap[node]:
#                     nav(
#                         destNode['name'],
#                         destNode['time'] + sumTime,
#                         set(path)
#                     )
#
#         # Start navigation
#         nav(K, 0, set())
#
#         # Signal does not reach all nodes
#         if len(incomingTimeMap)-1 != N-1:
#             return -1
#         else:
#             return max(incomingTimeMap.values())



# class Solution(object):
#     def networkDelayTime(self, times, N, K):
#         """
#         :type times: List[List[int]]
#         :type N: int
#         :type K: int
#         :rtype: int
#         """
#         # Hash map to store min time of signal incoming at a particular node
#         # incomingTimeMap = dict()
#
#         # Convert times to hash_map
#         destSourceMap = dict()
#         # times = dict()
#         # incomingNodeSet = set()
#
#         for directedEdge in times:
#             tempSource = directedEdge[0]
#             tempDest = directedEdge[1]
#             tempTime = directedEdge[2]
#
#             if tempDest == K:
#                 continue
#
#             if tempDest not in destSourceMap:
#                 destSourceMap[tempDest] = []
#             destSourceMap[tempDest].append({
#                 'name': tempSource,
#                 'time': tempTime
#             })
#
#         if len(destSourceMap) != N-1:
#             return -1
#
#         MEM_MIN_TIMES = dict()
#         MEM_MIN_TIMES[K] = 0
#
#         def nodeMinTime(node, path):
#
#             # if min for node already calculated, return the calculated value
#             if node in MEM_MIN_TIMES:
#                 return MEM_MIN_TIMES[node]
#
#             # To calculate the min for the node, minValue = MIN(all paths possible)
#             tempList = []
#             if node in destSourceMap:
#                 for sourceDetails in destSourceMap[node]:
#
#                     # Check if the same node is not already present to stop cycles
#                     if sourceDetails['name'] not in path:
#                         newPath = set(path)
#                         newPath.add(sourceDetails['name'])
#
#                         tempList.append(
#                             sourceDetails['time'] + nodeMinTime(
#                                                         sourceDetails['name'],
#                                                         newPath
#                                                     )
#                         )
#                 MEM_MIN_TIMES[node] = min(tempList)
#                 return MEM_MIN_TIMES[node]
#             else:
#                 return 0
#
#
#         # Iterate for all dest
#         for dest in destSourceMap:
#             tempSet = set()
#             tempSet.add(dest)
#             MEM_MIN_TIMES[dest] = nodeMinTime(dest, tempSet)
#
#         return max(MEM_MIN_TIMES.values())


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        import heapq
        infinity = 99999999999

        # Heap for storing minTimes
        myHeapQ = [(0, K)]

        # Set for storing nodes min-founded
        dictSeen = dict()

        # Set for storing node yet to be min-founded
        setUnseen = set()

        # initialize setUnseen
        sourceDestMap = {}
        for directedEdge in times:
            tempSource = directedEdge[0]
            tempDest = directedEdge[1]
            tempTime = directedEdge[2]

            setUnseen.add(tempSource)
            setUnseen.add(tempDest)

            if tempDest == K:
                continue

            if tempSource not in sourceDestMap:
                sourceDestMap[tempSource] = []
            sourceDestMap[tempSource].append({
                'name': tempDest,
                'time': tempTime
            })

        # Initialize minHeap with infinity values for all nodes except source node which gets 0
        # for node in setUnseen:
        #     if node != K:
        #         heapq.heappush(myHeapQ, (infinity, node))

        # Start Djikstra's
        while myHeapQ:
            distance, node = heapq.heappop(myHeapQ)

            if node in dictSeen:
                continue

            # The node above has been seen
            dictSeen[node] = distance

            # Propogate / Relax the node's edges
            if node in sourceDestMap:
                for edge in sourceDestMap[node]:
                    if edge['name'] not in dictSeen:
                        heapq.heappush(myHeapQ, (distance + edge['time'], edge['name']))


        if len(dictSeen) == N:
            return max(dictSeen.values())
        else:
            return -1



obj = Solution()
print obj.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
# print obj.networkDelayTime([[1,3,0],[1,2,0],[2,1,1],[2,3,59],[3,1,36],[3,2,98]], 3, 2)
# print obj.networkDelayTime([[1,2,1],[2,1,3]], 2, 2)

