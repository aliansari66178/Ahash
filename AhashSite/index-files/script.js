function set (link) {
    document.getElementById("iframe").src = `index-files/data/${link}.html`;
}

document.getElementById("h").onclick = function () {
    set("h")
}
document.getElementById("a").onclick = function () {
    set("a")
}
document.getElementById("d").onclick = function () {
    set("d")
}
document.getElementById("u").onclick = function () {
    set("u")
}