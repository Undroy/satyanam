<template>
  <v-app>
    <!-- <v-app-bar app> -->
      <NavDrawer/>
    <!-- </v-app-bar> -->
    <v-content>
      <HelloWorld/>
      <!-- <router-view/> -->
    </v-content>
  </v-app>
</template>

<script>
import NavDrawer from './components/share/NavDrawer'
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',
  components: {
    HelloWorld,
    NavDrawer
  },
  data: () => ({
    //
  }),
};
</script>
