<template>
 <v-container>
  <v-row no-gutters>
    <v-col>
      <v-card-title primary class="title">Status Pengguna Gedung Parkir Mahasiswa Politeknik Negeri Bandung</v-card-title>
    </v-col>
    <v-col cols="auto">
      <v-btn class="left" variant="outlined" color="indigo" prepend-icon="mdi-bell-outline">Button</v-btn>
      <v-btn class="right" variant="elevated" color="indigo" prepend-icon="mdi-plus">Add Record</v-btn>
    </v-col>
  </v-row>
  <v-data-table
    v-model:items-per-page="itemsPerPage"
    :headers="headers"
    :items="desserts"
    item-value="name"
    class="elevation-1"
  ></v-data-table>
 </v-container>
</template>

<script>
  export default{
    name : 'dashboard-page',
    data () {
      return {
        itemsPerPage: 5,
        headers: [
          {
            title: 'RFID',
            align: 'start',
            sortable: false,
            key: 'name',
          },
          { title: 'Plat Nomor', align: 'end', key: 'calories' },
          { title: 'Waktu Masuk', align: 'end', key: 'fat' },
          { title: 'Waktu Keluar', align: 'end', key: 'carbs' },
          { title: 'Bukti Masuk', align: 'end', key: 'protein' },
          { title: 'Bukti Keluar', align: 'end', key: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: '1',
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: '0',
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: '6',
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: '7',
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: '16',
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: '1',
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: '2',
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: '8',
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: '45',
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: '22',
          },
        ],
      }
    },
  }
</script>
<style scoped>
.title{
  color: rgb(255, 136, 9);
  text-align: left
}
.left{
  variant: outline;
}
.right{
  margin-left: 12px;
}
</style>