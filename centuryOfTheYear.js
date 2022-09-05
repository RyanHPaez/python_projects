function solution(year) {
 let solution = 0;
 while (year > 0){
     year = year - 100;
     solution = solution +1;
 }
 return solution
}
