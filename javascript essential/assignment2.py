<!-- 
Question 1
What is the value of clothes[0] and why?
const clothes = ['jacket', 't-shirt'];
clothes.length = 0;
console.log(clothes[0]);
-->
clothes[0] will return undefined, cause clothes.length = 0
makse clothes an empty array

<!--Question 2
Write a Javascript program to find the sum of all elements of a given array?
-->
function sum(array){
  var sum = 0
    for(i = 0; i < array.length; i++){
    sum = sum + array[i];
  }
}
arr = [1,2,3];
result = sum(arr);
