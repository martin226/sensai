<template>
  <form
    class="flex flex-col justify-center items-center"
    @submit.prevent="register"
  >
    <div class="space-y-8 w-full">
      <h2 class="text-4xl font-bold text-center">Register</h2>
      <label class="block">
        <span class="text-gray-700">Username</span>
        <input
          v-model="user.username"
          type="text"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-0 focus:outline-none"
          required
          autocomplete="username"
        />
      </label>
      <label class="block">
        <span class="text-gray-700">Email Address</span>
        <input
          v-model="user.email"
          type="email"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-0 focus:outline-none"
          required
          autocomplete="email"
        />
      </label>
      <label class="block">
        <span class="text-gray-700">Password</span>
        <div class="relative">
          <input
            v-model="user.password"
            :type="showPassword ? 'text' : 'password'"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-0 focus:outline-none"
            required
            autocomplete="new-password"
          />
          <span
            class="absolute right-3 bottom-2.5"
            role="button"
            @click="showPassword = !showPassword"
          >
            <IconEye v-if="showPassword" class="text-gray-400" />
            <IconEyeOff v-else class="text-gray-400" />
          </span>
        </div>
      </label>
      <button
        type="submit"
        class="bg-green-600 text-white py-4 rounded-lg w-full hover:opacity-90 transition-opacity duration-150"
      >
        Register
      </button>
      <p class="text-center text-gray-500 mt-1">
        Already have an account? Click
        <NuxtLink to="/login" class="text-blue-400">here</NuxtLink> to login.
      </p>
    </div>
  </form>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'AuthRegister',
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: '',
      },
      showPassword: false,
    };
  },
  methods: {
    async register() {},
  },
});
</script>
