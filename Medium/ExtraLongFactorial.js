'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

function extraLongFactorials(n) {
    // Write your code here
    let fact = BigInt(n);
    if (n<0 && n>100) return;
    for (let i = n - 1; i > 1; i--){
        fact *= BigInt(i);
    }
    console.log(fact.toString());
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    extraLongFactorials(n);
}
