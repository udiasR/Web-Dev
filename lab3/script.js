let cnt = 0;
let a = document.getElementById("counter-value")

let dec = document.getElementById("decrease-btn");
let inc = document.getElementById("increase-btn");
let res = document.getElementById("reset-btn");

function updateDisplay() {

}

function increase() {
    cnt+=1;
    a.innerHTML = cnt;
}

function decrease() {
    cnt-=1;
    a.textContent = cnt;
}

function reset () {
    cnt = 0;
    a.textContent = cnt;
}

dec.addEventListener("click", decrease);
inc.addEventListener("click", increase);
res.addEventListener("click", reset);