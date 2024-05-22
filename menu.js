let btnMenu = document.getElementById('btn-menu')
let menu = document.getElementById('menu-mobile')
let overlay = document.getElementById('overlay-menu')



btnMenu.addEventListener("click", ()=>{
    menu.classList.add('abrir-menu')
})


menu.addEventListener("click", ()=>{
    menu.classList.remove('abrir-menu')
})

overlay.addEventListener("click", ()=>{
    menu.classList.remove('abrir-menu')
})

window.sr = ScrollReveal({ reset: true});

sr.reveal('.menu-desktop, .EF-contato, .img-topo-site, .btn-abrir-menu, .menu-mobile, .txt-topo-site, .especialidades, .titulo, .flex, .especialidades-box, .sobre, .portfolio, .formulario', {duration:1000});

sr.reveal('.interface, .titulo,',{
    rotate: { x:0, y:80, z:0},
    duration:2000
})