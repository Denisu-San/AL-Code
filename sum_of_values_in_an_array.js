//sum of values in an array
// a = array
// like in python we initialize the value sum
// as a let variable since it changes throughout the course of the code
// and we as well do the += to keep adding for every iteration of the item within the array
// the for...of loop iterates through the array with every iteration with variable val of the array a
// or in other words iterating for every val of the parameter a

function sum_of_vals(a){
    let sum = 0
    for(let val of a){
        sum += val
    }
    return sum
}

console.log(sum_of_vals([2, 3, 67, 17, 21, 78, 81]))
console.log(sum_of_vals([]))