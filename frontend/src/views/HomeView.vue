<template>
  <v-container class="grey lighten-5">
    <!-- Stack the columns on mobile by making one full-width and the other half-width -->
    <v-row>
      <v-col
        cols="12"
        md="8"
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
            <v-card-title class="title">Pengguna Gate Parking Otomatis</v-card-title>
          </v-col>
          <v-col
          sm="5"
          offset-sm="2"
          md="6"
          offset-md="0"
          >
            <v-card-subtitle class="subtitle">24 April 2023</v-card-subtitle>
          </v-col>
        </v-row>

        <v-row no-gutters class="content" fluid>
          <v-row justify="center">
            <v-col cols="12" md="4">
              <v-card color="success" dark>
                <v-card-text>
                  <div class="headline white--text">
                    <v-icon
                    large
                    color="white"> mdi-import </v-icon>
                    Masuk
                  </div>
                  <div class="text-h2 white--text" >{{ totalMasuk }}</div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="4">
              <v-card color="warning" dark>
                <v-card-text>
                  <div class="headline white--text">
                    <v-icon
                    large
                    color="white"> mdi-export </v-icon>
                    Keluar
                  </div>
                  <div class="text-h2 white--text">{{ totalKeluar }}</div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="4">
              <v-card color="red">
                <v-card-text>
                  <div class="headline white--text">
                    <v-icon
                    large
                    color="white"> mdi-alert-outline </v-icon>
                    Peringatan
                  </div>
                  <div class="text-h2 white--text">{{ totalPeringatan }}</div>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-row>

      </v-card>
    </v-col>
      <v-col
      cols="6"
      md="4"
      >
        <v-card
        class="right-side"
        outlined
        tile
        >
          <v-card-title class="title">Status Gate Parking</v-card-title>
          <v-row
          class="mb-6"
          no-gutters
          >
            <v-col
            sm="5"
            md="6"
            mr=auto
            >
              <v-btn
              class="ma-2 pl-8"
              outlined
              color="indigo"
              x-large
              >
                <v-icon
                dark
                left
                x-large
                class="pr-4"
                >
                  mdi-boom-gate-outline
                </v-icon> Gate Masuk
              </v-btn>
            </v-col>
          <v-col
          sm="5"
          offset-sm="2"
          md="6"
          offset-md="0"
          >
            <v-card-subtitle class="subtitle">
              <v-chip
              color="green"
              text-color="white"
              >
                Aktif
              </v-chip>
            </v-card-subtitle>
          </v-col>
          <v-col
          sm="5"
          md="6"
          mr=auto
          >
          <v-btn
            class="ma-2 pl-8"
            outlined
            color="orange"
            x-large
            >
              <v-icon
              dark
              left
              x-large
              class="pr-4"
              >
              mdi-boom-gate-outline
              </v-icon> Gate Keluar
            </v-btn>
          </v-col>
          <v-col
          sm="5"
          offset-sm="2"
          md="6"
          offset-md="0"
          >
            <v-card-subtitle class="subtitle">
              <v-chip
              color="red"
              text-color="white"
              >
                Tidak Aktif
              </v-chip>
            </v-card-subtitle>
          </v-col>
        </v-row>
      </v-card>
      </v-col>
    </v-row>
      <!-- <notification-component ref="notificationComponent"></notification-component> -->
    <v-card class="mt-6">
      <v-card-title class="title">Pemberitahuan</v-card-title>
      <v-row
      class="mb-6"
      no-gutters
      >
        <v-col
        sm="5"
        md="6"
        mr=auto
        >
          <v-list>
            <v-list-item v-for="(notification, index) in notifications" :key="index">
              <v-list-item-avatar>
                <v-icon color="red">{{ notification.icon }}</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title>{{ notification.title }}</v-list-item-title>
                <v-list-item-subtitle>{{ notification.message }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
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
          color="success"
          class="ma-2 mt-4 white--text"
          large
          >
            <v-icon
            right
            dark
            class="mr-2"
            >
              mdi-check
            </v-icon>
            Izinkan
          </v-btn>

          <v-btn
          color="red"
          class="ma-2 mt-4 white--text"
          large
          outlined
          >
            <v-icon
            right
            dark
            class="mr-2"
            >
              mdi-close
            </v-icon>
            Tolak
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'
import { VCard, VCardText } from 'vuetify/lib';

  export default{
    data() {
      return {
        totalMasuk: null,
        totalKeluar: null,
        totalPeringatan: null,
        dialog: false,
        alertTitle: 'Peringatan',
        alertMessage: 'RFID dan Pelat Nomor tidak cocok di Gate Keluar, Mohon untuk ditindaklanjuti.',
        message: 'Hello, world!',
        notifications: [
          {
            icon: 'mdi-alert',
            title: 'Alert',
            message: 'RFID dan Pelat Nomor tidak cocok di Gate Keluar, Mohon untuk ditindaklanjuti'
          }
        ]
      }
    },

    mounted() {
      this.getDataJumlahMasuk();
      setInterval(this.getDataJumlahMasuk, 3000);
      this.getDataJumlahKeluar();
      setInterval(this.getDataJumlahKeluar, 3000);
      this.getDataJumlahPeringatan();
      setInterval(this.getDataJumlahPeringatan, 3000);
    },

    methods: {
    async getDataJumlahMasuk() {
      try {
        const response = await axios.get('http://localhost:8080/get_riwayat_count'); // Ganti '/api/endpoint' dengan URL API yang sesuai
        this.totalMasuk= response.data.data; // Simpan respons API ke variabel 
        console.log(this.totalMasuk)
      } catch (error) {
        console.error(error);
      }
    },

    async getDataJumlahKeluar() {
        try {
          const response = await axios.get('http://localhost:8080/get_keluar_count'); // Ganti '/api/endpoint' dengan URL API yang sesuai
          this.totalKeluar= response.data.data; // Simpan respons API ke variabel data
        } catch (error) {
          console.error(error);
        }
      },

      // fetchApiDataJumlahKeluar() {
      //   axios.get('https://gpujtk.polban.studio/get_riwayat_count') // Ubah URL sesuai dengan API Anda
      //     .then(response => {
      //       this.totalKeluar = response.data; // Mengambil nilai data dari respons API
      //     })
      //     .catch(error => {
      //       console.error(error);
      //     });
      // },

      async getDataJumlahPeringatan() {
        try {
          const response = await axios.get('http://localhost:8080/get_problem_count'); // Ganti '/api/endpoint' dengan URL API yang sesuai
          this.totalPeringatan = response.data.data; // Simpan respons API ke variabel data
        } catch (error) {
          console.error(error);
        }
      }
    },

    components: {
      VCard,
      VCardText
    }
  }
  </script>

<style scoped>
.title{
  color: orange;
  font-display: bold;
  font-size: x-large;
  
}
.modalTitle{
  text-align: center;
  align-content: center;
  justify-content: center;
  padding-top: 16px;
  color: rgb(240, 35, 35);
}
.subtitle{
  text-align: right;
  margin-top: 8px;
}
.content{
  padding-right: 16px;
  padding-left: 16px;
  padding-bottom: 16px;
}

.right-side{
  text-align: right;
}
</style>
