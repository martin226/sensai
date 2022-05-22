<template>
  <div>
    <div class="space-y-4">
      <div class="w-full bg-gray-200 rounded-full h-2.5 mb-8">
        <div
          class="bg-primary h-2.5 rounded-full"
          :style="{
            width: `${(idx / exercises.length) * 100}%`,
          }"
        ></div>
      </div>
      <h2 class="text-4xl font-serif font-semibold mb-4">
        {{ workoutName }}
      </h2>
      <p class="text-lg mb-4">
        <strong>Current Exercise:</strong>
        {{ exercises[idx].exerciseFormattedName }}
      </p>
      <p class="text-lg mb-4">
        <strong>Elapsed Time:</strong>
        {{ elapsedTime }}
      </p>
      <p class="text-lg mb-4">
        <strong>Reps Remaining:</strong>
        {{ exercises[idx].exerciseReps - reps }}
      </p>
    </div>
    <div
      v-if="formHint"
      class="bg-orange-100 border-l-4 border-orange-500 text-orange-700 p-4 my-8"
      role="alert"
    >
      <p class="font-bold">Improve Your Form</p>
      <p>{{ formHint }}</p>
    </div>
    <div class="grid grid-cols-1 gap-8 mb-16" md="grid-cols-2">
      <div class="flex justify-center items-center">
        <img
          :src="exercises[idx].exerciseImage"
          :alt="workoutName"
          class="rounded-lg h-full object-cover object-center"
        />
      </div>
      <div class="flex justify-center items-center">
        <video
          v-show="cameraActive"
          ref="video"
          autoplay
          muted
          class="rounded-lg"
        >
          <canvas ref="canvas"></canvas>
        </video>
        <p v-if="!cameraActive" class="text-lg text-center">
          Loading webcam...
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { io, Socket } from 'socket.io-client';
export default Vue.extend({
  name: 'WorkoutCoach',
  props: {
    workoutId: {
      type: String,
      required: true,
    },
    workoutName: {
      type: String,
      required: true,
    },
    exercises: {
      type: Array as () => any[],
      required: true,
    },
  },
  data() {
    return {
      video: null as HTMLVideoElement | null,
      canvas: null as HTMLCanvasElement | null,
      context: null as CanvasRenderingContext2D | null,
      socket: null as Socket | null,
      cameraActive: false,
      idx: 0,
      reps: 0,
      formHint: '',
      state: '',
      time: Date.now(),
      currentTime: Date.now(),
      coachLoop: null as NodeJS.Timer | null,
      elapsedTimeLoop: null as NodeJS.Timer | null,
    };
  },
  computed: {
    elapsedTime(): string {
      return new Date(this.currentTime - this.time).toISOString().slice(14, 19);
    },
  },
  mounted() {
    this.video = this.$refs.video as HTMLVideoElement;
    this.canvas = this.$refs.canvas as HTMLCanvasElement;
    this.context = this.canvas.getContext('2d');
    this.socket = io('', { path: '/api/coach' });
    this.elapsedTimeLoop = setInterval(() => {
      this.currentTime = Date.now();
    }, 1000);

    this.$axios.get('/api/workout/start/' + this.workoutId);

    this.socket.on('coach', (data) => {
      if (data.exercise === this.exercises[this.idx].exerciseName) {
        this.reps = Math.max(data.reps, this.reps);
        if (
          data.formHint &&
          this.formHint !== data.formHint &&
          speechSynthesis
        ) {
          const utterance = new SpeechSynthesisUtterance(data.formHint);
          speechSynthesis.speak(utterance);
        }
        this.formHint = data.formHint;
        this.state = data.state;
      }
    });

    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices
        .getUserMedia({
          video: true,
          audio: false,
        })
        .then((stream) => {
          if (!this.video) return;
          this.video.srcObject = stream;
          this.cameraActive = true;
          this.coachLoop = setInterval(() => {
            if (this.exercises[this.idx].exerciseReps === this.reps) {
              if (this.idx >= this.exercises.length - 1) {
                this.$emit('workout-complete', {
                  elapsedTime: this.elapsedTime,
                });
                this.$axios.get('/api/workout/end/' + this.workoutId);
                this.$destroy();
                return;
              }
              this.idx++;
              this.reps = 0;
              this.formHint = '';
            }
            this.socket!.emit('frame', {
              frame: this.getCurrentFrame()!.split(',')[1],
              reps: this.reps,
              exercise: this.exercises[this.idx].exerciseName,
              prevState: this.state,
            });
          }, 1000 / 30);
        });
    }
  },
  destroyed() {
    if (this.video) {
      const stream = this.video.srcObject as MediaStream;
      if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach((track) => track.stop());
      }
    }
    if (this.socket) {
      this.socket.close();
    }
    if (this.coachLoop) {
      clearInterval(this.coachLoop);
    }
    if (this.elapsedTimeLoop) {
      clearInterval(this.elapsedTimeLoop);
    }
  },
  methods: {
    getCurrentFrame() {
      if (!this.canvas || !this.video || !this.context) return;
      const width = this.video.videoWidth;
      const height = this.video.videoHeight;
      this.canvas.width = width;
      this.canvas.height = height;
      this.context.drawImage(this.video, 0, 0, width, height);
      return this.canvas.toDataURL('image/jpeg', 0.5);
    },
  },
});
</script>
