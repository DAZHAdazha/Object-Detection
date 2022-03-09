<template>

  <div id="Header">
    <div class="top-left-edition">
      <span style="color: #ff7c0b; font-weight: bold">
        Yunjia Feng
      </span>
      <span style="color:#21B3B9; font-weight: bold">
        2018110239
      </span>
      <a id="login">
        <span @click="myfunRouter" id="loginText" class="link"
          style=" cursor:pointer; color:#21B3B9; font-weight: bold; float:right">
          Log in/Sign up
        </span>
      </a>
    </div>
    <div id="word">
      <h1>{{ msg }}</h1>
    </div>
  </div>
</template>
<script>
  export default {
    name: "Header",
    data() {
      return {
        msg: "Object Detection Yolov5",
        user: "login",
      };
    },
    methods: {
      myfunRouter: function () {
        this.$router.push('/' + this.user);
        location.reload();
      },

    },
    created() {

      var httpRequest = new XMLHttpRequest();
      httpRequest.open('POST', 'http://127.0.0.1:5003/validation', true);
      httpRequest.setRequestHeader("Content-type", "application/json");
      httpRequest.send();
      httpRequest.onreadystatechange = () => {
        if (httpRequest.readyState == 4 && httpRequest.status == 200) {
          var json = httpRequest.responseText;
          if (json != '0') {
            const sign = document.getElementById('loginText');
            sign.innerHTML = json;
            this.user = "search";
          }
        }
      };
    }
  }
</script>
<style scoped>
  #Header {
    padding: 30px 110px 0 150px;
    width: 90%;
    margin: 10px auto;
  }

  #word {
    margin-left: 33%;
    margin-top: -35px;
    margin-bottom: 37px;
    height: 60px;
    line-height: 3.2em;
    letter-spacing: 8px;
  }

  h1 {
    /*text-align: center;*/
    color: #ff7c0b;
    letter-spacing: 3px;
    font-size: 2.3em;
  }

  .el-menu-demo {
    width: 80%;
    margin: 0px auto;
    padding: 0px auto;
  }

  .top-left-edition span i {
    float: left;
    margin-right: 10px;
  }

  i,
  input,
  label {
    vertical-align: middle;
  }

  i {
    border: 0;
    display: block;
    cursor: pointer;
  }

  .top-left-edition span {
    float: left;
    font-size: 16px;
    color: #999999;
    line-height: 24px;
    margin-right: 40px;
  }

  .link {
    transition: all .2s ease-in-out;
  }

  .link:hover {
    transform: scale(1.1);
    color: #ff7c0b !important;
  }
</style>