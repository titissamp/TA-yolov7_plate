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
                    color="white">
                      mdi-import
                    </v-icon>
                    Masuk
                  </div>
                  <div class="display-4 white--text">{{ totalUsers }}</div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="4">
              <v-card color="warning" dark>
                <v-card-text>
                  <div class="headline white--text">
                    <v-icon
                    large
                    color="white">
                      mdi-export
                    </v-icon>
                    Keluar
                  </div>
                  <div class="display-4 white--text">{{ totalSales }}</div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="4">
              <v-card color="red">
                <v-card-text>
                  <div class="headline white--text">
                    <v-icon
                    large
                    color="white">
                      mdi-alert-outline
                    </v-icon>
                    Peringatan
                  </div>
                  <div class="display-4 white--text">{{ totalRevenue }}</div>
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
    <v-btn @click="showAlert">Tampilkan Peringatan</v-btn>
      <v-dialog v-model="dialog" max-width="500px">
        <v-card class="modal"> 
          <v-card-title class="modalTitle text-h4">
            <v-icon
            class="mr-2"
            color="red"
            x-large>
              mdi-alert-outline
            </v-icon>
          </v-card-title>
          <v-card-title class="text-center justify-center align-center text-h5" color="black">{{ alertTitle }}</v-card-title>
          <v-card-text class="text-center justify-center align-center">{{ alertMessage }}</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="red" text @click="dialog = false" class="justify-content-center text-center align-content-center">Tutup</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  </v-container>
</template>

<script>
  export default {
    data() {
      return {
        totalUsers: 500,
        totalSales: 1000,
        totalRevenue: 500,
        dialog: false,
        alertTitle: 'Peringatan',
        alertMessage: 'RFID dan Pelat Nomor tidak cocok di Gate Keluar, Mohon untuk ditindaklanjuti.'
      }
    },
    methods: {
      showAlert() {
        this.dialog = true
      }
    }
  }
  </script>

<style scoped>
.title{
  color: orange;
  font-display: bold;
  
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
</style>
