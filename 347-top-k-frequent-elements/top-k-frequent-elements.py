import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        dic = {}
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
        for key, val in dic.items():
            heapq.heappush(heap, (-val, key))
        answer = []
        while len(answer) < k:
            answer.append(heapq.heappop(heap)[1])
        return answer
