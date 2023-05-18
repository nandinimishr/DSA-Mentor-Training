class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        wstart=0
        s=0
        wend=0
        ans=0
        while wend<N:
            s+=Arr[wend]
            if(wend-wstart+1==K):
                ans=max(ans,s)
                s-=Arr[wstart]
                wstart+=1
            wend+=1    
        return ans    
            
