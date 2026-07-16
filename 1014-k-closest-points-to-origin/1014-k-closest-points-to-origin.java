import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Map<Integer, List<int[]>> map = new HashMap<>();
        Map<Integer, Integer> hit = new HashMap<>();
        int[] nums = new int[points.length];

        int a = 0;

        for(int i = 0; i < points.length; i++){
            nums[a] = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1]);
            map.putIfAbsent(nums[a], new ArrayList<>());
            map.get(nums[a]).add(points[i]);
            // map.put(nums[a], points[i]);
            hit.put(nums[a], 0);
            a+=1;
        }
        // System.out.println(Arrays.toString(nums));

        quickSort(0, nums.length - 1, nums);
        // System.out.println(map);
        int[][] returnArr = new int[k][2];
        int O = 0;
        

        for(int z = 0; z < k; z++){
            int innerIndex = hit.get(nums[z]);
            returnArr[O] = map.get(nums[z]).get(innerIndex);
            hit.put(nums[z], innerIndex + 1);
            O+=1;
        }

        return returnArr;
        
    }

    public static void quickSort(int startPoint, int endPoint, int[] nums){

        if(startPoint >= endPoint) return;
        int i = startPoint - 1;
        int j = startPoint;
        int pivot = endPoint;
        
        while(j < pivot){
            if(nums[j] <= nums[pivot]){
                i= i + 1;
                int temp  = nums[i];
                nums[i] = nums[j] ;
                nums[j] = temp;
            }
            j= j + 1;
        }
        i+=1;

        int temp = nums[i];
        nums[i] = nums[pivot];
        nums[pivot] = temp;

        quickSort(startPoint, i - 1, nums);
        quickSort(i + 1, j, nums);
    }
}