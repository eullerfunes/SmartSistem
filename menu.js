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

sr.reveal('.menu-desktop, .EF-contato, .titulo, .img-topo-site, .btn-abrir-menu, .menu-mobile, .txt-topo-site, .especialidades, .interface, .titulo, .flex, .especialidades-box, .sobre, .portfolio, .formulario, .interface', {duration:1000});
