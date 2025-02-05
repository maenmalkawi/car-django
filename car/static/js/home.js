// // alert('welcome to the page')

// // var inputTxt =document.getElementById('inputTxt');
// // var checkbox =document.getElementById('checkbox')
//  var selectColor = document.getElementById('selectColor')
//  var body =document.getElementsByTagName('body')[0]
//  var nav = document.getElementById('navbarNav');
//  var card = document.getElementsByClassName('card')
//  var allCart = JSON.parse(localStorage.getItem('cart')) || []
// // function changeTxt(){

// // console.log(inputTxt.value);

// // }

// function changeColor(){
//     console.log(selectColor.value)
//      body.style.backgroundColor=selectColor.value;
//      nav.style.backgroundColor=selectColor.value;
//      console.log(card)
//      for (let index = 0; index < card.length; index++) {
//         card[index].style.background=selectColor.value;
        
//      }


//  }
//  var  card = document.getElementsByClassName('card')
// var counter = document.getElementById('counter')
// counter.innerHTML =allCart.length 


// function savecart (num){
//     console.log(card[num].children[1].children)
//     cart = {
//         title:card[num].children[1].children[0].innerHTML,
//         des:card[num].children[1].children[1].innerHTMl
//     }
//     allCart.push(cart)
//     counter.innerHTML =allCart.length 
//     // localStorage.setItem('title',card[num].children[1].children[0].innerHTML)
//     // localStorage.setItem('desc',card[num].children[1].children[1].innerHTML)
//    localStorage.setItem('cart',JSON.stringify(allCart))
        
        

// }

var inputTxt = document.getElementById('inputTxt');
// var txt = document.getElementById('txt');
var profile =document.getElementById('profile');
var dropdown =document.getElementById('dropdown');
var logout =document.getElementById('logout');






console.log(inputTxt.value);
if (localStorage.getItem('logout')=='true'){
profile.style.display= 'block'
logout.style.display= 'block'
dropdown.style.display='none'
}
function logoutfun(){
    localStorage.setItem('logout','false')
window.location.href = 'regester.html';
 
}
