var userName = document.getElementById('form3Example1c');
var email = document.getElementById('form3Example3c');
var password = document.getElementById('form3Example4c');
var registerForm = document.getElementById('registerForm');
var firstName = document.getElementById('form3Example1');
var lastName = document.getElementById('form3Example2');


var allUsers =JSON.parse (localStorage.getItem('user') )|| []; 

registerForm.addEventListener('submit', function(event){
  event.preventDefault();

  console.log('before click', allUsers)

var user ={
  
    name: userName.value,
    email: email.value,
    password: password.value, 

}

var allUsers =[];
allUsers.push(user)

console.log(user)


//save to local storage
  localStorage.setItem('user',JSON.stringify(allUsers));

console.log('after click',allUsers)
Swal.fire({
  position: "center",
  icon: "success",
  title: "Your work has been saved",
  showConfirmButton: false,
  timer: 1500
});

})



