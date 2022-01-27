<template>
  <div id="index">
    <app-header></app-header>
    <app-content></app-content>
    <app-footer></app-footer>

  </div>
</template>

<style scoped>

</style>


<script>
  import Header from "./components/Header";
  import Footer from "./components/Footer";
  import Content from "./components/Content";
  


  export default {
    name: "Object Detection Yolov5",
    data() {
      return {};
    },
    components: {
      "app-content": Content,
      "app-header": Header,
      "app-footer": Footer,
    },
    methods: {},
    mounted() {
      document.documentElement.style.setProperty('--app-bg','rgb(225, 232, 238)')
    }
  };
</script>