var mybutton = document.getElementById("top");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
const navOpen = document.querySelector(".hamburger");
const navContainer = document.querySelector(".nav_menu");
const list = document.querySelector(".nav_list");

navOpen.addEventListener("click", () => {
  const listHeight = list.getBoundingClientRect().height;
  const navHeight = navContainer.getBoundingClientRect().height;

  if (navHeight === 0) {
    navContainer.style["max-height"] = `${listHeight}px`;
  } else {
    navContainer.style["max-height"] = 0;
  }
});




//profile 
function openProf() {
  document.getElementById("myProf").style.display = "block";
}

function closeProf() {
  document.getElementById("myProf").style.display = "none";
}

// credential
function openCred() {
  document.getElementById("myCred").style.display = "block";
}

function closeForm() {
  document.getElementById("myCred").style.display = "none";
}



// log in design

const loginText = document.querySelector(".title-text .login");
         const loginForm = document.querySelector("form.login");
         const loginBtn = document.querySelector("label.login");
         const signupBtn = document.querySelector("label.signup");
         const signupLink = document.querySelector("form .signup-link a");
         signupBtn.onclick = (()=>{
           loginForm.style.marginLeft = "-50%";
           loginText.style.marginLeft = "-50%";
         });
         loginBtn.onclick = (()=>{
           loginForm.style.marginLeft = "0%";
           loginText.style.marginLeft = "0%";
         });
         signupLink.onclick = (()=>{
           signupBtn.click();
           return false;
         });


//login validation 
function validate(){
  const YName=document.getElementById('YName');
  const email=document.getElementById('email');
  const password1=document.getElementById('password1');
  const YPass2=document.getElementById('YPass2');
  const message=document.getElementsByClassName('message');

//submit sucess variable//
  let u=0;
  let e=0;
  let p1=0;
  let p2=0;

  //validation for name//
  if(YName.value==""){
    YName.style.borderColor = 'red';
    message[0].style.visibility = 'visible';
    message[0].style.color='red';
    message[0].innerText="Username cannot be blank";
  }

  else if(YName.value.length<5&&YName.value.length>0){
    YName.style.borderColor = 'red';
    message[0].style.visibility = 'visible';
    message[0].style.color='red';
    message[0].innerText="Username have atleast 5 character";
    // u=0;
  }
  else if(YName.value.length>3&&(isNaN(parseFloat(YName.value)))){
    YName.style.borderColor = 'green';
    message[0].style.visibility = 'hidden';
    u=1;
}

  // }
  //email validation//

  if(email.value==""){
		email.style.borderColor = 'red';
		message[1].style.visibility = 'visible';
		message[1].style.color='red';
	  message[1].innerText="Email cannot be blank";
		e=0;
		}
	
    else if(email.value.indexOf('@')<3||email.value.lastIndexOf('.')>=email.value.length-2){
		email.style.borderColor = 'red';
		message[1].style.visibility = 'visible';
		message[1].style.color='red';
		message[1].innerText="Invalid email";
		e=0;
		}
				
    else{
			email.style.borderColor = 'green';
			message[1].style.visibility = 'hidden';
			e=1;
		}
        
		
  //validation of password//

	var numbers=/[0-9]/g;
	if (password1.value==""){
		password1.style.borderColor = 'red';
		message[2].style.visibility = 'visible';
		message[2].style.color='red';
		message[2].innerText="Password cannot be blank";
		// p1=0;
		}
				
  else if(password1.value.length<9){
			password1.style.borderColor = 'red';
			message[2].style.visibility = 'visible';
			message[2].style.color='red';
			message[2].innerText="Password must be minimum 8 character";
    	p1=0;
			}

	else if(!(password1.value.match(numbers))){
		password1.style.borderColor = 'red';
		message[2].style.visibility = 'visible';
		message[2].style.color='red';
		message[2].innerText="Password have atleast a number";
		// p1=0;
		}

	else{
		password1.style.borderColor = 'green';
		message[2].style.visibility = 'hidden';
		p1=1;
	}


  //password check//
  if(YPass2.value==""){
    YPass2.style.borderColor = 'red';
    message[3].style.visibility = 'visible';
    message[3].style.color='red';
    message[3].innerText="Password cannot be blank";
    p2=0;
  }
  else if(password1.value!=YPass2.value){
    YPass2.style.borderColor = 'red';
    message[3].style.visibility = 'visible';
    message[3].style.color='red';
    message[3].innerText="Password does not match";
    p2=0;
  }
  else{
    YPass2.style.borderColor = 'green';
    message[3].style.visibility = 'visible';
    message[3].style.color='green';
    message[3].innerText="Password match";
    p2=1;
  }

  //return condition//

  if(u==1&&e==1&&p1==1&&p2==1){
    return true;
  }
  else
    return false;

}

