# Learning: for rectangle, you can think about thinking from diagonal points
# Used Hash Table -> Set for faster compute (get)

# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.
#
#
#
# Example 1:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2


class Solution(object):

    minArea = 99999999999
    memory = {}

    def createKeyTwoPoints(self, x1, y1, x2, y2):
        side1 = abs(x1-x2)
        side2 = abs(y1-y2)

        if side1 <= side2:
            return str(side1) + '_' + str(side2)
        else:
            return str(side2) + '_' + str(side1)

    def updateMinAreaDiagonal(self, x1,y1,x2,y2):
        return abs((x2-x1) * (y2-y1))


    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        self.minArea = 99999999999
        self.memory = {}
        pointX = {}
        pointY = {}
        for point in points:
            x = point[0]
            y = point[1]
            if x not in pointX:
                pointX[x] = set()
            if y not in pointY:
                pointY[y] = set()
            pointX[x].add(y)
            pointY[y].add(x)


        for x1 in pointX:
            for x2 in pointX:

                # Memorize later
                # --------------

                if x1 != x2:
                    # y1Set
                    y1Set = pointX[x1]
                    # y2Set
                    y2Set = pointX[x2]

                    # Iterate for all ys
                    for y1 in y1Set:
                        for y2 in y2Set:
                            # The current diagonal coordinates are (x1, y1), (x2,y2)

                            if y1 != y2:

                                # optimization: if area has already been calculated before
                                # memKey = self.createKeyTwoPoints(x1,y1,x2,y2)
                                # if memKey in self.memory:
                                #     continue

                                # optimization: even before looking whether the other two points exist, just check where the possible area would be less than current at all
                                if self.updateMinAreaDiagonal(x1, y1, x2, y2) < self.minArea:

                                    # Points needed for rectangle are - (x1, y2) and (x2, y1)
                                    if y2 in pointX[x1] and y1 in pointX[x2]:
                                        area = self.updateMinAreaDiagonal(x1, y1, x2, y2)
                                        # self.memory[memKey] = area
                                        if self.minArea > area:
                                            self.minArea = area


                            # Calculate only if less than current min
                            # ---------------------------------------

        if self.minArea == 99999999999:
            return 0
        else:
            return self.minArea



obj = Solution()
# print obj.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]])
# print obj.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])
print obj.minAreaRect([[0,1],[1,3],[3,3],[4,4],[1,4],[2,3],[1,0],[3,4]])
