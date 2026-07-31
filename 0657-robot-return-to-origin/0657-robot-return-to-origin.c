bool judgeCircle(char* moves) {
    int U = 0;
    int D = 0;
    int L = 0;
    int R = 0;

    int i = 0;
    while(moves[i] != '\0') {
        switch (moves[i]) {
            case 'U':
                U++;
                break;
            case 'D':
                D++;
                break;
            case 'L':
                L++;
                break;
            case 'R':
                R++;
                break;
            default:
                break;
                // code block
        }
        i++;
    }

    if( (U-D) == 0 && (L-R) == 0) {
        return true;
    }
    
    return false;
}