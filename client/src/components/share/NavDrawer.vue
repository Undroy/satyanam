<template>
  <div>
    <v-toolbar :src="bg ? 'https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg' : undefined">
      <v-toolbar-title>Title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items>
        <v-btn text>Link 1</v-btn>
        <v-btn text>Link 2</v-btn>
        <v-btn text>Link 3</v-btn>
      </v-toolbar-items>

      <template v-if="$vuetify.breakpoint.smAndUp">
        <v-btn icon>
          <v-icon>mdi-export-variant</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-delete-circle</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </template>
    </v-toolbar>
  </div>
</template>

<script>
export default {
  data: () => ({
    bg: true,
    menu: false,
    drawer: false,
    items: [
      { title: 'Edit Profile' },
      { title: 'Logout' }
    ]
  }),
  props: {
      source: String
  },
//   methods: {
//     referTo (route) {
//         this.$router.push(route)
//     },
//     logout (route) {
//       this.$store.state.isUserLoggedIn = false
//       this.$store.state.token = null
//       this.$store.state.loginuser = null
//       this.$router.push(route)
//     },
//     droproute (data) {
//       if (data === 'Logout') {
//         this.logout ({name: 'home'})
//       } else {
//         alert (data)
//       }
//     }
//   }
}
</script>

