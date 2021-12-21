<template>
  <div id="Header">
    <div class="top-left-edition">
      <span style="color: #ff7c0b; font-weight: bold">
       <!-- <i class="el-icon-star-off" style="font-size: 23px"></i> -->
       冯韵嘉
      </span>
      <span style="color:#21B3B9; font-weight: bold">
        <!-- <i class="el-icon-search" style="font-size: 23px"></i> -->
        2018110239
      </span>

    <router-link to="/login">

      <a id="login" >
      <span class="link" style="color:#21B3B9; font-weight: bold; float:right">
         Log in/Sign up
      </span>
      </a>
      </router-link>

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
      activeIndex: "1",
    };
  },
  methods: {
  },
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
.link{
transition: all .2s ease-in-out;
}
.link:hover
{
transform: scale(1.1);
color: #ff7c0b!important;
}

</style>


