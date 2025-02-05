var eye = document.getElementById('eye');
function showPassword() {
    // password.type='text';
    if (password.type === 'password') {
        password.type = 'text';
        eye.src='../media/eye close.png';
    } else {
        password.type = 'password';
        eye.src='../media/eyeopen.png';
        
    
    }
}
eye.addEventListener('click',showPassword);


var email = document.getElementById('form3Example3');
var password = document.getElementById('form3Example4');

var submitButton = document.getElementById('submitButton');


submitButton.addEventListener('click' , function(event){
    
  event.preventDefault();
  console.log(email.value);
  console.log(password.value);

var user=localStorage.getItem('user');
 user =JSON.parse(user); // رجعلي اليوزر لحالته قبل ما اجوله لسترنيقي فاي
  
 var isValid=false;

for(var i=0 ; i<user.length;i++){


    if(user[i]['email']==email.value &&  user[i]['password']==password.value){
        
    
       localStorage.setItem('image','./media/audi.jpg')
       localStorage.setItem('login','true')
     
       window.location.href ='home.html';
         isValid= true; 
        }

}
 
    if(isValid==false){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "email or password are incorrect !",
            footer: '<a href="#">Why do I have this issue?</a>'
          });
    }

})