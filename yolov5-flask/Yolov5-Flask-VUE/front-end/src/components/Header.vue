<template>

  <div id="Header">
    <div class="top-left-edition">
      <span style="color: #ff7c0b; font-weight: bold">
        <!-- <i class="el-icon-star-off" style="font-size: 23px"></i> -->
        Yunjia Feng
      </span>
      <span style="color:#21B3B9; font-weight: bold">
        <!-- <i class="el-icon-search" style="font-size: 23px"></i> -->
        2018110239
      </span>


        <a id="login">
          <span  @click="myfunRouter" id="loginText" class="link" style=" cursor:pointer; color:#21B3B9; font-weight: bold; float:right">
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
        user:"login",
      };
    },
    methods: {
      myfunRouter: function (){
        this.$router.push('/' + this.user);
        location.reload();
      },
    
  },created () {

          var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
          httpRequest.open('POST', 'http://127.0.0.1:5003/validation', true); //第二步：打开连接/***发送json格式文件必须设置请求头 ；如下 - */
          httpRequest.setRequestHeader("Content-type","application/json");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
          httpRequest.send();//发送请求 将json写入send中
          /**
           * 获取数据后的处理程序
           */
          httpRequest.onreadystatechange = () => {//请求后的回调接口，可将请求成功后要执行的程序写在其中
              if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
                  var json = httpRequest.responseText;//获取到服务端返回的数据
                  if(json!='0'){
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