class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {

        HashSet<Integer> unPaired = new HashSet<Integer>();
        int n = A.length;
        int[] C = new int[n];
        int currCom = 0;

        for (int i = 0; i < n; i++){

            if (unPaired.contains(A[i])){
                currCom++;
            } else {
                unPaired.add(A[i]);
            }
            if (unPaired.contains(B[i])){
                currCom++;
            } else {
                unPaired.add(B[i]);
            }
            C[i] = currCom;
        }
        return C;
    }
}