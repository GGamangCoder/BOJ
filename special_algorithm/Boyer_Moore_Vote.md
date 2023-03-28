## Boyer-Moore 과반수 투표 알고리즘(Majority Vote Algorithm)
> 스트리밍 알고리즘(straming algorithm)

[참고 문서](https://sgc109.github.io/2020/11/30/boyer-moore-majority-vote-algorithm/)


### 소스 코드  

```py
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        major = nums[0]
        for i in range(1,len(nums)):
            if count == 0 :
                major = nums[i]
                count = 1
            elif nums[i] == major : 
                count += 1
            else : 
                count -= 1
        return major
```  