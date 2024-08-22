document.getElementById(`calcular`).addEventListener(`click`, calcular)

function calcular(){
    let a = parseFloat(document.getElementById(`a`).value)
    let b = parseFloat(document.getElementById(`b`).value)
    document.getElementById(`resultado`).innerText = a*b
}