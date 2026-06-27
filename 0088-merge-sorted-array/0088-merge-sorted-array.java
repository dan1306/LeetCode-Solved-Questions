
import java.util.Arrays;
class Solution {
    public int[] merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m;
        int j = 0;
        while(i < nums1.length && j < n){  
            nums1[i] = nums2[j];
            i++;
            j++;
        }
        // System.out.println(Arrays.toString(nums1)); 
        int[] temp = mergeSort(nums1);
        // System.out.println(Arrays.toString(nums1)); 
        // return nums1;
        for(int k = 0; k < nums1.length; k++){
            nums1[k] = temp[k];
        }

        return nums1;
       
    }

  public static int[] mergeSort(int arr[]){
    
    if (arr.length < 2) return arr;
    
    int mid = arr.length/2;
    int[] subLeft = mergeSort(Arrays.copyOfRange(arr, 0, mid));
    int[] subRight = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));
    
    return merge(subLeft, subRight);
      
  }
  
  public static int[] merge(int[] arr1, int[] arr2){
      
      int firstArr = 0;
      int secArr = 0;
      int[] newArr = new int[arr1.length + arr2.length];
      int index = 0;
      
      while(firstArr < arr1.length && secArr < arr2.length){
          if(arr1[firstArr] < arr2[secArr]){
              newArr[index] = arr1[firstArr];
              firstArr++;
              index++;
          }else{
              newArr[index] = arr2[secArr];
              secArr++;
              index++;
          }
      }
      
      while(firstArr < arr1.length){
      newArr[index] = arr1[firstArr];
      firstArr++;
      index++;;
      }
      
      while(secArr < arr2.length){
        newArr[index] = arr2[secArr];
        secArr++;
        index++;
      }
      
      
      return newArr;
  }
    
}