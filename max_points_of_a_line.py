# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

import itertools
import collections
import fractions

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        n = len(points)
        if n == 0:
            return 0
        if n == 1:
            return 1
        N_max = 0
        print(n)
        for i in range(n):
            print(i)
            p1 = points[i]
            n_max = 1
            lines = collections.defaultdict(list)
            dup = 0

            for j in range(i+1, n):
                p2 = points[j]
                dx = p1.x - p2.x
                dy = p1.y - p2.y
                if dx == 0 and dy == 0:
                    dup += 1
                    continue
                g = self.gcd(dx, dy)
                if g != 0:
                    dx = dx/g
                    dy = dy/g
                key = (dx, dy)
                if p1 not in lines[key]:
                    lines[key].append(p1)
                if p2 not in lines[key]:
                    lines[key].append(p2)
            for points in lines.values():
                n = len(points)
                if n > n_max:
                    n_max = n
            n_max += dup
            if N_max < n_max:
                N_max = n_max
        return N_max

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

p = [(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)]
p = [(-4,-4),(-8,-582),(-3,3),(-9,-651),(9,591)]
points = [Point(a, b) for a, b in p]

solution = Solution()
print(solution.maxPoints(points))
