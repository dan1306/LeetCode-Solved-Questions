import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] recoverOrder(int[] order, int[] friends) {
        // String[] array = {"apple", "banana", "apple", "orange"};


        Set<Integer> set = Arrays.stream(friends)
                         .boxed()
                         .collect(Collectors.toSet());
        int[] returnArr = new int[friends.length];
        int j = 0;

        for(int i = 0; i < order.length; i++) {
            if(set.contains(order[i])){
                returnArr[j] = order[i];
                j++;
            }
        }
        return returnArr;
    }
}