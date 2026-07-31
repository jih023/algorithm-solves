class Solution(object):
    def minimumPushes(self, word):
        arr = [0] * 26
        for w in word:
            arr[ord(w) - 97] += 1
        
        arr.sort(reverse=True)

        idx, cnt, num, result = 0, 8, 1, 0
        while idx < 26 and arr[idx]:
            if not cnt:
                cnt = 8
                num += 1
            result += arr[idx] * num
            idx += 1
            cnt -= 1
        
        return result
            