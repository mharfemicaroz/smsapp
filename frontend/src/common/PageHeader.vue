<template>
  <div class="page-header">
    <div class="row">
      <div class="col-sm-12">
        <div class="page-sub-header">
          <h3 class="page-title">Welcome {{ first_name }}!</h3>
          <ul class="breadcrumb">
            <li class="breadcrumb-item"><a href="index.html">Home</a></li>
            <li class="breadcrumb-item active">{{ $route.name }}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { useAuthStore } from "@/stores/authStore";
export default {
  data() {
    return {
      first_name: "",
    };
  },
  mounted() {
    const authStore = useAuthStore();
    this.first_name = authStore.user.first_name;
  },
};
</script>
