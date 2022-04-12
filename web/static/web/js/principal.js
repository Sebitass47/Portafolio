document.addEventListener('DOMContentLoaded', function(){

    up = () =>{
        window.scrollTo({top: 0,
            behavior: 'smooth'
        });
    }
    
    let animado = document.querySelectorAll('.animado');
    
    mostrarScroll = () =>{
       
        let scrollTop = document.documentElement.scrollTop;
    
        for (var i = 0; i < animado.length; i++) {
            let alturaAnimado = animado[i].offsetTop;
            if(scrollTop > alturaAnimado - 700 ){
                animado[i].style.opacity = 1;
                animado[i].classList.add('mostrarArriba');
            }
        }
    
    }


    window.addEventListener('scroll', mostrarScroll);
});
