int numberOfEmployeesWhoMetTarget(int* hours, int hoursSize, int target) {
    int i = 0;
    for(int j = 0; j < hoursSize; j++){
        if(hours[j] >= target) i++;
    }

    return i;
}