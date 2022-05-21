<template>
  <div class="space-y-6">
    <div>
      <img
        :src="workoutImage"
        :alt="workoutName"
        class="rounded-lg border-4 border-primary h-40 w-72 object-cover object-center"
      />
    </div>
    <div>
      <h3 class="text-3xl font-serif font-semibold">
        {{ workoutName }}
      </h3>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'WorkoutCard',
  props: {
    workoutName: {
      type: String,
      required: true,
    },
    workoutImage: {
      type: String,
      required: true,
    },
  },
});
</script>
