// Login/Register toggle button:

const registerBtn = document.querySelector('#register-toggleBtn');
const loginBtn = document.querySelector('#login-toggleBtn');
const toggleBtn = document.querySelector('#toggle');
const form1 = document.querySelector('#login');
const form2 = document.querySelector('#register');
const formContainer = document.querySelector('.form');

registerBtn.addEventListener('click', () => {
  toggleBtn.style.left = '103px';
  registerBtn.style.color = 'white';
  loginBtn.style.color = 'black';
  form1.style.left = '-400px';
  form2.style.left = '0px';
  userLabel.classList.remove('active');
  passLabel.classList.remove('active');
  usernameInput.value = '';
  passInput.value = '';
});

loginBtn.addEventListener('click', () => {
  toggleBtn.style.left = '-5px';
  registerBtn.style.color = 'black';
  loginBtn.style.color = 'white';
  form1.style.left = '0px';
  form2.style.left = '440px';
  userLabelReg.classList.remove('active');
  passLabelReg.classList.remove('active');
  emailLabel.classList.remove('active');
  usernameInputReg.value = '';
  passInputReg.value = '';
  emailInput.value = '';
});

//Input label click event (form1):

const usernameInput = document.querySelector('#username');
const userLabel = document.querySelector('#user-label');

const passInput = document.querySelector('#password');
const passLabel = document.querySelector('#pass-label');

usernameInput.addEventListener('click', () => {
  userLabel.classList.add('active');
});

passInput.addEventListener('click', () => {
  passLabel.classList.add('active');
});

//Input label click event (form2):

const usernameInputReg = document.querySelector('#username-reg');
const userLabelReg = document.querySelector('#user-label-reg');

const passInputReg = document.querySelector('#password-reg');
const passLabelReg = document.querySelector('#pass-label-reg');

const emailInput = document.querySelector('#email');
const emailLabel = document.querySelector('#email-label');

usernameInputReg.addEventListener('click', () => {
  userLabelReg.classList.add('active');
});

emailInput.addEventListener('click', () => {
  emailLabel.classList.add('active');
});

passInputReg.addEventListener('click', () => {
  passLabelReg.classList.add('active');
});

