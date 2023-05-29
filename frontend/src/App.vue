<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
</template>

<style scoped>
  html body {
      opacity: 1;
      transition: opacity 0.5s ease-in-out;
  }
</style>
