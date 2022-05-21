<template>
  <div class="min-h-screen flex flex-col justify-center items-center space-y-8">
    <img src="@/assets/img/sensai.svg" alt="Logo" class="w-32" />
    <AuthLogin />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'LoginPage',
  middleware: 'auth',
  auth: 'guest',
});
</script>
