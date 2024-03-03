class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        count=0
        for i, c in enumerate(operations):
            if c == "C" or c == "c":
                if score:
                    prev = score[count-1]
                    score.remove(prev)
                    count -= 1
            elif c == "D" or c == "d":
                if score:
                    prev = score[-1]
                    score.append(prev*2)
                    count += 1
            elif c == "+":
                if len(score) >= 2:
                    p1 = score[count-1]
                    p2 = score[count-2]
                    score.append(p1+p2)
                    count += 1
            else:
                score.append(int(c))
                count += 1

        return sum(score)