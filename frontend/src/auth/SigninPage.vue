<template>
  <div class="main-wrapper login-body">
    <div class="login-wrapper">
      <div class="container">
        <div class="loginbox">
          <div class="login-left">
            <img class="img-fluid" src="/img/login.png" alt="Logo" />
          </div>
          <div class="login-right">
            <div class="login-right-wrap">
              <h1>Welcome to ManageEdu</h1>
              <p class="account-subtitle">
                Need an account? <a href="#">Sign Up</a>
              </p>
              <h2>Sign in</h2>

              <form @submit.prevent="login">
                <div class="form-group">
                  <label>Username <span class="login-danger">*</span></label>
                  <input
                    class="form-control"
                    v-model="username"
                    :readonly="isAuthenticated"
                    type="text"
                  />
                  <span class="profile-views"
                    ><i class="fas fa-user-circle"></i
                  ></span>
                </div>
                <div class="form-group">
                  <label>Password <span class="login-danger">*</span></label>
                  <input
                    class="form-control pass-input"
                    type="text"
                    v-model="password"
                    :readonly="isAuthenticated"
                  />
                  <span
                    class="profile-views feather-eye toggle-password"
                  ></span>
                </div>
                <div class="forgotpass">
                  <div class="remember-me">
                    <label
                      class="custom_check mr-2 mb-0 d-inline-flex remember-me"
                    >
                      Remember me
                      <input type="checkbox" name="radio" />
                      <span class="checkmark"></span>
                    </label>
                  </div>
                  <a href="#">Forgot Password?</a>
                </div>
                <div class="form-group">
                  <button
                    class="btn btn-primary btn-block"
                    :disabled="isAuthenticated"
                    type="submit"
                  >
                    Login
                  </button>
                </div>
              </form>

              <div class="login-or">
                <span class="or-line"></span>
                <span class="span-or">or</span>
              </div>

              <div class="social-login">
                <a href="#"><i class="fab fa-google-plus-g"></i></a>
                <a href="#"><i class="fab fa-facebook-f"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-linkedin-in"></i></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <ToasterComponent ref="toast" />
</template>
<script>
import ToasterComponent from "../common/ToasterComponent.vue";
import { useAuthStore } from "@/stores/authStore";
export default {
  data() {
    return {
      username: "",
      password: "",
      isAuthenticated: false,
    };
  },
  methods: {
    async login() {
      const authStore = useAuthStore(); // Access the authStore
      const authAccess = await authStore.login({
        username: this.username,
        password: this.password,
      });

      if (authAccess) {
        this.isAuthenticated = true;
        this.$refs.toast.showToast("success", "Login successfully!");

        let dashboardPath = `/index/dashboard`;
        if (authStore.user.role === "teacher") {
          dashboardPath = `/index/dashboard-1`;
        } else if (authStore.user.role === "student") {
          dashboardPath = `/index/dashboard-2`;
        }

        setTimeout(() => {
          this.$router.push(dashboardPath);
        }, 1000);
      } else {
        this.$refs.toast.showToast("danger", "Invalid login credentials!");
      }
    },
  },
  components: { ToasterComponent },
};
</script>
