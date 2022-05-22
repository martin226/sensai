<template>
  <div>
    <div class="grid grid-cols-1 gap-8 mb-16" md="grid-cols-2">
      <div class="flex justify-center items-center">
        <img
          :src="workoutImage"
          :alt="workoutName"
          class="rounded-lg h-lg object-cover object-center"
        />
      </div>
      <div class="flex flex-col space-y-8 justify-center items-center">
        <h3 class="text-3xl font-serif font-semibold">{{ workoutName }}</h3>
        <button
          class="bg-primary text-secondary py-4 px-8 rounded-lg"
          @click="$emit('started')"
        >
          Start >
        </button>
      </div>
    </div>
    <div class="flex flex-wrap gap-8 justify-center" md="justify-start">
      <WorkoutCard
        v-for="e in exercises"
        :key="e.id"
        :workout-name="e.exerciseFormattedName"
        :workout-image="e.exerciseImage"
      />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'WorkoutInfo',
  props: {
    workoutName: {
      type: String,
      required: true,
    },
    workoutImage: {
      type: String,
      required: true,
    },
    exercises: {
      type: Array,
      required: true,
    },
  },
});
</script>
