import string
def solution(name):    
    alpha_dict = {a:min(i, abs(26-i)) for i, a in enumerate(string.ascii_uppercase)}
    L = len(name)
    
    nums = [alpha_dict[s] for s in name]
    
    idx = 0
    r_idx = 1
    l_idx = -1
    
    ans = nums[idx]
    nums[idx] = 0
    
    while sum(nums) > 0:
        while True:
            ans += 1
            
            if nums[r_idx] != 0:
                idx = r_idx
                break
            r_idx = (r_idx+1)%L
            
            if nums[l_idx] != 0:
                idx = l_idx
                break
            l_idx = (l_idx-1)%L
        
        r_idx = (idx+1)%L
        l_idx = (idx-1)%L
        ans += nums[idx]
        nums[idx] = 0
        
    return ans