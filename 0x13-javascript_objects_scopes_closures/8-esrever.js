#!/usr/bin/node

// Specifies the path to the Node.js interpreter, indicating that the script should be executed with Node.js.

exports.esrever = function (list) {
  // Defines a function to reverse the order of elements in an array.

  let len = list.length - 1; 
  // Initializes a variable to the last index of the array, to start swapping from the end.

  let i = 0; 
  // Initializes a variable to the first index of the array, to start swapping from the beginning.

  while ((len - i) > 0) {
    // Continues swapping elements until it reaches the middle of the array.
    const aux = list[len]; 
    // Stores the current last element in a temporary variable.

    list[len] = list[i]; 
    // Swaps the last element with the first element (or the element at the current beginning index).

    list[i] = aux; 
    // Places the previously last element (stored in aux) at the current beginning index.

    i++; 
    // Moves the beginning index towards the center of the array.

    len--; 
    // Moves the end index towards the center of the array.
  }

  return list; 
  // Returns the array after reversing its elements.
};
