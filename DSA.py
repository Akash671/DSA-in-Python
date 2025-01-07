# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:19:01 2024

@author: akash
"""


import math
class Solution:
    
    
    #Count pairs is sum is equal to target in array
     def countPairs (self, arr, target) : 
        #Complete the function
        
        pair_count=0
        pair_map={}
        
        for num1 in arr:
            num2=target-num1
            if num2 in pair_map:
                pair_count+=pair_map[num2]
            #now er need to update the num in dictionary
            
            if num1 in pair_map:
                pair_map[num1]+=1
            else:
                pair_map[num1]=1
        return pair_count
   
    #count those subarry have sum equal to target k
    def countSubarrays(self, arr, k):
       
        """
        n=len(arr)
        ans=[]
        c=0
        for i in range(n):
            for j in range(i,n):
                ans.append(arr[i:j])
                if sum(arr[i:j+1])==k:
                    c+=1
        #print(ans)
        return c
        """
        
        hash_map={0:1}
        n=len(arr)
        c=0
        sum_subarr=0
        for i in range(n):
            sum_subarr+=arr[i]
            if sum_subarr-k in hash_map:
                #print(hash_map[sum_subarr-k])
                c+=hash_map[sum_subarr-k]
            
            if sum_subarr in hash_map:
                hash_map[sum_subarr]+=1
            else:
                 hash_map[sum_subarr]=1
            print(hash_map)
        return c
    #Count Subarrays that have xor equal to K
    def subarrayXor(self, arr, k):
        # code here
        """
        def xor(a):
            xor_result = 0
            for x in a:
                xor_result ^= x
            return xor_result
        ans=0
        n=len(arr)
        for i in range(n):
            for j in range(i,n+1):
                a=arr[i:j]
                if len(a)!=0:
                    #print(a)
                    subarr_xor=xor(a)
                    if subarr_xor==k:
                        ans+=1
        return ans
        """
        
        
        n=len(arr)
        xor_sum=0
        xor_map={0:1}
        
        ans=0
        
        for i in range(n):
            xor_sum^=arr[i]
            
            if xor_sum^k in xor_map:
                ans+=xor_map[xor_sum^k]
            
            if xor_sum in xor_map:
                xor_map[xor_sum]+=1
            else:
                xor_map[xor_sum]=1
        return ans
        
    #Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target.
    def countPairs(self, arr, target):
        #Your code here
        
        
        """
        n=len(arr)
        pair_count=0
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[i]+arr[j]<target:
                    pair_count+=1
        return pair_count
        """
        
        #optimize solution
        
        arr=sorted(arr)
        left_ptr=0
        right_ptr=len(arr)-1

        count_pairs=0
        while(left_ptr<right_ptr):
          if arr[left_ptr]+arr[right_ptr]<target:
              count_pairs+=len(arr[left_ptr:right_ptr])
              left_ptr+=1
          else:
              right_ptr-=1
        return count_pairs
        


 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        #print(ob.countPairs(A, k))
        print(ob.countSubarrays(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()


