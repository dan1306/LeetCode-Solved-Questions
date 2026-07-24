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
        reccursiveSolution(0, 0);
        return dynamic2D;
    }

    public int reccursiveSolution(int i, int sum){
        // sum+= this.n[i];
        if(i >= this.n.length || sum >= this.t){
            if(sum == this.t){
                this.dynamic2D.add(new ArrayList<>(this.subsetArr));
            }
            return sum;
        }

        this.subsetArr.add(this.n[i]);
        sum+= this.n[i];
        sum = reccursiveSolution(i, sum) - this.n[i];
        if(this.subsetArr.size() > 0){
            this.subsetArr.remove(this.subsetArr.size() - 1);
        }
        // reccursiveSolution(i + 1, sum);

        // if (this.subsetArr.size() > 0) {
        //     this.subsetArr.remove(this.subsetArr.size() - 1);
        // }
        // this.subsetArr.remove(this.subsetArr.size() - 1);
        return reccursiveSolution(i + 1, sum);
        

    }

}
