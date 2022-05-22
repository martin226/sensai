<template>
  <div class="flex flex-col min-h-screen">
    <SharedNavbar />
    <div class="px-4 py-12 flex-1" sm="px-24">
      <WorkoutInfo
        v-if="stage == 0"
        :workout-image="workoutImage"
        :workout-name="workoutName"
        :exercises="exercises"
        @started="stage++"
      />
      <WorkoutCoach
        v-if="stage == 1"
        :workout-id="workoutId"
        :workout-name="workoutName"
        :exercises="exercises"
        @workout-complete="
          (x) => {
            stage++;
            elapsedTime = x.elapsedTime;
          }
        "
      />
      <WorkoutSummary
        v-if="stage == 2"
        :workout-name="workoutName"
        :exercises="exercises"
        :elapsed-time="elapsedTime"
      />
    </div>
    <SharedFooter />
  </div>
</template>

<script>
export default {
  async asyncData({ params, $axios }) {
    const id = params.id;
    const response = await $axios.get('/api/workout/' + id);
    const exercises = [];
    for (const exercise of response.data.workout.exercise_list) {
      exercises.push({
        exerciseFormattedName:
          exercise.name
            .replace('_', ' ')
            .split(' ')
            .map((x) => x.charAt(0).toUpperCase() + x.slice(1))
            .join(' ') +
          ' - ' +
          exercise.reps +
          ' Reps',
        exerciseImage: exercise.image,
        exerciseId: exercise.id,
        exerciseName: exercise.name,
        exerciseReps: exercise.reps,
      });
    }
    return {
      workoutId: id,
      workoutImage: response.data.workout.image,
      workoutName: response.data.workout.name,
      exercises,
    };
  },
  data() {
    return {
      stage: 0,
      elapsedTime: '',
    };
  },
};
</script>
