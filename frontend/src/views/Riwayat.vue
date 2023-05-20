<template>
  <v-container class="grey lighten-5">
    <v-card
        class="left-side"
        outlined
        tile
      >
        <v-card-title class="title">Riwayat Pengguna Gedung Parkir Polteknik Negeri Bandung</v-card-title>

      <v-data-table
      :headers="headers"
      :items="items"
      class="elevation-1 pl-4 pr-4"
      >
        <!-- <template v-slot:top>
          <v-switch
          v-model="singleSelect"
          label="Single select"
          class="pa-3"
          ></v-switch>
        </template> -->
        <template v-slot:[`item.BuktiMasuk`]="{ item }">
          <v-btn color="primary" @click="openDialog(item.BuktiMasuk)">
            Lihat Gambar
          </v-btn>
        </template>
        <template v-slot:[`item.BuktiKeluar`]="{item}">
          <v-btn color="primary" @click="openDialog(item.BuktiKeluar)">
            Lihat Gambar
          </v-btn>
        </template>
      </v-data-table>
      <v-dialog v-model="dialogVisible" max-width="500px">
        <v-img :src="popupLink" width="100%"></v-img>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="closeDialog">Tutup</v-btn>
        </v-card-actions>
      </v-dialog>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  name: 'riwayat-page',
  data() {
      return {
        // singleSelect: false,
        // selected: [],
        headers: [
          {
            text: 'RFID',
            align: 'start',
            sortable: false,
            value: 'RFID',
          },
          { text: 'Pelat Nomor', value: 'PelatNomor' },
          { text: 'Waktu Masuk', value: 'WaktuMasuk' },
          { text: 'Bukti Masuk', value: 'BuktiMasuk', sortable: false, },
          { text: 'Waktu Keluar', value: 'WaktuKeluar' },
          { text: 'Bukti Keluar', value: 'BuktiKeluar', sortable: false, },
          { text: 'Status', value: 'Status' },
        ],
        items: [],
        dialogVisible: false,
        popupLink: ''
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
          // this.items = response.data;
          const list = response.data
          const mappedRiwayat = list.map((item) => ({
            BuktiKeluar: item[2],
            BuktiMasuk: item[0],
            PelatNomor: item[4],
            RFID: item[5],
            Status: item[6],
            WaktuKeluar: item[3],
            WaktuMasuk: item[1],
          }));
          this.items = mappedRiwayat
          console.log(response)
        } catch (error) {
          console.error(error);
        }
      },
      openDialog(item) {
        this.popupLink = item;
        this.dialogVisible = true;
      },
      closeDialog() {
      this.dialogVisible = false;
      this.popupLink = '';
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