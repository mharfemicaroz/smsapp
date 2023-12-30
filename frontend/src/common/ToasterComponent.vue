<template>
    <div
      v-if="show"
      class="position-fixed top-0 end-0 p-3"
      style="z-index: 99999"
    >
      <div
        id="liveToast"
        :class="`toast show bg-${toastType} text-white`"
        style="width: fit-content"
        role="alert"
        aria-live="polite"
        aria-atomic="true"
      >
        <div class="d-flex">
          <div class="toast-body">{{ toastMessage }}</div>
          <button
            type="button"
            class="btn-close btn-close-white me-2 m-auto"
            @click="hideToast"
            aria-label="Close"
          ></button>
        </div>
        <div class="progress">
          <div :style="{ width: progress + '%' }" class="progress-bar"></div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      initialToastType: {
        type: String,
        default: "success",
      },
      initialToastMessage: {
        type: String,
        default: "This is a toast message.",
      },
    },
    data() {
      return {
        toastType: this.initialToastType, // Initialize with prop
        toastMessage: this.initialToastMessage, // Initialize with prop
        show: false,
        progress: 0,
        timer: null,
      };
    },
    methods: {
      showToast(type, message) {
        this.show = true;
        this.progress = 0;
        this.toastType = type;
        this.toastMessage = message;
        this.timer = setInterval(() => {
          this.progress += 10;
          if (this.progress >= 100) {
            this.hideToast();
          }
        }, 300);
      },
      hideToast() {
        this.show = false;
        this.progress = 0;
        clearInterval(this.timer);
        this.$emit("toastClosed");
      },
    },
  };
  </script>
  
  <style scoped>
  .progress {
    height: 5px;
  }
  .progress-bar {
    background-color: white;
  }
  </style>
  