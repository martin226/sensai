<template>
  <div class="border-t-16 border-primary flex justify-between px-24 py-12">
    <NuxtLink to="/"
      ><img src="@/assets/img/sensai.svg" alt="Logo" class="w-28"
    /></NuxtLink>
    <div class="space-x-12">
      <NuxtLink to="/" class="font-serif">home</NuxtLink>
      <NuxtLink to="/dashboard" class="font-serif">workouts</NuxtLink>
      <NuxtLink to="/account" class="font-serif">my account</NuxtLink>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'SharedNavbar',
});
</script>
