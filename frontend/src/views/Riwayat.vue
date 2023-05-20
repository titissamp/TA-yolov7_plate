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
        <v-card-title class="title">Riwayat Pengguna Gedung Parkir Polteknik Negeri Bandung</v-card-title>

      <v-data-table
      :headers="headers"
      :items="content"
      >
        <!-- <template v-slot:top>
          <v-switch
          v-model="singleSelect"
          label="Single select"
          class="pa-3"
          ></v-switch>
        </template> -->
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
import axios from 'axios'
export default {
  name: 'status-page',
  data () {
      return {
        // singleSelect: false,
        content:[],
        // selected: [],
        headers: [
          {
            text: 'RFID',
            align: 'start',
            sortable: false,
            value: 'RFID',
          },
          { text: 'Pelat Nomor', value: 'pelatNomor' },
          { text: 'Waktu Masuk', value: 'waktuMasuk' },
          { text: 'Bukti Masuk', value: 'buktiMasuk' },
          { text: 'Waktu Keluar', value: 'waktuKeluar' },
          { text: 'Bukti Keluar', value: 'buktiKeluar' },
          { text: 'Status', value: 'status' },
        ],
      }
    },

    mounted() {
    this.getDataRiwayat();
    // setInterval(this.getDataRiwayat,3000);
    },

    methods: {
      async getDataRiwayat() {
        try {
          const response = await axios.get('http://localhost:8080/get_riwayat_parkir'); // Ganti '/api/endpoint' dengan URL API yang sesuai
          this.content = response.data;
          // const list = response.data.data
          // const regex = /^(\d{4})(\d{3})(\d{4})$/;
          // const mappedRiwayat = list.map((item) => ({
          //   RFID: item.RFID,
          //   PelatNomor: item.pelatNomor,
          //   WaktuMasuk: item.waktuMasuk,
          //   BuktiMasuk: item.buktiMasuk,
          //   WaktuKeluar: item.waktuKeluar,
          //   BuktiKeluar: item.buktiKeluar,
          //   Status: item.status
          // }));
          // this.content = mappedRiwayat
        } catch (error) {
          console.error(error);
        }
      },
      handleClick(item) {
        console.log(item)
      }
    }
  }
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