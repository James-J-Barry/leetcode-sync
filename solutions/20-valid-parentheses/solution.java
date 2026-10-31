class Solution {
    public boolean isValid(String s) {

        char[] charArray = s.toCharArray();
        
        Stack<Character> p = new Stack<>();

        for (char a : charArray){
            if (a == '('){
                p.push('(');
            } else if (a == ')'){
                if (p.isEmpty() || p.pop() != '('){
                    return false;
                }
            } else if (a == '['){
                p.push('[');
            } else if (a == ']'){
                if (p.isEmpty() || p.pop() != '['){
                    return false;
                }
            } else if (a == '{'){
                p.push('{');
            } else if (a == '}'){
                if (p.isEmpty() || p.pop() != '{'){
                    return false;
                }
            }
        }
        return (p.isEmpty());
    }
}