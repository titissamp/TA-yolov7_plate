<template>
  <v-app>
    <v-main>
      <Sidebar />
      <div :style="{ 'margin-left': sidebarWidth }">
      <router-view />
    </div>
    </v-main>
  </v-app>
</template>

<script>
import Sidebar from '@/components/sidebar/Sidebar'
import { sidebarWidth } from '@/components/sidebar/state'
export default {
  name: 'App',

  data: () => ({
    //
  }),
  components: { Sidebar },
  setup() {
    return { sidebarWidth }
  }
}

</script>
