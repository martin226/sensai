<template>
  <div class="min-h-screen flex flex-col justify-center items-center space-y-8">
    <img src="@/assets/img/sensai.svg" alt="Logo" class="w-32" />
    <AuthRegister />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'RegisterPage',
  middleware: 'auth',
  auth: 'guest',
});
</script>
