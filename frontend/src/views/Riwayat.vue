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
        <v-col
        sm="5"
        md="6"
        mr=auto
        >
          <v-card-title class="title">Riwayat Pengguna Gedung Parkir Polteknik Negeri Bandung</v-card-title>
        </v-col>

        <v-col
        class="right-side"
        sm="5"
        offset-sm="2"
        md="6"
        mr="12"
        offset-md="0"
        >
          <v-btn
          color="indigo"
          class="ma-2 mt-4 white--text"
          outlined
          >
            <v-icon
            right
            dark
            class="mr-4"
            >
              mdi-bell-outline
            </v-icon>
            Button
          </v-btn>

          <v-btn
          color="#5E35B1"
          class="ma-2 mt-4 white--text"
          >
            <v-icon
            right
            dark
            class="mr-4"
            >
              mdi-plus
            </v-icon>
            Add Record
          </v-btn>
        </v-col>
      </v-row>
      <v-data-table
      :headers="headers"
      :items="contents"
      :single-select="singleSelect"
      show-select
      >
        <template v-slot:top>
          <v-switch
          v-model="singleSelect"
          label="Single select"
          class="pa-3"
          ></v-switch>
        </template>
        <template v-slot:[`item.buktiMasuk`]="{item}">
          <v-btn color="primary" @click="handleClick(item)">
            Lihat Gambar
          </v-btn>
        </template>
        <template v-slot:[`item.buktiKeluar`]="{item}">
          <v-btn color="primary" @click="handleClick(item)">
            Lihat Gambar
          </v-btn>
        </template>
      </v-data-table>
      </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: 'status-page',
  data () {
      return {
        singleSelect: false,
        selected: [],
        headers: [
          {
            text: 'RFID',
            align: 'start',
            sortable: false,
            value: 'RFID',
          },
          { text: 'Pelat Nomor', value: 'pelatNomor' },
          { text: 'Waktu Masuk', value: 'waktuMasuk' },
          { text: 'Waktu Keluar', value: 'waktuKeluar' },
          { text: 'Bukti Masuk', value: 'buktiMasuk' },
          { text: 'Bukti Keluar', value: 'buktiKeluar' },
          { text: 'Status', value: 'status' },
          { text: 'Action', value: 'actioin' },
        ],
        contents: [
          {
            RFID: '19029374202',
            pelatNomor: 'D 1234 YD',
            waktuMasuk: 6.0,
            waktuKeluar: 24,
            buktiMasuk: 'Lihat Gambar',
            buktiKeluar: 'Lihat Gambar',
            status: 1,
            action: 'icon'
          },
        ],
      }
    },
    methods: {
      handleClick(item) {
        console.log(item)
      }
    }
};
</script>

<style scoped>
.title{
color: orange;
font-display: bold;
}
.left-side{
text-align: right;
margin-top: 0px;
}
.right-side{
}
</style>