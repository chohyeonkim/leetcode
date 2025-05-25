class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # position[i]
        # speed
        # target

        # can not pass / drive at the same speed (car1 car2)
        # car fleet non empty set  (same position same speed)

        # [1,4]  [3,2]
        # [4,6]
        # [7 8]
        # [10 10] -1

        # target/min(speed) * O(n)
        # [4,1,0,7] [2,2,1,1]
        # [6 3 1 8] check any of them reach target? O(n)
        # [8 5 2 9]  check any of them reach target? O(n)
        # [10 7 3 10] check any of them reach target? O(n) -> 10 , bind them as  car fleet
        # [10 9 4 10]
        # [10 11 5 10]

        # [4,1,0,7]
        # sorting X -> need to maintain order
        # [4,1,0,7]
        # [6 9 10 3] difference
        # [3 5 10 3] how many distinct number? = len(list)  = 3
        #
        # [1,4]
        # [9,6]
        # [3,3]

        # target=12
        # position=[10,8,0,5,3]
        #           12 12 1 6 6
        #                 2 7 9
        #                 3 8 8  # 앞차 추월을 못해서

        #          [2, 4 12 7 9]
        #          [1  1  12 7 3]
        # speed=[2,4,1,1,3]

        # [(10 1),(8 1), (0 12), (5 7),(3 3)]
        #  (10 1) (8 1) (5 7) (3 3) (0 12)
        #  [(10 1) (8 1) (3 3) (0 12)]
        # 0,4,2]
        # 2 5 5
        # 4 5 5
        # 6 6 6
        # 7 7 7
        # 2,1,3]

        position_speed = [
            (pos, (target - pos) / spd) for pos, spd in zip(position, speed)
        ]
        print(position_speed)

        cars = sorted(position_speed, key=lambda x: -x[0])
        print(cars)

        stack = []

        for car in cars:

            car_p, car_v = car

            if not stack:
                stack.append(car)
                continue

            while stack and stack[-1][1] >= car_v:
                car_v = stack[-1][1]
                stack.pop()

            stack.append((car_p, car_v))

        return len(stack)
