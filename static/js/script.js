var cards = document.querySelectorAll("div.card");

        for(let card of cards){
            card.addEventListener('mouseover', function(){
                card.style = 'transform: rotateY(180deg) scale(1.1);background-color: #DAA520;'
                for(let i = 0 ; i<card.children.length; i++){
                 card.children[i].style = "display:none; "
                }
                card.children[0].style = 'display:block;'
            }
            )

            card.addEventListener('mouseout', function(){
                card.style = 'transform: rotateY(0deg) scale(1)'
                for(let i = 0 ; i<card.children.length; i++){
                 card.children[i].style = "display:block;"
                }
                card.children[0].style = 'display:none'
            })}

var width = window.innerWidth

console.log(width)