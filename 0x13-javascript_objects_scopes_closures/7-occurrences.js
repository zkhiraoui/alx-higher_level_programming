#!/usr/bin/node

// Specifies the path to the Node.js interpreter for the script execution.

exports.nbOccurences = function (list, searchElement) {
  // Function to count occurrences of searchElement in the list.
  
  let count = 0; 
// Initialize count to keep track of the occurrences.

  for (let i = 0; i < list.length; i++) {
    // Iterate over each element in the list to check for matches.
    if (list[i] === searchElement) {
      // If the current element matches the searchElement,
      count++; 
      // increment the count.
    }
  }

  return count; 
// Return the total number of occurrences found.
};
