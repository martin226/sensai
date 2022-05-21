<template>
  <form
    class="flex flex-col justify-center items-center"
    @submit.prevent="login"
  >
    <div class="space-y-8 w-full">
      <h2 class="text-4xl font-bold text-center">Login</h2>
      <div
        v-if="error"
        class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative"
        role="alert"
      >
        <span class="block sm:inline">{{ error }}</span>
      </div>
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
        <span class="text-gray-700">Password</span>
        <div class="relative">
          <input
            v-model="user.password"
            :type="showPassword ? 'text' : 'password'"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-0 focus:outline-none"
            required
            autocomplete="current-password"
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
        Login
      </button>
      <p class="text-center text-gray-500 mt-1">
        Don't have an account yet? Click
        <NuxtLink to="/register" class="text-blue-400">here</NuxtLink> to
        register.
      </p>
    </div>
  </form>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'AuthLogin',
  data() {
    return {
      user: {
        username: '',
        password: '',
      },
      showPassword: false,
      error: '',
    };
  },
  methods: {
    async login() {
      this.error = '';
      try {
        await this.$auth.loginWith('local', {
          data: this.user,
        });
      } catch (error: any) {
        if (error.response && error.response.data.message) {
          this.error = error.response.data.message;
        }
      }
    },
  },
});
</script>
