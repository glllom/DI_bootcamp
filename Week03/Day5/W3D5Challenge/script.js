/*
 * Stars
 */
let stars = "";

for (let count = 0; count < 6; count++) {
    stars += '* ';
    console.log(stars);
}

for (let count = 0; count < 6; count++) {
    stars = "";
    for (let starsCount = 0; starsCount <= count; starsCount++) {
        stars += '* ';
    }
    console.log(stars);
}

/*
 * Bubble sort
 */
const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];
console.log(numbers.toString());
console.log(numbers.join(','));
myBubbleSort(numbers);
console.log("sorted: ", numbers.join(','));

function myBubbleSort(arr) {
    let temp;
    for (let count1 = 0; count1 < arr.length; count1++)
        for (let count2 = count1; count2 < arr.length; count2++)
            if (arr[count1] < arr[count2]) {
                temp = arr[count1];
                arr[count1] = arr[count2];
                arr[count2] = temp;
            }
}

