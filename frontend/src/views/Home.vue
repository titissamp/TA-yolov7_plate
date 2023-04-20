<template>
    <v-container class="d-flex bg-surface-variant">
    <v-row no-gutters>
      <v-col>
        <v-sheet class="d-flex pa-2 ma-2">
          <v-card
          class="mx-auto"
          width="75%"
          padding-top="50px"
          prepend-icon="mdi-home"
        >
          <v-card-text>
            Penggunaan Gate Parking Otomatis
          </v-card-text>
          </v-card>
        </v-sheet>

      </v-col>
      <v-col>
        <v-sheet class="d-flex pa-2 ma-2">
          Gate Status
        </v-sheet>
      </v-col>
    </v-row>
    </v-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home-page',
  components: {
  }
}
</script>
