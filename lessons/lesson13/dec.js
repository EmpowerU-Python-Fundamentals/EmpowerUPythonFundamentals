function dec(fn) {
    return function(...args) {
        console.log("start run");
        const result = fn.apply(this, args);
        console.log("end run");
        return result;
    }
}



add = function(a, b) {
    return a+b;
}
add = dec(add)
add(1,2)
add(10, 20)

