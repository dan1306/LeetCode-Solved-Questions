import java.util.ArrayList;

class Solution {
    public int i;
    public List<List<Integer>> dynamic2D;
    public  List<Integer> subsetArr;
    public int[] n;
    public int t;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.dynamic2D = new ArrayList<>();
        // this.i = 0;
        this.subsetArr =  new ArrayList<>();
        this.n = candidates;
        this.t = target;
        reccursiveSolution(0);
        return dynamic2D;
    }

    public void reccursiveSolution(int i){
        int ans = this.getArrSum(this.subsetArr);
        if(i >= this.n.length || ans >= this.t){
            if(ans == this.t && this.have(this.subsetArr) == false){
                this.dynamic2D.add(new ArrayList<>(this.subsetArr));
            }
            return;
        }

        this.subsetArr.add(this.n[i]);
        reccursiveSolution(i);
        // if (this.subsetArr.size() >= 2) {
        //     if (this.subsetArr.get(this.subsetArr.size() - 1).equals(this.subsetArr.get(this.subsetArr.size() - 2))) {
        //                 this.subsetArr.remove(this.subsetArr.size() - 1);
        //     }
        // }
        reccursiveSolution(i + 1);
        if (this.subsetArr.size() >= 1) {
            this.subsetArr.remove(this.subsetArr.size() - 1);
        }
        // this.subsetArr.remove(this.subsetArr.size() - 1);
        reccursiveSolution(i + 1);
        

    }

    public int getArrSum(List<Integer> arr){
        int n = 0;

        for(int i = 0; i < arr.size(); i++){
            n+= arr.get(i);
        }
        
        return n;
    }
    public boolean have(List<Integer> arr) {
        // This replaces your entire loop and behaves exactly the same way
        return this.dynamic2D.contains(arr);
    }
}

// }

// import java.util.ArrayList;

// class Solution {
//     public int i;
//     public List<List<Integer>> dynamic2D;
//     public  List<Integer> subsetArr;
//     public int[] n;

//     public List<List<Integer>> subsets(int[] nums) {
//         this.dynamic2D = new ArrayList<>();
//         this.i = 0;
//         this.subsetArr =  new ArrayList<>();
//         this.n = nums;
//         reccursiveSolution(0);
//         return dynamic2D;
//     }
//     public void reccursiveSolution(int i){
//         if(i >= this.n.length){
//             if(this.getArrSum(this.subsetArr) == );
//             this.getArrSum.add(new ArrayList<>(this.subsetArr));
//             return;
//         }

//         this.subsetArr.add(this.n[i]);
//         reccursiveSolution(i + 1);

//         this.subsetArr.remove(this.subsetArr.size() - 1);
//         reccursiveSolution(i + 1);
        

//     }
//     public int getArrSum(List<Integer> arr){
//         int n = 0;

//         for(int i = 0; i < arr.size(); i++){
//             n+= arr.get(i);
//         }
        
//         return n;
//     }
// }