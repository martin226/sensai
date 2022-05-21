<template>
  <div class="flex flex-col min-h-screen">
    <SharedNavbar />
    <div class="px-4 py-12 flex-1" sm="px-24">
      <h1 class="text-5xl font-serif font-semibold mb-8" md="text-7xl">
        Workouts
      </h1>
      <h3 class="text-3xl font-serif font-semibold mb-2">Search</h3>
      <div class="mb-16 relative">
        <input
          v-model="search"
          type="text"
          class="rounded-xl border-2 border-primary w-full focus:outline-green-600 px-16"
        />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 text-primary absolute bottom-2.5 left-4"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          />
        </svg>
      </div>
      <div class="flex flex-wrap gap-8 justify-center" md="justify-start">
        <NuxtLink
          v-for="w in filteredWorkouts"
          :key="w.id"
          :to="`/workout/${w.workoutId}`"
        >
          <WorkoutCard
            :workout-name="w.workoutName"
            :workout-image="w.workoutImage"
          />
        </NuxtLink>
        <p
          v-if="!filteredWorkouts.length"
          class="text-lg text-center font-serif w-full"
        >
          No search results found.
        </p>
      </div>
    </div>
    <SharedFooter />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'DashboardPage',
  middleware: 'auth',
  data() {
    return {
      search: '',
      workouts: [] as any[],
    };
  },
  async fetch() {
    const response = await this.$axios.get('/api/workout/list');
    for (const workout of response.data.workouts) {
      this.workouts.push({
        workoutId: workout.id,
        workoutName: workout.name,
        workoutImage: workout.image,
      });
    }
  },
  computed: {
    filteredWorkouts(): {
      workoutId: string;
      workoutName: string;
      workoutImage: string;
    }[] {
      return this.workouts.filter((w: any) =>
        w.workoutName.toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
});
</script>
