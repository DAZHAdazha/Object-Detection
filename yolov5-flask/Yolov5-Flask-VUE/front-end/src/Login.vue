<template>
  <div id="login">
    <router-link to="/">
      <div id="home" style="color:white;position: absolute; top:5em; font-size:70px;margin-left:15%">
        <i class="el-icon-back"></i>
      </div>
    </router-link>
    <div class="form-structor" style="margin-left:40%; margin-top:8%">
      <div class="signup">
        <h2 style="margin-left:-35px" class="form-title" @click="myfunSignup" id="signup"><span>Or</span>Sign up</h2>
        <div class="form-holder">
          <input id="signupUsername" type="text" class="input" placeholder="Username" />
          <input id="signupEmail" type="email" class="input" placeholder="Email" />
          <input id="signupPassword" type="password" class="input" placeholder="Password" />
        </div>
        <button class="submit-btn" @click="Signup">Sign up</button>
      </div>
      <div class="login slide-up">
        <div class="center">
          <h2 class="form-title" @click="myfunLogin" id="loginButton"><span>Or</span>Log in</h2>
          <div class="form-holder">
            <input id="loginEmail" type="email" class="input" placeholder="Email" />
            <input id="loginPassword" type="password" class="input" placeholder="Password" />
          </div>
          <button class="submit-btn" @click="Login">Log in</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
  export default {
    name: "Object Detection Yolov5",
    data() {
      return {};
    },
    components: {},
    methods: {
      myfunSignup: function (event) {
        const loginBtn = document.getElementById('loginButton');
        let parent = event.target.parentElement;
        Array.from(event.target.parentNode.classList).find((element) => {
          if (element !== "slide-up") {
            parent.classList.add('slide-up')
          } else {
            loginBtn.parentNode.parentNode.classList.add('slide-up')
            parent.classList.remove('slide-up')
          }
        });
      },
      myfunLogin: function (event) {
        const signupBtn = document.getElementById('signup');
        let parent = event.target.parentElement.parentElement;
        Array.from(event.target.parentNode.parentNode.classList).find((element) => {
          if (element !== "slide-up") {
            parent.classList.add('slide-up')
          } else {
            signupBtn.parentNode.classList.add('slide-up')
            parent.classList.remove('slide-up')
          }
        });
      },
      Signup: function (event) {
        const signupUsername = document.getElementById('signupUsername').value;
        const signupEmail = document.getElementById('signupEmail').value;
        const signupPassword = document.getElementById('signupPassword').value;
        if (signupUsername == "" || signupEmail == "" || signupPassword == "") {
          this.$notify({
            title: "Sign up failed",
            message: "Please fill up all the inputs!",
            duration: 2000,
            type: "warning",
          });
          event.preventDefault();
        } else {
          var httpRequest = new XMLHttpRequest(); 
          httpRequest.open('POST', 'http://127.0.0.1:5003/signupPage', true); 
          httpRequest.setRequestHeader("Content-type", "application/json"); 
          var obj = {
            username: signupUsername,
            email: signupEmail,
            password: signupPassword
          };
          httpRequest.send(JSON.stringify(obj)); 
          httpRequest.onreadystatechange = () => { 
            if (httpRequest.readyState == 4 && httpRequest.status == 200) { 
              var json = httpRequest.responseText;
              if (json == '1') {
                this.$notify({
                  title: "Sign up successfully!",
                  message: "Sign up successfully!",
                  duration: 2000,
                  type: "success",
                });
                this.$router.push('/search');
              } else {
                this.$notify({
                  title: "Sign up failed!",
                  message: json,
                  duration: 2000,
                  type: "warning",
                });
              }
            }
          };
        }
      },
      Login: function (event) {
        const loginEmail = document.getElementById('loginEmail').value;
        const loginPassword = document.getElementById('loginPassword').value;
        if (loginEmail == "" || loginPassword == "") {
          this.$notify({
            title: "Login failed",
            message: "Please fill up all the inputs!",
            duration: 2000,
            type: "warning",
          });
          event.preventDefault();
        } else {
          var httpRequest = new XMLHttpRequest(); 
          httpRequest.open('POST', 'http://127.0.0.1:5003/loginPage', true); 
          httpRequest.setRequestHeader("Content-type", "application/json"); 
          var obj = {
            email: loginEmail,
            password: loginPassword
          };
          httpRequest.send(JSON.stringify(obj));
          httpRequest.onreadystatechange = () => {
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {
              var json = httpRequest.responseText; 
              if (json == '1') {
                this.$notify({
                  title: "Log in successfully!",
                  message: "Log in successfully!",
                  duration: 2000,
                  type: "success",
                });
                this.$router.push('/search');
              } else if (json == '0') {
                this.$notify({
                  title: "Log in failed!",
                  message: "Wrong password",
                  duration: 2000,
                  type: "error",
                });
              } else if (json == '2') {
                this.$notify({
                  title: "Log in failed!",
                  message: "Can not find this account",
                  duration: 2000,
                  type: "warning",
                });
              }
            }
          };
        }
      },
    },
  };
</script>

<style scoped>
  html,
  body {
    position: relative;
    min-height: 100vh;
    background-color: #E1E8EE;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: "Fira Sans", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .form-structor {
    background-color: #222;
    border-radius: 15px;
    height: 550px;
    width: 350px;
    position: relative;
    overflow: hidden;
  }

  .form-structor::after {
    content: "";
    opacity: 0.8;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-repeat: no-repeat;
    background-position: left bottom;
    background-size: 500px;
    background-image: url("./image/32.jpg");
  }

  .form-structor .signup {
    position: absolute;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    width: 65%;
    z-index: 5;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .signup.slide-up {
    top: 5%;
    -webkit-transform: translate(-50%, 0%);
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .signup.slide-up .form-holder,
  .form-structor .signup.slide-up .submit-btn {
    opacity: 0;
    visibility: hidden;
  }

  .form-structor .signup.slide-up .form-title {
    font-size: 1em;
    cursor: pointer;
  }

  .form-structor .signup.slide-up .form-title span {
    margin-right: 5px;
    opacity: 1;
    visibility: visible;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .signup .form-title {
    color: #fff;
    font-size: 1.7em;
    text-align: center;
  }

  .form-structor .signup .form-title span {
    color: rgba(0, 0, 0, 0.4);
    opacity: 0;
    visibility: hidden;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .signup .form-holder {
    border-radius: 15px;
    background-color: #fff;
    overflow: hidden;
    margin-top: 50px;
    opacity: 1;
    visibility: visible;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .signup .form-holder .input {
    border: 0;
    outline: none;
    box-shadow: none;
    display: block;
    height: 30px;
    line-height: 30px;
    padding: 8px 15px;
    border-bottom: 1px solid #eee;
    width: 100%;
    font-size: 12px;
  }

  .form-structor .signup .form-holder .input:last-child {
    border-bottom: 0;
  }

  .form-structor .signup .form-holder .input::-webkit-input-placeholder {
    color: rgba(0, 0, 0, 0.4);
  }

  .form-structor .signup .submit-btn {
    background-color: rgba(0, 0, 0, 0.4);
    color: rgba(255, 255, 255, 0.7);
    border: 0;
    border-radius: 15px;
    display: block;
    margin: 15px auto;
    padding: 15px 45px;
    width: 100%;
    font-size: 13px;
    font-weight: bold;
    cursor: pointer;
    opacity: 1;
    visibility: visible;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .signup .submit-btn:hover {
    transition: all 0.3s ease;
    background-color: rgba(0, 0, 0, 0.8);
  }

  .form-structor .login {
    position: absolute;
    top: 20%;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #fff;
    z-index: 5;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login::before {
    content: "";
    position: absolute;
    left: 50%;
    top: -20px;
    -webkit-transform: translate(-50%, 0);
    background-color: #fff;
    width: 200%;
    height: 250px;
    border-radius: 50%;
    z-index: 4;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login .center {
    position: absolute;
    top: calc(50% - 10%);
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    width: 65%;
    z-index: 5;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login .center .form-title {
    color: #000;
    font-size: 1.7em;
    text-align: center;
  }

  .form-structor .login .center .form-title span {
    color: rgba(0, 0, 0, 0.4);
    opacity: 0;
    visibility: hidden;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login .center .form-holder {
    border-radius: 15px;
    background-color: #fff;
    border: 1px solid #eee;
    overflow: hidden;
    margin-top: 50px;
    opacity: 1;
    visibility: visible;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login .center .form-holder .input {
    border: 0;
    outline: none;
    box-shadow: none;
    display: block;
    height: 30px;
    line-height: 30px;
    padding: 8px 15px;
    border-bottom: 1px solid #eee;
    width: 100%;
    font-size: 12px;
  }

  .form-structor .login .center .form-holder .input:last-child {
    border-bottom: 0;
  }

  .form-structor .login .center .form-holder .input::-webkit-input-placeholder {
    color: rgba(0, 0, 0, 0.4);
  }

  .form-structor .login .center .submit-btn {
    background-color: #6B92A4;
    color: rgba(255, 255, 255, 0.7);
    border: 0;
    border-radius: 15px;
    display: block;
    margin: 15px auto;
    padding: 15px 45px;
    width: 100%;
    font-size: 13px;
    font-weight: bold;
    cursor: pointer;
    opacity: 1;
    visibility: visible;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login .center .submit-btn:hover {
    transition: all 0.3s ease;
    background-color: rgba(0, 0, 0, 0.8);
  }

  .form-structor .login.slide-up {
    top: 90%;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login.slide-up .center {
    top: 10%;
    -webkit-transform: translate(-50%, 0%);
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login.slide-up .form-holder,
  .form-structor .login.slide-up .submit-btn {
    opacity: 0;
    visibility: hidden;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login.slide-up .form-title {
    font-size: 1em;
    margin: 0;
    padding: 0;
    cursor: pointer;
    -webkit-transition: all 0.3s ease;
  }

  .form-structor .login.slide-up .form-title span {
    margin-right: 5px;
    opacity: 1;
    visibility: visible;
    -webkit-transition: all 0.3s ease;
  }

  #home {
    transition: all .2s ease-in-out;
  }

  #home:hover {
    transform: scale(1.1);
    cursor: pointer;
  }
</style>