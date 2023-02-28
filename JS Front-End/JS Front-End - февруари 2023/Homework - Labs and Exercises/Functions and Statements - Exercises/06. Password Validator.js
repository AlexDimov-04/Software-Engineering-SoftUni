function passwordValidator(password) {
    let invalid = false;

    if (!invalid) {
        if (!(password.length >= 6 && password.length <= 10)) {
            console.log("Password must be between 6 and 10 characters");
            invalid = true;
        }
        if (!/^[a-zA-z0-9]+$/.test(password)) {
            console.log("Password must consist only of letters and digits");
            invalid = true;
        }
        if (!/\d.*\d/.test(password)) {
            console.log("Password must have at least 2 digits");
            invalid = true;
        }
    } 
    
    if (!invalid) {
        console.log("Password is valid");
    }

}