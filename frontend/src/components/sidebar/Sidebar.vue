<script>
import SidebarLink from './SidebarLink'
import { collapsed, toggleSidebar, sidebarWidth } from './state'

export default {
  name: 'Sidebar-menu',
  props: {},
  components: { SidebarLink },
  setup() {
    return { collapsed, toggleSidebar, sidebarWidth }
  }
}
</script>

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h3>
      <img src="src/assets/polban.png">
      <span v-if="collapsed">
        <div>G</div>
        <div>P</div>
        <div>O</div>
      </span>
      <span v-else>Gate Parking Otomatis</span>
    </h3>

    <SidebarLink to="/" icon="fas fa-home">Overview</SidebarLink>
    <SidebarLink to="/dashboard" icon="fas fa-columns">Status</SidebarLink>
    <SidebarLink to="/analytics" icon="fas fa-chart-bar">Riwayat</SidebarLink>
  

    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<style>
:root {
  --sidebar-bg-color:white;
  --sidebar-item-hover: rgb(208, 173, 31);
  --sidebar-item-active: rgb(227, 122, 11);
}
</style>

<style scoped>
.sidebar {
  color: rgb(227, 122, 11);
  background-color: var(--sidebar-bg-color);

  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;

  transition: 0.3s ease;

  display: flex;
  flex-direction: column;
}

.sidebar h1 {
  height: 2.5em;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;

  color: black;

  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}
</style>
