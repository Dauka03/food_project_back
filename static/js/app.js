var $hamburger = document.querySelector('.hamburger');
var $menu = document.querySelector('.menu-bar');

var email = document.forms['form']['email'];
var password = document.forms['form']['password'];


email.addEventListener('textInput', email_Verify);
password.addEventListener('textInput', pass_Verify);


function validated(){
    if(email.value.length < 9 ){
        email.style.border = "1px solid red";
        email.focus();
        return false;
    }
    if(password.value.length < 6 ){
        password.style.border = "1px solid red";
        password.focus();
        return false;
    }
}

function email_Verify(){
    if(email.value.length >= 8){
        email.style.border = "1px solid silver";
        return true;
    }
}

function pass_Verify(){
    if(password.value.length >= 6){
        password.style.border = "1px solid silver";
        return true;
    }
}

function toggleMenu() {
    $menu.classList.toggle('active-mobile');
}
$hamburger.addEventListener('click', toggleMenu);

const spinner = document.getElementById('spinner')
const tableBody = document.getElementById('table-body-box')

const url = window.location.href
console.log(url)

$.ajax({
    type: 'GET',
    url: '/data-json/',
    success: function(responce){
        const data = JSON.parse(responce.data)
        console.log(data)
        data.forEach(el=>{
            console.log(el.fields)
            tableBody.innerHTML += `
                <tr>
                    <td>${el.pk}</td>
                    <td><img src="${url}media/${el.fields.item}" height='40px'></td>
                    <td>${el.fields.info}</td>
                </tr>

            `
        })
    }
})

