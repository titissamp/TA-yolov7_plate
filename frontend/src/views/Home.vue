<template>
  <div class="dashboard-page">  
    <v-container>
      <v-row no-gutters>
      <v-col cols="8">
        <v-sheet class="left-side">
          <v-flex d-flex xs12 sm6 md4>
            <v-card color="white" dark rounded="lg">
              <div class="left-side-title">
                <v-row no-gutters>
                  <v-col>
                    <v-card-title primary class="title">Pengguna Gate Parking Otomatis</v-card-title>
                  </v-col>
                  <v-col>
                    <v-card-subtitle primary class="subtitle">24 April 2023</v-card-subtitle>
                  </v-col>
                </v-row>
              </div>
              <v-row no-gutters>
                <v-col>
                  <v-sheet class="info-masuk">
                    Masuk 
                  </v-sheet>
                </v-col>
                <v-col>
                  <v-sheet class="info-keluar">
                    Keluar
                  </v-sheet>
                </v-col>
                <v-col>
                  <v-sheet class="info-peringatan">
                    Peringatan
                  </v-sheet>
                </v-col>
              </v-row>
            </v-card>
          </v-flex>
        </v-sheet>
      </v-col>

      <v-col cols="4">
        <v-sheet class="right-side">
          <v-flex d-flex xs12 sm6 md4>
            <v-card color="white" dark rounded="lg">
              <v-card-title primary class="title">Status Gate Parking</v-card-title>
                <v-row no-gutters>
                  <v-col>
                    <v-sheet class="gate-parking">
                      Gate Masuk 1
                    </v-sheet>
                  </v-col>
                  <v-col>
                    <v-sheet class="status">
                      Aktif
                    </v-sheet>
                  </v-col>

                  <v-responsive width="100%"></v-responsive>

                  <v-col>
                    <v-sheet class="gate-parking">
                      Gate Keluar 1
                    </v-sheet>
                  </v-col>

                  <v-col>
                    <v-sheet class="status">
                      Aktif
                    </v-sheet>
                  </v-col>

                  <v-responsive width="100%"></v-responsive>

                  <v-col>
                    <v-sheet class="gate-parking">
                      Gate Masuk 2
                    </v-sheet>
                  </v-col>

                  <v-col>
                    <v-sheet class="status">
                      Tidak Aktif
                    </v-sheet>
                  </v-col>

                  <v-responsive width="100%"></v-responsive>

                  <v-col>
                    <v-sheet class="gate-parking">
                      Gate Keluar 2
                    </v-sheet>
                  </v-col>

                  <v-col>
                    <v-sheet class="status">
                      Tidak Aktif 
                    </v-sheet>
                  </v-col>
                </v-row>
            </v-card>
          </v-flex>
        </v-sheet>
      </v-col>
    </v-row>
    </v-container>
    
  </div> 
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home-page',
  components: {
  }
}
</script>

<style scoped>
h1 {
  color: rgb(255, 136, 9)
}
.left-side{
  color: rgb(255, 136, 9);
  font-weight : bold;
  justify-content: left;
  border: 1px;
  margin-left: 0px;
  padding-right: 20px;
}
.left-side-title{
  margin-bottom: 20px;
}
.right-side{
  color: rgb(255, 136, 9);
  font-weight : bold
}
.title{
  color: rgb(255, 136, 9);
  text-align: center
}
.info-masuk{
  margin-left: 16px;
  margin-bottom: 16px;
  text-align: center
}
.info-keluar{
  margin-bottom: 16px;
  text-align: center
}
.info-peringatan{
  margin-right: 16px;
  margin-bottom: 16px;
  text-align: center;
}
.gate-parking{
  margin: 2px;
  margin-left: 12px;
  margin-bottom: 12px;
}
.status{
  margin: 2px;
  text-align: right;
  margin-right: 12px;
  margin-bottom: 12px
}
.subtitle{
  text-align: right;
  align: center;
  justify-content: center;
  margin-top: 16px;
}
</style>
