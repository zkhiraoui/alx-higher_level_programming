#!/usr/bin/node

// Specifies the path to the Node.js interpreter, indicating that the script should be executed with Node.js.

exports.nbOccurences = function (list, searchElement) {
  // Defines a function to count how many times a specific element appears in an array.

  let nOccurrences = 0; 
  // Initializes a counter to track the occurrences of the searchElement in the array.

  for (let i = 0; i < list.length; i++) {
    // Loops through each element of the array to compare with searchElement.
    if (searchElement === list[i]) {
      // Checks if the current element of the array matches the searchElement.
      nOccurrences++; // Increments the counter if a match is found.
    }
  }

  return nOccurrences; // Returns the total number of occurrences found.
};

