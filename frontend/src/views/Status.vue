<template>
    <v-container class="grey lighten-5">
    <v-row>
      <v-col
      >
        <v-card
          class="left-side"
          outlined
          tile
        >
        <v-row
        class="mb-6"
        no-gutters
        >
        <v-card-title class="title">Status Pengguna Gedung Parkir Polteknik Negeri Bandung</v-card-title>
        </v-row>
        <v-data-table
        v-model="selected"
        :headers="headers"
        :items="contents"
        :single-select="singleSelect"
        item-key="name"
        show-select
        class="elevation-1"
        >
          <template v-slot:top>
            <v-switch
            v-model="singleSelect"
            label="Single select"
            class="pa-3"
            ></v-switch>
          </template>
        </v-data-table>
        </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  <script>
  
  export default {
    name: 'riwayat-page',
    data () {
        return {
          singleSelect: false,
          selected: [],
          headers: [
            {
              text: 'Nama',
              align: 'start',
              sortable: false,
              value: 'Nama',
            },
            { text: 'Status', value: 'Status' },
            { text: 'Keterangan', value: 'Keterangan' },
          ],
          contents: [
            {
              Nama: 'Frozen Yogurt',
              Status: 159,
              Keterangan: 'Terhubung',
            },
          ],
        }
      },
  };
  </script>
  
  <style scoped>
  .title{
  color: orange;
  font-display: bold;
  font-size: smaller;
  }
  .left-side{
  text-align: right;

  }
  .right-side{
  }
  </style>