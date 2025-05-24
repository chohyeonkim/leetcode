class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        res = []

        for a in asteroids:

            while res and res[-1] > 0 and a < 0:
                top = res[-1]
                if top < -a:
                    res.pop()
                    continue
                if top == -a:
                    res.pop()
                    break
                else:
                    break  # when pos > -a

            else:
                res.append(a)

        return res
