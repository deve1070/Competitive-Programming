class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path=[]
        for log in logs:
            if log=='./':
                continue
            elif log=='../':
                if  path:
                    path.pop()
                else:
                    continue
            else:
                path.append(log)
        print(path)
        return len(path)