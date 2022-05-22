<template>
  <div>
    <div class="w-full bg-primary rounded-full h-2.5 mb-8"></div>
    <h2 class="text-5xl font-serif font-bold text-center mb-16">
      Workout Finished.
    </h2>
    <div class="space-y-8 mb-16">
      <div class="rounded-lg border-primary border-2 flex p-8">
        <div class="flex-1">
          <h3 class="text-3xl font-bold font-serif">Workout Name</h3>
          <h4 class="text-2xl text-gray-400">{{ workoutName }}</h4>
        </div>
        <div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-16 text-primary"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
            />
          </svg>
        </div>
      </div>
      <div class="rounded-lg border-primary border-2 flex p-8">
        <div class="flex-1">
          <h3 class="text-3xl font-bold font-serif">Time Spent</h3>
          <h4 class="text-2xl text-gray-400">{{ elapsedTime }}</h4>
        </div>
        <div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-16 text-primary"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </div>
      </div>
      <h3 class="text-4xl font-serif font-bold">Exercises Done</h3>
      <div class="flex flex-wrap gap-8 justify-center" md="justify-start">
        <WorkoutCard
          v-for="e in exercises"
          :key="e.id"
          :workout-name="e.exerciseFormattedName"
          :workout-image="e.exerciseImage"
        />
      </div>
    </div>
    <div class="flex justify-center">
      <NuxtLink
        to="/dashboard"
        class="bg-primary text-secondary py-4 px-8 rounded-lg"
      >
        Go Back Home
      </NuxtLink>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'WorkoutSummary',
  props: {
    workoutName: {
      type: String,
      required: true,
    },
    exercises: {
      type: Array as () => any[],
      required: true,
    },
    elapsedTime: {
      type: String,
      required: true,
    },
  },
});
</script>
