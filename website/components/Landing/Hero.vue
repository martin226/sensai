<template>
  <div class="bg-primary px-4 flex flex-col justify-center" sm="px-36">
    <h1
      class="lowercase font-bold text-6xl text-secondary mb-4"
      md="text-7xl"
      lg="text-9xl"
    >
      sensai.
    </h1>
    <p class="text-2xl text-gray-100 mb-4">/ˌsenˈsā,senˌsā/</p>
    <p class="text-2xl italics text-gray-300">noun</p>
    <p class="text-xl text-extralight text-secondary mb-8" md="text-2xl">
      the workout platform revolutionizing workouts, with a built-in AI coach
      that changes the way you exercise.
    </p>
    <NuxtLink
      to="/dashboard"
      class="px-8 py-4 border-secondary text-secondary rounded-lg border-2 w-min focus:ring-0 focus:outline-none"
    >
      enter.
    </NuxtLink>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'LandingHero',
});
</script>
