console.log("Hello World!");

// Test function
function greetUser(name = "User") {
    return `Hello, ${name}! Welcome to the test file.`;
}

// Export for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { greetUser };
}

// Run the test
console.log(greetUser());
console.log(greetUser("Claude"));