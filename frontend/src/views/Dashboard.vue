<template>
  <div>
    <h1>The sidebar is {{ collapsed ? 'closed' : 'open' }}</h1>
  </div>
</template>

<script>
import { collapsed, toggleSidebar } from '@/components/sidebar/state'

export default {
  name: 'Dashboard-page',
  setup() {
    return { collapsed, toggleSidebar }
  }
}
</script>
