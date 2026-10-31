class ProductOfNumbers {
    private class Node {
        int val;
        Node next;

        private Node(int v, Node n){
            val = v;
            next = n;
        }
    }
    private Node head;
    public ProductOfNumbers() {
        head = null;
    }
    
    public void add(int num) {
        Node n = new Node(num, head);
        head = n;
    }
    
    public int getProduct(int k) {
        if(k == 0){
            return 0;
        }
        int sum = 1;
        Node point = head;
        for (int i = 0; i < k; i++){
            sum *= point.val;
            point = point.next;
        }
        return sum;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */