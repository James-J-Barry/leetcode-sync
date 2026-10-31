class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        // iterate over words and create a new arrayList of all of the 
        // indecies of vowel words
        Set<Character> vowels = new HashSet<Character>();
        vowels.addAll(Arrays.asList('a','e','i','o','u'));

        ArrayList<Integer> temp = new ArrayList<Integer>();
        for (int i = 0; i < words.length; i++){
            if (vowels.contains(words[i].charAt(0)) 
            && vowels.contains(words[i].charAt(words[i].length() - 1))){
                temp.add(i);
            }
        }

        // transfer indecies to indexible array
        int[] vowelInds = new int[temp.size()];
        for (int i = 0; i < temp.size(); i++){
            vowelInds[i] = temp.get(i);
        }

        // actually get answers using binary search
        int[] answers = new int[queries.length];
        for (int i = 0; i < queries.length; i++){
            answers[i] = binarySearch(vowelInds, queries[i][1], true) 
                        -  binarySearch(vowelInds, queries[i][0], false) + 1;
        }
        return answers;
    }


    private int binarySearch(int arr[], int x, boolean upper) {
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;

            // Check if x is present at mid
            if (arr[mid] == x)
                return mid;

            // If x greater, ignore left half
            if (arr[mid] < x)
                low = mid + 1;

            // If x is smaller, ignore right half
            else
                high = mid - 1;
        }

        // If we reach here, then element was
        // not present - return next highest
        return upper ? low - 1 : low;
    }
}