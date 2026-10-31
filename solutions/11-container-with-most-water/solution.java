class Solution {
    public int maxArea(int[] height) {
        int n = height.length;
        int i=0,j=n-1,sum=0,max=0;
        while(i<j){
            sum=(Math.min(height[i],height[j]))*(j-i);
            if(max<sum){
                max=sum;
            }
            if(height[i]<height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return max;
    }
}