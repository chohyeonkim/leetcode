class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # x -> record x
        # + -> record sum of previous 2 number
        # D -> record double previous 2
        # C -> invalidate previous score remove

        record = []

        for op in operations:

            if op in "+DC":

                previous_1 = record[-1]

                if op == "+":
                    previous_2 = record[-2]
                    new_record = previous_1 + previous_2
                    record.append(new_record)
                elif op == "D":
                    new_record = previous_1 * 2
                    record.append(new_record)
                else:
                    record.pop()

            else:
                record.append(int(op))

        return sum(record)
