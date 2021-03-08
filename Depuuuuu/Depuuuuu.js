window.onload = function () {
    var perflop = document.querySelector(".perflop .contents");
    var flop = document.querySelector(".flop .contents");
    var turn = document.querySelector(".turn .contents");
    var river = document.querySelector(".river .contents");
    var compare = document.querySelector(".compare .contents");
    var icons = document.querySelector("#icons");
    var contents = document.querySelector(".contentsDisplay");
    var lis = document.querySelectorAll("ol");
    lis[0].onclick = function () {
        contents.innerHTML = perflop.innerHTML;
    }
    lis[1].onclick = function () {
        contents.innerHTML = flop.innerHTML;
    }
    lis[2].onclick = function () {
        contents.innerHTML = turn.innerHTML;
    }
    lis[3].onclick = function () {
        contents.innerHTML = river.innerHTML;
    }
    lis[4].onclick = function () {
        contents.innerHTML = compare.innerHTML;
    }
    icons.onclick = function () {
        contents.innerHTML = "<p>Welcome to Depuuuuu</p>";
    }

}

