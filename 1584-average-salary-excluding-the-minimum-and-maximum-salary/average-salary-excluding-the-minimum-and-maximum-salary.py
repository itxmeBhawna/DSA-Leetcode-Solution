class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal = max(salary)
        min_sal = min(salary)
        total = sum(salary)
        count = len(salary)
        remain = total - max_sal -min_sal
        re_count = count - 2
        return remain / re_count
        