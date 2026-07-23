import java.util.ArrayList;

class Solution {
    public int i;
    public List<List<Integer>> dynamic2D;
    public  List<Integer> subsetArr;
    public int[] n;

    public List<List<Integer>> subsets(int[] nums) {
        this.dynamic2D = new ArrayList<>();
        this.i = 0;
        this.subsetArr =  new ArrayList<>();
        this.n = nums;
        reccursiveSolution(0);
        return dynamic2D;
    }
    public void reccursiveSolution(int i){
        if(i >= this.n.length){
            this.dynamic2D.add(new ArrayList<>(this.subsetArr));
            return;
        }

        this.subsetArr.add(this.n[i]);
        reccursiveSolution(i + 1);

        this.subsetArr.remove(this.subsetArr.size() - 1);
        reccursiveSolution(i + 1);
        

    }
}