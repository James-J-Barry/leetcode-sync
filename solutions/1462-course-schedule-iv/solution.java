class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        boolean[][] isReachable = new boolean[numCourses][numCourses];

        for (int[] pre : prerequisites){
            isReachable[pre[1]][pre[0]] = true;
        }

        for (int i = 0; i < numCourses; i++){
            Queue<Integer> q = new LinkedList<>();
            boolean[] visited = new boolean[numCourses];

            visited[i] = true;
            q.add(i);

            while (!q.isEmpty()) {
          
                int curr = q.poll();
                isReachable[i][curr] = true;
                
                for (int x = 0; x < numCourses; x++) {
                    if (isReachable[curr][x]){
                        if (!visited[x]) {
                            visited[x] = true;
                            q.add(x);
                        }
                    }
                }
            }
        }

        ArrayList<Boolean> answers = new ArrayList<Boolean>();
        for (int i = 0; i < queries.length; i++){
            if (isReachable[queries[i][1]][queries[i][0]]){
                answers.add(true);
            } else {
                answers.add(false);
            }
        }
        return answers;
    }
    /*
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        HashMap<Integer, HashSet<Integer>> pres = new HashMap<Integer, HashSet<Integer>>();
        for (int[] pre : prerequisites){
            if (pres.containsKey(pre[1])){
                pres.get(pre[1]).add(pre[0]);
            } else {
                HashSet<Integer> add = new HashSet<Integer>();
                add.add(pre[0]);
                pres.put(pre[1], add);
            }
        }
        int n = queries.length;
        ArrayList<Boolean> answer = new ArrayList<Boolean>();
        for (int i = 0; i < n; i++){
            int looking = queries[i][0];
            int current = queries[i][1];
            if (findRec(looking, current, pres)){
                answer.add(true);
            } else {
                answer.add(false);
            }
        }
        return answer;
    }
    private boolean findRec(int looking, int current, HashMap<Integer, HashSet<Integer>> pres){
        boolean toReturn = false;
        if (pres.containsKey(current)){
            if (pres.get(current).contains(looking)){
                return true;
            } else {
                for (Integer i : pres.get(current)){
                    if (findRec(looking, i, pres)){
                        toReturn = true;
                    }
                }
            }
        }
        return toReturn;
    }
    */
}