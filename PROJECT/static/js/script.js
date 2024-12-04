// Message to be displayed
const msg = "The road ahead may be unknown, but the destination is within your control. Keep your eyes fixed on the horizon and move forward with purpose."; 
    
// See commented version below for more info 
let i = 0; 
let delay = 50; 

function typeWriter() { 
if (i < msg.length) { 
    document.getElementById("message").innerHTML += msg.charAt(i); 
    i++; 
    setTimeout(typeWriter, delay); 
}
}
typeWriter(); 

// COMMENTED VERSION
/*

let i = 0; // This is the character the function will be looking at each time it runs, or each iteration
let delay = 50; // Time in milliseconds that the timer will wait before executing the function on each iteration

function typeWriter() { //name the function
if (i < msg.length) { //this tells the function to run until it reaches the full length of the message, but not after
    document.getElementById("message").innerHTML += msg.charAt(i); //tells the function to grab each individual character in the message and add it to the output
    i++; //moves the count of the iteration, or character, forward by 1
    setTimeout(typeWriter, delay); //method to set a timer for each execution/iteration of the function
}
}
typeWriter(); //Calling the function here starts the animation without delay

*/