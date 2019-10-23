let div = document.querySelector("div > div");
let form = document.querySelector("div > form")
let button = document.querySelector("input[type='submit']");

function Desaparecer(){
    form.classList.add("desaparecer");
    div.classList.add("aparecer");
}

button.onclick = Desaparecer;